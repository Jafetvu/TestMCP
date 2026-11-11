using System;
using UnityEngine;
using UnityEngine.Rendering.Universal;
using Firefly.Player;

namespace Firefly.Light
{
    /// <summary>
    /// Manages the firefly's light energy, consumption over time, recharge from crystals,
    /// dynamic radius/intensity scaling of the 2D Light, and Game Over trigger when depleted.
    /// Follows the Single Responsibility Principle: handles light energy state and lighting presentation.
    /// </summary>
    [RequireComponent(typeof(PlayerController))]
    public class LightEnergy : MonoBehaviour
    {
        [Header("Energy Settings")]
        [Tooltip("Maximum energy capacity.")]
        [SerializeField] private float maxEnergy = 100f;

        [Tooltip("Starting energy on level start.")]
        [SerializeField] private float initialEnergy = 100f;

        [Tooltip("Energy consumed per second passively.")]
        [SerializeField] private float drainRatePerSecond = 4.5f;

        [Tooltip("Threshold percentage (0-1) where light is considered critically low.")]
        [SerializeField] private float criticalThreshold = 0.25f;

        [Header("Light 2D References & Settings")]
        [Tooltip("The URP 2D Light component that illuminates the dark caves.")]
        [SerializeField] private Light2D fireflyLight;

        [Tooltip("Maximum outer radius when at full energy.")]
        [SerializeField] private float maxOuterRadius = 6.5f;

        [Tooltip("Minimum outer radius when near death.")]
        [SerializeField] private float minOuterRadius = 1.2f;

        [Tooltip("Maximum inner radius when at full energy.")]
        [SerializeField] private float maxInnerRadius = 2.0f;

        [Tooltip("Minimum inner radius when near death.")]
        [SerializeField] private float minInnerRadius = 0.3f;

        [Tooltip("Base light intensity.")]
        [SerializeField] private float baseIntensity = 1.1f;

        [Header("Color Dynamics")]
        [SerializeField] private Color fullEnergyColor = new Color(1.0f, 0.95f, 0.65f, 1f);
        [SerializeField] private Color criticalEnergyColor = new Color(0.95f, 0.35f, 0.2f, 1f);

        [Header("Low Light Tension / Pulse")]
        [SerializeField] private bool enableFlickerWhenLow = true;
        [SerializeField] private float flickerSpeed = 12f;
        [SerializeField] private float flickerAmplitude = 0.15f;

        // Public Events
        public event Action<float, float> OnEnergyChanged;
        public event Action<bool> OnCriticalStateChanged;
        public event Action OnEnergyDepleted;
        public event Action<float> OnEnergyRecharged;
        public event Action<float> OnDamaged;

        // State
        private float currentEnergy;
        private bool isDepleted;
        private bool isCritical;
        private PlayerController playerController;
        private float targetOuterRadius;
        private float targetInnerRadius;
        private float currentOuterRadius;
        private float currentInnerRadius;

        public float CurrentEnergy => currentEnergy;
        public float MaxEnergy => maxEnergy;
        public float EnergyNormalized => Mathf.Clamp01(currentEnergy / maxEnergy);
        public bool IsDepleted => isDepleted;
        public bool IsCritical => isCritical;

        private void Awake()
        {
            playerController = GetComponent<PlayerController>();

            if (fireflyLight == null)
            {
                fireflyLight = GetComponentInChildren<Light2D>();
            }

            currentEnergy = initialEnergy;
            currentOuterRadius = maxOuterRadius;
            currentInnerRadius = maxInnerRadius;
        }

        private void Start()
        {
            UpdateLightAppearance(instant: true);
            OnEnergyChanged?.Invoke(currentEnergy, maxEnergy);
        }

        private void Update()
        {
            if (isDepleted) return;

            // Passive drain over time
            ConsumeEnergy(drainRatePerSecond * Time.deltaTime);

            // Update light visuals smoothly
            UpdateLightAppearance(instant: false);
        }

