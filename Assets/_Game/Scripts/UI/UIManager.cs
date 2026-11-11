using UnityEngine;
using UnityEngine.UI;
using Firefly.Light;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Coordinates the in-game HUD: Light energy bar, crystal counter,
    /// level title, and critical energy warning effects.
    /// Provides both uGUI support and an instant, foolproof OnGUI fallback.
    /// Follows the Single Responsibility Principle: handles in-game HUD display logic.
    /// </summary>
    public class UIManager : MonoBehaviour
    {
        public static UIManager Instance { get; private set; }

        [Header("Light Bar (Optional uGUI)")]
        [SerializeField] private Image lightBarFill;
        [SerializeField] private Text lightPercentageText;
        [SerializeField] private Color fullEnergyColor = new Color(1.0f, 0.88f, 0.25f, 1f);
        [SerializeField] private Color criticalEnergyColor = new Color(0.95f, 0.25f, 0.2f, 1f);

        [Header("Crystals HUD (Optional uGUI)")]
        [SerializeField] private Text crystalsCounterText;
        [SerializeField] private Image crystalIcon;

        [Header("Level Info (Optional uGUI)")]
        [SerializeField] private Text levelTitleText;

        [Header("Low Light Warning Effect (Optional uGUI)")]
        [SerializeField] private Image criticalVignette;
        [SerializeField] private float pulseSpeed = 6f;

        private LightEnergy playerLight;
        private bool isCritical;
        private float currentEnergy = 100f;
        private float maxEnergy = 100f;
        private int collectedCrystals;
        private int totalCrystals;
        private string levelTitle = "";

        // OnGUI textures and styles
        private Texture2D barBgTex;
        private Texture2D barFillTex;
        private GUIStyle hudLabelStyle;
        private GUIStyle hudTitleStyle;
        private GUIStyle warningStyle;

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

            // Pulsating warning vignette when energy is critical (uGUI)
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
                levelTitle = LevelManager.Instance.LevelTitle;

                if (levelTitleText != null)
                {
                    levelTitleText.text = LevelManager.Instance.LevelTitle;
                }
            }
        }

        public void UpdateLightBar(float current, float max)
        {
            currentEnergy = current;
            maxEnergy = max;
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
            collectedCrystals = collected;
            totalCrystals = total;

            if (crystalsCounterText != null)
            {
                crystalsCounterText.text = $"{collected} / {total}";
            }
        }

        public void SetCriticalWarning(bool critical)
        {
            isCritical = critical;
        }

        private void InitGUIStyles()
        {
            if (hudLabelStyle != null) return;

            barBgTex = MakeColorTex(2, 2, new Color(0.08f, 0.1f, 0.14f, 0.85f));
            barFillTex = MakeColorTex(2, 2, Color.white);

            hudLabelStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 15,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleLeft
            };
            hudLabelStyle.normal.textColor = Color.white;

            hudTitleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 16,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleRight
            };
            hudTitleStyle.normal.textColor = new Color(0.7f, 0.85f, 1f, 0.9f);

            warningStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 16,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            warningStyle.normal.textColor = new Color(1f, 0.25f, 0.2f);
        }

        private Texture2D MakeColorTex(int width, int height, Color col)
        {
            Color[] pix = new Color[width * height];
            for (int i = 0; i < pix.Length; i++) pix[i] = col;
            Texture2D tex = new Texture2D(width, height);
            tex.SetPixels(pix);
            tex.Apply();
            return tex;
        }

        private void OnGUI()
        {
            InitGUIStyles();

            float norm = Mathf.Clamp01(currentEnergy / maxEnergy);
            float screenW = Screen.width;

            // 1. Light Bar HUD (Top Left)
            float startX = 20f;
            float startY = 16f;
            float barW = 200f;
            float barH = 22f;

            // Background container
            GUI.DrawTexture(new Rect(startX - 6, startY - 6, barW + 12, barH + 12), barBgTex);

            // Energy Bar Fill
            Color barCol = Color.Lerp(criticalEnergyColor, fullEnergyColor, norm);
            GUI.color = barCol;
            GUI.DrawTexture(new Rect(startX, startY, barW * norm, barH), barFillTex);
            GUI.color = Color.white;

            // Text inside bar
            GUI.Label(new Rect(startX + 10, startY - 1, barW, barH), $"LUZ: {Mathf.CeilToInt(norm * 100f)}%", hudLabelStyle);

            // 2. Crystal Counter HUD (Below Light Bar)
            string crystalText = $"💎 Cristales: {collectedCrystals} / {totalCrystals}";
            if (collectedCrystals >= totalCrystals && totalCrystals > 0)
            {
                crystalText += "  ✓ [¡PORTAL ABIERTO!]";
            }
            GUI.Label(new Rect(startX, startY + barH + 10, 300f, 25f), crystalText, hudLabelStyle);

            // 3. Level Title (Top Right)
            if (!string.IsNullOrEmpty(levelTitle))
            {
                GUI.Label(new Rect(screenW - 320f, startY, 300f, 25f), levelTitle, hudTitleStyle);
            }

            // 4. Critical Warning Pulse Text
            if (isCritical)
            {
                float flash = (Mathf.Sin(Time.time * 8f) + 1f) * 0.5f;
                if (flash > 0.4f)
                {
                    GUI.Label(new Rect((screenW - 300f) * 0.5f, startY + 45f, 300f, 30f), "⚠️ ¡ENERGÍA DE LUZ CRÍTICA! ⚠️", warningStyle);
                }
            }
        }
    }
}
