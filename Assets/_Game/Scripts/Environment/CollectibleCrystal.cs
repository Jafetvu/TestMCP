using System;
using UnityEngine;
using UnityEngine.Rendering.Universal;
using Firefly.Light;
using Firefly.Core;

namespace Firefly.Environment
{
    /// <summary>
    /// Collectible Light Crystal that recharges the firefly's light energy
    /// and contributes to opening the level's exit portal.
    /// Follows the Single Responsibility Principle: handles crystal state and pickup reaction.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class CollectibleCrystal : MonoBehaviour
    {
        [Header("Recharge Settings")]
        [Tooltip("Amount of light energy restored upon collection.")]
        [SerializeField] private float energyRestored = 35f;

        [Header("Visuals & Animation")]
        [SerializeField] private SpriteRenderer spriteRenderer;
        [SerializeField] private Light2D crystalLight;
        [SerializeField] private float bobSpeed = 3f;
        [SerializeField] private float bobHeight = 0.15f;
        [SerializeField] private float pulseSpeed = 4f;

        [Header("Collection FX")]
        [SerializeField] private ParticleSystem collectParticles;

        private Vector3 startPosition;
        private bool isCollected;
        private float baseLightIntensity = 1.0f;

        public static event Action<CollectibleCrystal> OnAnyCrystalCollected;

        [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
        private static void ResetStatics()
        {
            OnAnyCrystalCollected = null;
        }

        private void Awake()
        {
            if (spriteRenderer == null)
                spriteRenderer = GetComponentInChildren<SpriteRenderer>();

            if (crystalLight == null)
                crystalLight = GetComponentInChildren<Light2D>();

            if (crystalLight != null)
                baseLightIntensity = crystalLight.intensity;

            Collider2D col = GetComponent<Collider2D>();
            col.isTrigger = true;
        }

        private void Start()
        {
            startPosition = transform.position;

            // Auto-register with LevelManager if present
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.RegisterCrystal(this);
            }
        }

        private void Update()
        {
            if (isCollected) return;

            // Smooth floating bob
            float newY = startPosition.y + Mathf.Sin(Time.time * bobSpeed) * bobHeight;
            transform.position = new Vector3(startPosition.x, newY, startPosition.z);

            // Subtle light breathing pulse
            if (crystalLight != null)
            {
                float pulse = 1f + Mathf.Sin(Time.time * pulseSpeed) * 0.15f;
                crystalLight.intensity = baseLightIntensity * pulse;
            }
        }

        private void OnTriggerEnter2D(Collider2D other)
        {
            if (isCollected) return;

            // Verify if player collided
            if (other.CompareTag("Player") || other.GetComponent<LightEnergy>() != null)
            {
                Collect(other.gameObject);
            }
        }

        private void Collect(GameObject player)
        {
            isCollected = true;

            // Recharge player's light energy
            LightEnergy lightEnergy = player.GetComponent<LightEnergy>();
            if (lightEnergy != null)
            {
                lightEnergy.AddEnergy(energyRestored);
            }

            // Fire events
            OnAnyCrystalCollected?.Invoke(this);

            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnCrystalCollected(this);
            }

            // Play particles
            if (collectParticles != null)
            {
                collectParticles.transform.parent = null;
                collectParticles.Play();
                Destroy(collectParticles.gameObject, 1.5f);
            }

            // Disable visuals and collider immediately
            if (spriteRenderer != null) spriteRenderer.enabled = false;
            if (crystalLight != null) crystalLight.enabled = false;
            GetComponent<Collider2D>().enabled = false;

            Destroy(gameObject, 0.5f);
        }
    }
}
