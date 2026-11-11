using System;
using UnityEngine;
using UnityEngine.Rendering.Universal;
using Firefly.Core;

namespace Firefly.Environment
{
    /// <summary>
    /// The exit portal / altar that unlocks once all crystals in the level are gathered.
    /// Follows the Single Responsibility Principle: handles exit portal activation and exit triggering.
    /// </summary>
    [RequireComponent(typeof(Collider2D))]
    public class LevelExit : MonoBehaviour
    {
        [Header("Visuals & Lighting")]
        [SerializeField] private SpriteRenderer portalRenderer;
        [SerializeField] private Light2D portalLight;
        [SerializeField] private Color lockedColor = new Color(0.4f, 0.45f, 0.5f, 0.6f);
        [SerializeField] private Color unlockedColor = new Color(0.2f, 0.95f, 1f, 1f);
        [SerializeField] private float lockedLightRadius = 1.5f;
        [SerializeField] private float unlockedLightRadius = 5.0f;
        [SerializeField] private float unlockedLightIntensity = 1.6f;

        [Header("Activation FX")]
        [SerializeField] private ParticleSystem unlockParticles;

        private bool isUnlocked;
        private bool isTriggered;
        private Collider2D exitCollider;

        public bool IsUnlocked => isUnlocked;

        public static event Action OnPortalUnlocked;
        public static event Action OnPortalEntered;

        private void Awake()
        {
            exitCollider = GetComponent<Collider2D>();
            exitCollider.isTrigger = true;

            if (portalRenderer == null)
                portalRenderer = GetComponentInChildren<SpriteRenderer>();

            if (portalLight == null)
                portalLight = GetComponentInChildren<Light2D>();
        }

        private void Start()
        {
            SetLockedVisuals();

            // Hook up with LevelManager
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnAllCrystalsCollected += Unlock;
            }
        }

        private void OnDestroy()
        {
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnAllCrystalsCollected -= Unlock;
            }
        }

        public void Unlock()
        {
            if (isUnlocked) return;

            isUnlocked = true;

            if (portalRenderer != null)
            {
                portalRenderer.color = unlockedColor;
            }

            if (portalLight != null)
            {
                portalLight.color = unlockedColor;
                portalLight.pointLightOuterRadius = unlockedLightRadius;
                portalLight.intensity = unlockedLightIntensity;
            }

            if (unlockParticles != null)
            {
                unlockParticles.Play();
            }

            OnPortalUnlocked?.Invoke();
        }

        private void SetLockedVisuals()
        {
            isUnlocked = false;

            if (portalRenderer != null)
            {
                portalRenderer.color = lockedColor;
            }

            if (portalLight != null)
            {
                portalLight.color = lockedColor;
                portalLight.pointLightOuterRadius = lockedLightRadius;
                portalLight.intensity = 0.5f;
            }
        }

        private void OnTriggerEnter2D(Collider2D other)
        {
            if (!isUnlocked || isTriggered) return;

            if (other.CompareTag("Player") || other.GetComponent<Firefly.Player.PlayerController>() != null)
            {
                isTriggered = true;
                OnPortalEntered?.Invoke();

                if (LevelManager.Instance != null)
                {
                    LevelManager.Instance.CompleteLevel();
                }
            }
        }
    }
}
