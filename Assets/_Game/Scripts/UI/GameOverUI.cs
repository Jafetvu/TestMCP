using UnityEngine;
using UnityEngine.UI;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Displays the Game Over screen upon light extinction or falling into the abyss.
    /// Provides both uGUI support and instant OnGUI modal rendering.
    /// Follows the Single Responsibility Principle: handles failure feedback and restart actions.
    /// </summary>
    public class GameOverUI : MonoBehaviour
    {
        [Header("UI References (Optional uGUI)")]
        [SerializeField] private GameObject gameOverPanel;
        [SerializeField] private Text deathMessageText;
        [SerializeField] private Button retryButton;
        [SerializeField] private Button mainMenuButton;

        private bool isGameOver;
        private GUIStyle modalStyle;
        private GUIStyle titleStyle;
        private GUIStyle messageStyle;
        private GUIStyle hintStyle;
        private GUIStyle buttonStyle;
        private Texture2D modalBgTex;
        private Texture2D btnNormalTex;
        private Texture2D btnHoverTex;

        private void Awake()
        {
            if (gameOverPanel != null)
                gameOverPanel.SetActive(false);

            if (retryButton != null)
                retryButton.onClick.AddListener(RetryLevel);

            if (mainMenuButton != null)
                mainMenuButton.onClick.AddListener(ReturnToMainMenu);
        }

        private void Start()
        {
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnLevelFailed += ShowGameOver;
            }
        }

        private void OnDestroy()
        {
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.OnLevelFailed -= ShowGameOver;
            }
        }

        private void Update()
        {
            if (isGameOver && GameInput.GetRetryDown())
            {
                RetryLevel();
            }
        }

        public void ShowGameOver()
        {
            isGameOver = true;

            if (gameOverPanel != null)
                gameOverPanel.SetActive(true);

            if (deathMessageText != null)
            {
                deathMessageText.text = "La oscuridad ha consumido a la luciérnaga...";
            }
        }

        public void RetryLevel()
        {
            Time.timeScale = 1f;
            if (LevelManager.Instance != null)
            {
                LevelManager.Instance.RestartLevel();
            }
            else if (GameManager.Instance != null)
            {
                GameManager.Instance.RestartCurrentScene();
            }
        }

        public void ReturnToMainMenu()
        {
            Time.timeScale = 1f;
            if (GameManager.Instance != null)
            {
                GameManager.Instance.ReturnToMainMenu();
            }
            else if (LevelManager.Instance != null)
            {
                LevelManager.Instance.ReturnToMainMenu();
            }
        }

        private void InitStyles()
        {
            if (modalStyle != null) return;

            modalBgTex = MakeColorTex(2, 2, new Color(0.12f, 0.04f, 0.06f, 0.96f));
            btnNormalTex = MakeColorTex(2, 2, new Color(0.35f, 0.12f, 0.15f, 0.95f));
            btnHoverTex = MakeColorTex(2, 2, new Color(0.6f, 0.2f, 0.25f, 1f));

            modalStyle = new GUIStyle(GUI.skin.box);
            modalStyle.normal.background = modalBgTex;

            titleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 26,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            titleStyle.normal.textColor = new Color(1f, 0.3f, 0.25f);

            messageStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 15,
                fontStyle = FontStyle.Italic,
                alignment = TextAnchor.MiddleCenter
            };
            messageStyle.normal.textColor = new Color(0.9f, 0.85f, 0.85f);

            hintStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 13,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            hintStyle.normal.textColor = new Color(1f, 0.85f, 0.3f, 0.9f);

            buttonStyle = new GUIStyle(GUI.skin.button)
            {
                fontSize = 16,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            buttonStyle.normal.background = btnNormalTex;
            buttonStyle.normal.textColor = Color.white;
            buttonStyle.hover.background = btnHoverTex;
            buttonStyle.hover.textColor = new Color(1f, 1f, 0.7f);
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
            if (!isGameOver) return;

            // If uGUI panel is active and assigned, avoid overlapping
            if (gameOverPanel != null && gameOverPanel.activeSelf) return;

            InitStyles();

            float screenW = Screen.width;
            float screenH = Screen.height;

            // Fullscreen dark red tint
            GUI.color = new Color(0.1f, 0, 0, 0.75f);
            GUI.DrawTexture(new Rect(0, 0, screenW, screenH), modalBgTex);
            GUI.color = Color.white;

            // Centered Modal Box
            float modalW = 420f;
            float modalH = 290f;
            float modalX = (screenW - modalW) * 0.5f;
            float modalY = (screenH - modalH) * 0.5f;

            GUI.Box(new Rect(modalX, modalY, modalW, modalH), "", modalStyle);

            GUI.Label(new Rect(modalX, modalY + 18f, modalW, 35f), "¡LA LUZ SE HA EXTINGUIDO!", titleStyle);
            GUI.Label(new Rect(modalX, modalY + 54f, modalW, 25f), "La oscuridad de la cueva ha consumido a la luciérnaga...", messageStyle);
            GUI.Label(new Rect(modalX, modalY + 82f, modalW, 22f), "[ Pulsa R para Reintentar Rápido ]", hintStyle);

            float btnW = 260f;
            float btnX = modalX + (modalW - btnW) * 0.5f;
            float btnY = modalY + 120f;

            if (GUI.Button(new Rect(btnX, btnY, btnW, 46f), "↺  REINTENTAR NIVEL", buttonStyle))
            {
                RetryLevel();
            }

            if (GUI.Button(new Rect(btnX, btnY + 58f, btnW, 44f), "⌂  MENÚ PRINCIPAL", buttonStyle))
            {
                ReturnToMainMenu();
            }
        }
    }
}
