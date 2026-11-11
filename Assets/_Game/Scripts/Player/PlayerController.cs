using System;
using UnityEngine;
using Firefly.Core;

namespace Firefly.Player
{
    /// <summary>
    /// Controls the 2D movement, flight/flutter, jumping, and physical reactions of the firefly.
    /// Follows the Single Responsibility Principle: handles physical locomotion and input execution.
    /// </summary>
    [RequireComponent(typeof(Rigidbody2D))]
    [RequireComponent(typeof(Collider2D))]
    public class PlayerController : MonoBehaviour
    {
        [Header("Movement Settings")]
        [Tooltip("Horizontal speed in units per second.")]
        [SerializeField] private float moveSpeed = 6.5f;

        [Tooltip("Acceleration factor when changing directions or starting.")]
        [SerializeField] private float acceleration = 35f;

        [Tooltip("Deceleration factor when releasing movement keys.")]
        [SerializeField] private float deceleration = 30f;

        [Header("Jump & Flight Settings")]
        [Tooltip("Initial impulse force when jumping/flapping.")]
        [SerializeField] private float jumpForce = 10f;

        [Tooltip("Maximum number of mid-air flutter flaps before needing to land.")]
        [SerializeField] private int maxAirFlaps = 2;

        [Tooltip("Extra upward force applied while holding the jump button to simulate wing flutter / floatiness.")]
        [SerializeField] private float flutterHoverForce = 12f;

        [Tooltip("Maximum vertical fall speed to prevent dropping like a stone.")]
        [SerializeField] private float maxFallSpeed = -8f;

        [Tooltip("Multiplier applied to gravity when falling without holding jump.")]
        [SerializeField] private float fallGravityMultiplier = 1.6f;

        [Header("Ground Check")]
        [SerializeField] private Transform groundCheck;
        [SerializeField] private Vector2 groundCheckSize = new Vector2(0.4f, 0.15f);
        [SerializeField] private LayerMask groundLayer;

        [Header("Visuals & Feedback")]
        [SerializeField] private SpriteRenderer spriteRenderer;
        [Tooltip("Visual container to apply gentle wing flutter/bobbing.")]
        [SerializeField] private Transform visualTransform;

        [Header("Audio Events / Hooks")]
        public event Action OnJump;
        public event Action OnFlutter;
        public event Action OnLand;
        public event Action OnDamaged;

        // Internal physics & state
        private Rigidbody2D rb;
        private Collider2D col;
        private bool isGrounded;
        private bool wasGrounded;
        private int remainingAirFlaps;
        private float horizontalInput;
        private bool jumpRequested;
        private bool jumpHeld;

        // Coyote time & Jump buffer
        private float coyoteTimeCounter;
        private const float CoyoteTimeDuration = 0.15f;
        private float jumpBufferCounter;
        private const float JumpBufferDuration = 0.15f;

        // Knockback / Inactive state
        private bool isKnockedBack;
        private float knockbackTimer;
        private bool canMove = true;

        // Subtle flight bobbing
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

            rb.gravityScale = 2.0f;
            rb.collisionDetectionMode = CollisionDetectionMode2D.Continuous;
            rb.interpolation = RigidbodyInterpolation2D.Interpolate;
        }

        private void Update()
        {
            if (!canMove)
            {
                horizontalInput = 0f;
                return;
            }

            // Read Input
            horizontalInput = GameInput.GetHorizontal();
            jumpHeld = GameInput.GetJumpHeld();

            if (GameInput.GetJumpDown())
            {
                jumpBufferCounter = JumpBufferDuration;
            }
            else if (jumpBufferCounter > 0f)
            {
                jumpBufferCounter -= Time.deltaTime;
            }

            // Coyote time management
            if (isGrounded)
            {
                coyoteTimeCounter = CoyoteTimeDuration;
                remainingAirFlaps = maxAirFlaps;
            }
            else
            {
                coyoteTimeCounter -= Time.deltaTime;
            }

            // Jump trigger logic (Ground jump or Coyote jump)
            if (jumpBufferCounter > 0f)
            {
                if (coyoteTimeCounter > 0f)
                {
                    ExecuteJump();
                    jumpBufferCounter = 0f;
                    coyoteTimeCounter = 0f;
                }
                else if (remainingAirFlaps > 0)
                {
                    ExecuteAirFlap();
                    jumpBufferCounter = 0f;
                }
            }

            // Visual Facing Direction
            if (Mathf.Abs(horizontalInput) > 0.05f)
            {
                Vector3 scale = transform.localScale;
                scale.x = Mathf.Sign(horizontalInput) * Mathf.Abs(scale.x);
                transform.localScale = scale;
            }

            // Visual Hover / Bobbing effect for firefly
            ApplyVisualHover();
        }

