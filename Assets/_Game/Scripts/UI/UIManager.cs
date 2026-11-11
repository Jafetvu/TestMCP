using UnityEngine;
using UnityEngine.UI;
using Firefly.Light;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Coordinates the in-game HUD: Light energy bar, crystal counter,
    /// level title, and critical energy warning effects.
    /// Follows the Single Responsibility Principle: handles in-game HUD display logic.
    /// </summary>
    public class UIManager : MonoBehaviour
    {
        public static UIManager Instance { get; private set; }

        [Header("Light Bar")]
        [SerializeField] private Image lightBarFill;
        [SerializeField] private Text lightPercentageText;
        [SerializeField] private Color fullEnergyColor = new Color(1.0f, 0.88f, 0.25f, 1f);
        [SerializeField] private Color criticalEnergyColor = new Color(0.95f, 0.25f, 0.2f, 1f);

        [Header("Crystals HUD")]
        [SerializeField] private Text crystalsCounterText;
        [SerializeField] private Image crystalIcon;

        [Header("Level Info")]
        [SerializeField] private Text levelTitleText;

        [Header("Low Light Warning Effect")]
        [SerializeField] private Image criticalVignette;
        [SerializeField] private float pulseSpeed = 6f;

        private LightEnergy playerLight;
        private bool isCritical;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }
            Instance = this;
        }

        private void Start()
        {
            HookPlayer();
            HookLevelManager();
        }

        private void OnDestroy()
        {
            if (Instance == this)
            {
                Instance = null;
            }

            if (playerLight != null)
            {
                playerLight.OnEnergyChanged -= UpdateLightBar;
                playerLight.OnCriticalStateChanged -= SetCriticalWarning;
            }

            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnCrystalCountChanged -= UpdateCrystalsCount;
            }
        }

        private void Update()
        {
            if (playerLight == null)
            {
                HookPlayer();
            }

            // Pulsating warning vignette when energy is critical
            if (isCritical && criticalVignette != null)
            {
                float alpha = (Mathf.Sin(Time.time * pulseSpeed) + 1f) * 0.5f * 0.4f;
                Color col = criticalVignette.color;
                col.a = alpha;
                criticalVignette.color = col;
            }
            else if (criticalVignette != null && criticalVignette.color.a > 0f)
            {
                Color col = criticalVignette.color;
                col.a = 0f;
                criticalVignette.color = col;
            }
        }

        private void HookPlayer()
        {
            GameObject player = GameObject.FindWithTag("Player");
            if (player != null)
            {
                playerLight = player.GetComponent<LightEnergy>();
                if (playerLight != null)
                {
                    playerLight.OnEnergyChanged += UpdateLightBar;
                    playerLight.OnCriticalStateChanged += SetCriticalWarning;
                    UpdateLightBar(playerLight.CurrentEnergy, playerLight.MaxEnergy);
                }
            }
        }

        private void HookLevelManager()
        {
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnCrystalCountChanged += UpdateCrystalsCount;
                UpdateCrystalsCount(LevelManager.Instance.CollectedCrystals, LevelManager.Instance.TotalCrystals);

                if (levelTitleText != null)
                {
                    levelTitleText.text = LevelManager.Instance.LevelTitle;
                }
            }
        }

        public void UpdateLightBar(float current, float max)
        {
            float norm = Mathf.Clamp01(current / max);

            if (lightBarFill != null)
            {
                lightBarFill.fillAmount = norm;
                lightBarFill.color = Color.Lerp(criticalEnergyColor, fullEnergyColor, norm);
            }

            if (lightPercentageText != null)
            {
                lightPercentageText.text = $"{Mathf.CeilToInt(norm * 100f)}%";
            }
        }

        public void UpdateCrystalsCount(int collected, int total)
        {
            if (crystalsCounterText != null)
            {
                crystalsCounterText.text = $"{collected} / {total}";
            }
        }

        public void SetCriticalWarning(bool critical)
        {
            isCritical = critical;
        }
    }
}
