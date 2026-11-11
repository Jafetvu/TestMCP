using UnityEngine;
using Firefly.Light;

namespace Firefly.Hazards
{
    /// <summary>
    /// Static hazardous obstacle (stalagmites/spikes) that drains light energy
    /// and repels the firefly on contact.
    /// Follows the Single Responsibility Principle: handles static spike damage and knockback.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class HazardSpikes : MonoBehaviour
    {
        [Header("Damage Settings")]
        [Tooltip("Amount of light energy drained on contact.")]
        [SerializeField] private float damageAmount = 30f;

        [Tooltip("Upward/outward knockback impulse.")]
        [SerializeField] private float knockbackForce = 9f;

        [Tooltip("Cooldown in seconds between hits on the same target to avoid multi-hitting every frame.")]
        [SerializeField] private float damageCooldown = 0.6f;

        private float lastDamageTime;

        private void Awake()
        {
            Collider2D col = GetComponent<Collider2D>();
            // Can be trigger or solid collider; isTrigger allows smooth pass-through hurtbox
            col.isTrigger = true;
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
            if (Time.time - lastDamageTime < damageCooldown) return;

            LightEnergy light = target.GetComponent<LightEnergy>();
            if (light == null)
            {
                light = target.GetComponentInParent<LightEnergy>();
            }

            if (light != null)
            {
                lastDamageTime = Time.time;

                // Calculate knockback direction: away and upward from spikes
                Vector2 dir = (target.transform.position - transform.position).normalized;
                if (dir.y < 0.3f) dir.y = 0.8f;
                dir.Normalize();

                light.TakeDamage(damageAmount, dir, knockbackForce);
            }
        }
    }
}