        private void FixedUpdate()
        {
            CheckGround();

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
                rb.linearVelocity = new Vector2(0f, rb.linearVelocity.y);
                return;
            }

            // Horizontal velocity with smooth acceleration and deceleration
            float targetSpeed = horizontalInput * moveSpeed;
            float speedDiff = targetSpeed - rb.linearVelocity.x;
            float accelRate = (Mathf.Abs(targetSpeed) > 0.01f) ? acceleration : deceleration;
            float movement = speedDiff * accelRate * Time.fixedDeltaTime;
            rb.linearVelocity = new Vector2(rb.linearVelocity.x + movement, rb.linearVelocity.y);

            // Wing flutter hover while holding jump
            if (jumpHeld && rb.linearVelocity.y < 2f && !isGrounded)
            {
                rb.AddForce(Vector2.up * flutterHoverForce, ForceMode2D.Force);
            }

            // Variable jump fall gravity tuning
            if (rb.linearVelocity.y < 0f)
            {
                rb.linearVelocity = new Vector2(rb.linearVelocity.x, Mathf.Max(rb.linearVelocity.y, maxFallSpeed));
            }
            else if (rb.linearVelocity.y > 0f && !jumpHeld)
            {
                rb.linearVelocity += Vector2.up * (Physics2D.gravity.y * (fallGravityMultiplier - 1f) * Time.fixedDeltaTime);
            }
        }

        private void CheckGround()
        {
            wasGrounded = isGrounded;

            if (groundCheck != null)
            {
                isGrounded = Physics2D.OverlapBox(groundCheck.position, groundCheckSize, 0f, groundLayer);
            }
            else
            {
                // Fallback: BoxCast from bottom of collider
                Bounds bounds = col.bounds;
                Vector2 origin = new Vector2(bounds.center.x, bounds.min.y);
                RaycastHit2D hit = Physics2D.BoxCast(origin, new Vector2(bounds.size.x * 0.8f, 0.1f), 0f, Vector2.down, 0.1f, groundLayer);
                isGrounded = hit.collider != null;
            }

            // Landing event
            if (!wasGrounded && isGrounded)
            {
                OnLand?.Invoke();
            }
        }

        private void ExecuteJump()
        {
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpForce);
            OnJump?.Invoke();
        }

        private void ExecuteAirFlap()
        {
            remainingAirFlaps--;
            // Reset negative vertical velocity so the flap lifts cleanly
            float upwardVel = Mathf.Max(jumpForce * 0.85f, jumpForce * 0.85f);
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, upwardVel);
            OnFlutter?.Invoke();
        }

        private void ApplyVisualHover()
        {
            if (visualTransform == null) return;

            bobTimer += Time.deltaTime * 6f;
            float bobOffset = Mathf.Sin(bobTimer) * 0.06f;
            visualTransform.localPosition = new Vector3(0f, bobOffset, 0f);
        }

        /// <summary>
        /// Applies knockback force when hitting an obstacle or enemy.
        /// </summary>
        public void ApplyKnockback(Vector2 direction, float force, float duration = 0.25f)
        {
            isKnockedBack = true;
            knockbackTimer = duration;
            rb.linearVelocity = Vector2.zero;
            rb.AddForce(direction.normalized * force, ForceMode2D.Impulse);
            OnDamaged?.Invoke();
        }

        public void SetControlActive(bool active)
        {
            canMove = active;
            if (!active && rb != null)
            {
                rb.linearVelocity = Vector2.zero;
            }
        }

        private void OnDrawGizmosSelected()
        {
            Gizmos.color = Color.green;
            if (groundCheck != null)
            {
                Gizmos.DrawWireCube(groundCheck.position, groundCheckSize);
            }
            else if (GetComponent<Collider2D>() != null)
            {
                Bounds bounds = GetComponent<Collider2D>().bounds;
                Gizmos.DrawWireCube(new Vector3(bounds.center.x, bounds.min.y - 0.05f, 0f), new Vector3(bounds.size.x * 0.8f, 0.1f, 0f));
            }
        }
    }
}
