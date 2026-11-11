using System;
using System.Collections.Generic;
using UnityEngine;
using Firefly.Core;
using Firefly.Environment;

namespace Firefly.Player
{
    /// <summary>
    /// Controls 2D movement, jumping, mid-air wing flaps and gliding for the firefly.
    /// Follows the Single Responsibility Principle: handles player locomotion and physical response.
    /// </summary>
    [RequireComponent(typeof(Rigidbody2D))]
    [RequireComponent(typeof(Collider2D))]
    public class PlayerController : MonoBehaviour
    {
        [Header("Movement")]
        [Tooltip("Horizontal speed in units per second.")]
        [SerializeField] private float moveSpeed = 6.5f;

        [Header("Jump & Flight")]
        [Tooltip("Upward velocity applied when jumping from the ground.")]
        [SerializeField] private float jumpForce = 9.5f;

        [Tooltip("Upward velocity applied on each mid-air wing flap.")]
        [SerializeField] private float airFlapForce = 8.0f;

        [Tooltip("Mid-air flaps available before needing to land.")]
        [SerializeField] private int maxAirFlaps = 3;

        [Tooltip("Maximum fall speed while holding jump (glide).")]
        [SerializeField] private float glideMaxFallSpeed = -2.0f;

        [Tooltip("Maximum fall speed when not gliding.")]
        [SerializeField] private float normalMaxFallSpeed = -9.0f;

        [Tooltip("Rigidbody gravity scale.")]
        [SerializeField] private float gravityScale = 1.6f;

        [Header("Ground Detection")]
        [Tooltip("Layers considered walkable ground.")]
        [SerializeField] private LayerMask groundLayer = ~0;

        [Header("Visuals")]
        [Tooltip("Optional CHILD transform used for the hover bobbing. Must not be the root transform.")]
        [SerializeField] private Transform visualTransform;

        // Gameplay events (audio / feedback hooks)
        public event Action OnJump;
        public event Action OnFlutter;
        public event Action OnLand;
        public event Action OnDamaged;

        private const float CoyoteDuration = 0.12f;
        private const float JumpBufferDuration = 0.12f;
        // Ignore ground contact briefly after jumping so the jump is not cancelled on the same frame.
        private const float GroundIgnoreAfterJump = 0.1f;

        private Rigidbody2D rb;
        private Collider2D col;
        private ContactFilter2D groundFilter;
        private readonly List<Collider2D> groundHits = new List<Collider2D>(8);

        private bool isGrounded;
        private MovingPlatform currentPlatform;
        private int remainingAirFlaps;
        private float horizontalInput;
        private bool jumpHeld;
        private float coyoteTimer;
        private float jumpBufferTimer;
        private float groundIgnoreTimer;

        private bool isKnockedBack;
        private float knockbackTimer;
        private bool canMove = true;

        private float bobTimer;
        private Vector3 visualBaseLocalPos;

        public bool IsGrounded => isGrounded;

        private void Awake()
        {
            rb = GetComponent<Rigidbody2D>();
            col = GetComponent<Collider2D>();

            rb.bodyType = RigidbodyType2D.Dynamic;
            rb.gravityScale = gravityScale;
            rb.collisionDetectionMode = CollisionDetectionMode2D.Continuous;
            rb.interpolation = RigidbodyInterpolation2D.Interpolate;
            rb.constraints = RigidbodyConstraints2D.FreezeRotation;

            groundFilter = new ContactFilter2D { useTriggers = false };
            groundFilter.SetLayerMask(groundLayer);

            // Bobbing the root would teleport the player every frame, so only child transforms are allowed.
            if (visualTransform == transform)
                visualTransform = null;
            if (visualTransform != null)
                visualBaseLocalPos = visualTransform.localPosition;

            remainingAirFlaps = maxAirFlaps;
        }

