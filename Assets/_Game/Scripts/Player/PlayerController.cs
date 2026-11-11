using System;
using UnityEngine;
using Firefly.Core;

namespace Firefly.Player
{
    /// <summary>
    /// Controls 2D movement, jumping, wing flutter, and gliding for the firefly.
    /// Follows the Single Responsibility Principle: handles player locomotion and physical response.
    /// </summary>
    [RequireComponent(typeof(Rigidbody2D))]
    [RequireComponent(typeof(Collider2D))]
    public class PlayerController : MonoBehaviour
    {
        [Header("Movement Settings")]
        [Tooltip("Horizontal speed in units per second.")]
        [SerializeField] private float moveSpeed = 6.5f;

        [Header("Jump & Flight Settings")]
        [Tooltip("Upward impulse velocity when jumping from the ground.")]
        [SerializeField] private float jumpForce = 9.5f;

        [Tooltip("Upward impulse velocity when fluttering mid-air.")]
        [SerializeField] private float airFlapForce = 8.0f;

        [Tooltip("Maximum mid-air flutter flaps before needing to land.")]
        [SerializeField] private int maxAirFlaps = 3;

        [Tooltip("Gliding fall speed limit while holding the jump key.")]
        [SerializeField] private float glideMaxFallSpeed = -2.0f;

        [Tooltip("Normal maximum downward fall speed.")]
        [SerializeField] private float normalMaxFallSpeed = -9.0f;

        [Header("Ground Check")]
        [SerializeField] private Transform groundCheck;
        [SerializeField] private Vector2 groundCheckSize = new Vector2(0.5f, 0.2f);
        [SerializeField] private LayerMask groundLayer = ~0; // Default: all layers

        [Header("Visuals & Feedback")]
        [SerializeField] private SpriteRenderer spriteRenderer;
        [Tooltip("Visual container for bobbing/wing animations.")]
        [SerializeField] private Transform visualTransform;

        // Audio Events / Hooks
        public event Action OnJump;
        public event Action OnFlutter;
        public event Action OnLand;
        public event Action OnDamaged;

        // Internal State
        private Rigidbody2D rb;
        private Collider2D col;
        private bool isGrounded;
        private bool wasGrounded;
        private int remainingAirFlaps;
        private float horizontalInput;
        private bool jumpPressed;
        private bool jumpHeld;
        private float coyoteTimer;
        private const float CoyoteDuration = 0.18f;

        // Knockback / Control Lock
        private bool isKnockedBack;
        private float knockbackTimer;
        private bool canMove = true;

        // Subtle visual hover
        private float bobTimer;

        public bool IsGrounded => isGrounded;
        public Rigidbody2D Rigidbody => rb;

        private void Awake()
        {
            rb = GetComponent<Rigidbody2D>();
            col = GetComponent<Collider2D>();

            if (spriteRenderer == null)
                spriteRenderer = GetComponentInChildren<SpriteRenderer>();

            if (visualTransform == null && spriteRenderer != null)
                visualTransform = spriteRenderer.transform;

            rb.gravityScale = 1.6f;
            rb.collisionDetectionMode = CollisionDetectionMode2D.Continuous;
            rb.interpolation = RigidbodyInterpolation2D.Interpolate;
            rb.constraints = RigidbodyConstraints2D.FreezeRotation;
        }

        private void Update()
        {
            if (!canMove)
            {
                horizontalInput = 0f;
                return;
            }

            // Read Inputs
            horizontalInput = GameInput.GetHorizontal();
            jumpPressed = GameInput.GetJumpDown();
            jumpHeld = GameInput.GetJumpHeld();

            // Coyote Timer & Air Flap replenishment
            if (isGrounded)
            {
                coyoteTimer = CoyoteDuration;
                remainingAirFlaps = maxAirFlaps;
            }
            else
            {
                coyoteTimer -= Time.deltaTime;
            }

            // Jump / Flap Trigger
            if (jumpPressed)
            {
                if (isGrounded || coyoteTimer > 0f)
                {
                    ExecuteGroundJump();
                    coyoteTimer = 0f;
                }
                else if (remainingAirFlaps > 0)
                {
                    ExecuteAirFlap();
                }
            }

            // Visual Facing Direction
            if (Mathf.Abs(horizontalInput) > 0.05f)
            {
                Vector3 scale = transform.localScale;
                scale.x = Mathf.Sign(horizontalInput) * Mathf.Abs(scale.x);
                transform.localScale = scale;
            }

            // Visual Hover / Bobbing
            ApplyVisualHover();
        }

