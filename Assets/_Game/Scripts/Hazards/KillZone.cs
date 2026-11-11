using UnityEngine;
using Firefly.Light;

namespace Firefly.Hazards
{
    /// <summary>
    /// Abyss trigger that instantly drains all light energy if the player falls off the cave platforms.
    /// Follows the Single Responsibility Principle: handles bottom boundary death detection.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class KillZone : MonoBehaviour
    {
        private void Awake()
        {
            GetComponent<Collider2D>().isTrigger = true;
        }

        private void OnTriggerEnter2D(Collider2D other)
        {
            LightEnergy light = other.GetComponent<LightEnergy>();
            if (light == null)
            {
                light = other.GetComponentInParent<LightEnergy>();
            }

            if (light != null)
            {
                light.ConsumeEnergy(9999f); // Instantly extinguish light in abyss
            }
        }
    }
}