        private void Update()
        {
            if (!canMove)
            {
                horizontalInput = 0f;
                jumpHeld = false;
                return;
            }

            horizontalInput = GameInput.GetHorizontal();
            jumpHeld = GameInput.GetJumpHeld();

            if (GameInput.GetJumpDown())
                jumpBufferTimer = JumpBufferDuration;
            else
                jumpBufferTimer -= Time.deltaTime;

            coyoteTimer = isGrounded ? CoyoteDuration : coyoteTimer - Time.deltaTime;

            if (jumpBufferTimer > 0f)
            {
                if (coyoteTimer > 0f)
                {
                    GroundJump();
                }
                else if (remainingAirFlaps > 0)
                {
                    AirFlap();
                }
            }

            if (Mathf.Abs(horizontalInput) > 0.05f)
            {
                Vector3 scale = transform.localScale;
                scale.x = Mathf.Sign(horizontalInput) * Mathf.Abs(scale.x);
                transform.localScale = scale;
            }

            ApplyVisualHover();
        }

        private void FixedUpdate()
        {
            UpdateGrounded();

            if (isKnockedBack)
            {
                knockbackTimer -= Time.fixedDeltaTime;
                if (knockbackTimer <= 0f)
                    isKnockedBack = false;
                return;
            }

            Vector2 velocity = rb.linearVelocity;
            Vector2 platformVelocity = (isGrounded && currentPlatform != null) ? currentPlatform.Velocity : Vector2.zero;

            velocity.x = (canMove ? horizontalInput * moveSpeed : 0f) + platformVelocity.x;

            // Glide: holding jump while falling caps descent speed.
            float fallLimit = (jumpHeld && !isGrounded) ? glideMaxFallSpeed : normalMaxFallSpeed;
            if (velocity.y < fallLimit)
                velocity.y = fallLimit;

            // Follow vertical platforms while standing on them.
            if (isGrounded && currentPlatform != null && groundIgnoreTimer <= 0f)
                velocity.y = platformVelocity.y;

            rb.linearVelocity = velocity;
        }

        private void UpdateGrounded()
        {
            if (groundIgnoreTimer > 0f)
            {
                groundIgnoreTimer -= Time.fixedDeltaTime;
                SetGrounded(false, null);
                return;
            }

            Bounds b = col.bounds;
            Vector2 center = new Vector2(b.center.x, b.min.y - 0.05f);
            Vector2 size = new Vector2(b.size.x * 0.8f, 0.1f);

            groundHits.Clear();
            Physics2D.OverlapBox(center, size, 0f, groundFilter, groundHits);

            bool found = false;
            MovingPlatform platform = null;
            foreach (Collider2D hit in groundHits)
            {
                if (hit == col || hit.transform.IsChildOf(transform))
                    continue;

                found = true;
                MovingPlatform mp = hit.GetComponent<MovingPlatform>();
                if (mp != null)
                {
                    platform = mp;
                    break;
                }
            }

            SetGrounded(found, platform);
        }

        private void SetGrounded(bool grounded, MovingPlatform platform)
        {
            bool wasGrounded = isGrounded;
            isGrounded = grounded;
            currentPlatform = grounded ? platform : null;

            if (grounded)
                remainingAirFlaps = maxAirFlaps;

            if (!wasGrounded && grounded)
                OnLand?.Invoke();
        }

        private void GroundJump()
        {
            jumpBufferTimer = 0f;
            coyoteTimer = 0f;
            groundIgnoreTimer = GroundIgnoreAfterJump;
            isGrounded = false;
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, jumpForce);
            OnJump?.Invoke();
        }

        private void AirFlap()
        {
            jumpBufferTimer = 0f;
            remainingAirFlaps--;
            rb.linearVelocity = new Vector2(rb.linearVelocity.x, airFlapForce);
            OnFlutter?.Invoke();
        }

        private void ApplyVisualHover()
        {
            if (visualTransform == null) return;
            bobTimer += Time.deltaTime * 6f;
            visualTransform.localPosition = visualBaseLocalPos + new Vector3(0f, Mathf.Sin(bobTimer) * 0.05f, 0f);
        }

        /// <summary>
        /// Pushes the player away from a hazard and briefly suspends input-driven movement.
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
            if (!active)
                rb.linearVelocity = new Vector2(0f, rb.linearVelocity.y);
        }
    }
}