        private void FixedUpdate()
        {
            // Fallback ground check if collision events didn't catch it
            CheckGroundRaycast();

            if (isKnockedBack)
            {
                knockbackTimer -= Time.fixedDeltaTime;
                if (knockbackTimer <= 0f)
                {
                    isKnockedBack = false;
                }
                return;
            }

            if (!canMove)
            {
                SetVelocity(0f, rb.linearVelocity.y);
                return;
            }

            // 1. Horizontal Locomotion (Crisp and Responsive)
            float targetVelX = horizontalInput * moveSpeed;
            float currentVelY = rb.linearVelocity.y;

            // 2. Gliding Mechanic (Planeo al mantener pulsado Espacio en el aire)
            if (jumpHeld && !isGrounded && currentVelY < 0f)
            {
                // Soft glide: clamp descent speed to gentle float
                currentVelY = Mathf.Max(currentVelY, glideMaxFallSpeed);
            }
            else if (currentVelY < normalMaxFallSpeed)
            {
                // Terminal velocity clamp
                currentVelY = normalMaxFallSpeed;
            }

            SetVelocity(targetVelX, currentVelY);
        }

        private void SetVelocity(float x, float y)
        {
            Vector2 newVel = new Vector2(x, y);
            rb.linearVelocity = newVel;
        }

        private void ExecuteGroundJump()
        {
            isGrounded = false;
            SetVelocity(rb.linearVelocity.x, jumpForce);
            OnJump?.Invoke();
        }

        private void ExecuteAirFlap()
        {
            remainingAirFlaps--;
            // Lift upward cleanly regardless of existing downward momentum
            SetVelocity(rb.linearVelocity.x, airFlapForce);
            OnFlutter?.Invoke();
        }

        private void CheckGroundRaycast()
        {
            if (isGrounded) return;

            // Raycast downward from player bottom
            Bounds b = col.bounds;
            Vector2 origin = new Vector2(b.center.x, b.min.y + 0.05f);
            RaycastHit2D hit = Physics2D.Raycast(origin, Vector2.down, 0.15f);

            if (hit.collider != null && hit.collider != col && !hit.collider.isTrigger)
            {
                SetGrounded(true);
            }
        }

        private void OnCollisionEnter2D(Collision2D collision)
        {
            EvaluateContacts(collision);
        }

        private void OnCollisionStay2D(Collision2D collision)
        {
            EvaluateContacts(collision);
        }

        private void OnCollisionExit2D(Collision2D collision)
        {
            SetGrounded(false);
        }

        private void EvaluateContacts(Collision2D collision)
        {
            for (int i = 0; i < collision.contactCount; i++)
            {
                Vector2 normal = collision.GetContact(i).normal;
                // If contact is supporting the player from below
                if (normal.y > 0.45f)
                {
                    SetGrounded(true);
                    return;
                }
            }
        }

        private void SetGrounded(bool grounded)
        {
            wasGrounded = isGrounded;
            isGrounded = grounded;

            if (!wasGrounded && isGrounded)
            {
                remainingAirFlaps = maxAirFlaps;
                OnLand?.Invoke();
            }
        }

        private void ApplyVisualHover()
        {
            if (visualTransform == null) return;
            bobTimer += Time.deltaTime * 6f;
            float bob = Mathf.Sin(bobTimer) * 0.05f;
            visualTransform.localPosition = new Vector3(0f, bob, 0f);
        }

        public void ApplyKnockback(Vector2 direction, float force, float duration = 0.25f)
        {
            isKnockedBack = true;
            knockbackTimer = duration;
            SetVelocity(0f, 0f);
            rb.AddForce(direction.normalized * force, ForceMode2D.Impulse);
            OnDamaged?.Invoke();
        }

        public void SetControlActive(bool active)
        {
            canMove = active;
            if (!active && rb != null)
            {
                SetVelocity(0f, 0f);
            }
        }
    }
}