        /// <summary>
        /// Consumes energy, updating status and triggering depletion if <= 0.
        /// </summary>
        public void ConsumeEnergy(float amount)
        {
            if (isDepleted || amount <= 0f) return;

            currentEnergy = Mathf.Max(0f, currentEnergy - amount);
            CheckCriticalState();
            OnEnergyChanged?.Invoke(currentEnergy, maxEnergy);

            if (currentEnergy <= 0f)
            {
                DieFromDarkness();
            }
        }

        /// <summary>
        /// Recharges energy, e.g. when collecting light crystals.
        /// </summary>
        public void AddEnergy(float amount)
        {
            if (isDepleted || amount <= 0f) return;

            currentEnergy = Mathf.Min(maxEnergy, currentEnergy + amount);
            CheckCriticalState();
            OnEnergyChanged?.Invoke(currentEnergy, maxEnergy);
            OnEnergyRecharged?.Invoke(amount);
        }

        /// <summary>
        /// Inflicts damage to energy (e.g. hitting hazards or bats).
        /// </summary>
        public void TakeDamage(float amount, Vector2? knockbackDir = null, float knockbackForce = 8f)
        {
            if (isDepleted || amount <= 0f) return;

            ConsumeEnergy(amount);
            OnDamaged?.Invoke(amount);

            if (knockbackDir.HasValue && playerController != null)
            {
                playerController.ApplyKnockback(knockbackDir.Value, knockbackForce);
            }
        }

        private void CheckCriticalState()
        {
            bool wasCrit = isCritical;
            isCritical = (currentEnergy / maxEnergy) <= criticalThreshold;

            if (wasCrit != isCritical)
            {
                OnCriticalStateChanged?.Invoke(isCritical);
            }
        }

        private void DieFromDarkness()
        {
            if (isDepleted) return;

            isDepleted = true;
            currentEnergy = 0f;

            if (playerController != null)
            {
                playerController.SetControlActive(false);
            }

            if (fireflyLight != null)
            {
                fireflyLight.pointLightOuterRadius = 0f;
                fireflyLight.pointLightInnerRadius = 0f;
                fireflyLight.intensity = 0f;
            }

            OnEnergyDepleted?.Invoke();
        }

        private void UpdateLightAppearance(bool instant)
        {
            if (fireflyLight == null) return;

            float norm = EnergyNormalized;
            targetOuterRadius = Mathf.Lerp(minOuterRadius, maxOuterRadius, norm);
            targetInnerRadius = Mathf.Lerp(minInnerRadius, maxInnerRadius, norm);

            // Pulse/flicker when in critical state
            float flicker = 0f;
            if (isCritical && enableFlickerWhenLow)
            {
                flicker = Mathf.Sin(Time.time * flickerSpeed) * flickerAmplitude;
            }

            if (instant)
            {
                currentOuterRadius = targetOuterRadius;
                currentInnerRadius = targetInnerRadius;
            }
            else
            {
                currentOuterRadius = Mathf.Lerp(currentOuterRadius, targetOuterRadius, Time.deltaTime * 6f);
                currentInnerRadius = Mathf.Lerp(currentInnerRadius, targetInnerRadius, Time.deltaTime * 6f);
            }

            fireflyLight.pointLightOuterRadius = Mathf.Max(0.2f, currentOuterRadius + flicker);
            fireflyLight.pointLightInnerRadius = Mathf.Max(0.1f, currentInnerRadius + (flicker * 0.5f));
            fireflyLight.color = Color.Lerp(criticalEnergyColor, fullEnergyColor, norm);
            fireflyLight.intensity = Mathf.Max(0.2f, baseIntensity + (flicker * 0.3f));
        }

        /// <summary>
        /// Resets the energy to full (e.g. on respawn).
        /// </summary>
        public void ResetEnergy()
        {
            isDepleted = false;
            currentEnergy = maxEnergy;
            isCritical = false;
            if (playerController != null)
            {
                playerController.SetControlActive(true);
            }
            UpdateLightAppearance(instant: true);
            OnEnergyChanged?.Invoke(currentEnergy, maxEnergy);
            OnCriticalStateChanged?.Invoke(false);
        }
    }
}
