using UnityEngine;
using UnityEngine.Rendering.Universal;
using Firefly.Light;

namespace Firefly.Hazards
{
    /// <summary>
    /// Cave Bat enemy that patrols back and forth in the dark.
    /// Emits faint red light from its glowing eyes to signal danger.
    /// Follows the Single Responsibility Principle: manages bat patrol movement and player contact damage.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class EnemyPatrol : MonoBehaviour
    {
        [Header("Movement Settings")]
        [Tooltip("Horizontal patrol speed in units per second.")]
        [SerializeField] private float speed = 2.5f;

        [Tooltip("Horizontal distance from start position to travel before turning around.")]
        [SerializeField] private float patrolDistance = 4.0f;

        [Tooltip("Frequency of vertical wing bobbing.")]
        [SerializeField] private float flyWaveSpeed = 6.0f;

        [Tooltip("Amplitude of vertical wing bobbing.")]
        [SerializeField] private float flyWaveHeight = 0.25f;

        [Header("Combat Settings")]
        [Tooltip("Light energy drained on contact.")]
        [SerializeField] private float damageAmount = 25f;

        [Tooltip("Knockback force applied to the player.")]
        [SerializeField] private float knockbackForce = 10f;

        [Tooltip("Hit cooldown per target.")]
        [SerializeField] private float hitCooldown = 0.75f;

        [Header("Visuals & Lighting")]
        [SerializeField] private SpriteRenderer spriteRenderer;
        [SerializeField] private Light2D eyeGlowLight;

        private Vector3 startPosition;
        private int movingDirection = 1; // 1 = right, -1 = left
        private float lastHitTime;
        private float waveTimer;

        private void Awake()
        {
            if (spriteRenderer == null)
                spriteRenderer = GetComponentInChildren<SpriteRenderer>();

            if (eyeGlowLight == null)
                eyeGlowLight = GetComponentInChildren<Light2D>();

            Collider2D col = GetComponent<Collider2D>();
            col.isTrigger = true;
        }

        private void Start()
        {
            startPosition = transform.position;
        }

        private void Update()
        {
            PatrolMovement();
            UpdateVisuals();
        }

        private void PatrolMovement()
        {
            // Move horizontally
            float newX = transform.position.x + (movingDirection * speed * Time.deltaTime);

            // Check patrol bounds
            float distFromOrigin = newX - startPosition.x;
            if (Mathf.Abs(distFromOrigin) >= patrolDistance)
            {
                movingDirection *= -1;
                newX = startPosition.x + (Mathf.Sign(distFromOrigin) * patrolDistance);
            }

            // Bat flight wavy vertical motion
            waveTimer += Time.deltaTime * flyWaveSpeed;
            float newY = startPosition.y + (Mathf.Sin(waveTimer) * flyWaveHeight);

            transform.position = new Vector3(newX, newY, startPosition.z);
        }

        private void UpdateVisuals()
        {
            // Facing flip
            if (spriteRenderer != null)
            {
                spriteRenderer.flipX = (movingDirection < 0);
            }
        }

        private void OnTriggerStay2D(Collider2D other)
        {
            TryDamage(other.gameObject);
        }

        private void OnTriggerEnter2D(Collider2D other)
        {
            TryDamage(other.gameObject);
        }

        private void TryDamage(GameObject target)
        {
            if (Time.time - lastHitTime < hitCooldown) return;

            LightEnergy light = target.GetComponent<LightEnergy>();
            if (light == null)
            {
                light = target.GetComponentInParent<LightEnergy>();
            }

            if (light != null)
            {
                lastHitTime = Time.time;

                Vector2 knockbackDir = (target.transform.position - transform.position).normalized;
                if (Mathf.Abs(knockbackDir.x) < 0.2f)
                {
                    knockbackDir.x = movingDirection;
                }
                knockbackDir.y = Mathf.Max(0.5f, knockbackDir.y);
                knockbackDir.Normalize();

                light.TakeDamage(damageAmount, knockbackDir, knockbackForce);
            }
        }

        private void OnDrawGizmosSelected()
        {
            Gizmos.color = Color.red;
            Vector3 center = Application.isPlaying ? startPosition : transform.position;
            Gizmos.DrawLine(center - Vector3.right * patrolDistance, center + Vector3.right * patrolDistance);
            Gizmos.DrawWireSphere(center - Vector3.right * patrolDistance, 0.2f);
            Gizmos.DrawWireSphere(center + Vector3.right * patrolDistance, 0.2f);
        }
    }
}
