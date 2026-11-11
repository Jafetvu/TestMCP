using UnityEngine;
using UnityEngine.UI;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Handles the pause menu toggle, timeScale freeze, and navigation buttons.
    /// Provides both uGUI support and instant OnGUI modal rendering.
    /// Follows the Single Responsibility Principle: handles pause state and UI interaction.
    /// </summary>
    public class PauseMenuUI : MonoBehaviour
    {
        [Header("UI References (Optional uGUI)")]
        [SerializeField] private GameObject pausePanel;
        [SerializeField] private Button resumeButton;
        [SerializeField] private Button restartButton;
        [SerializeField] private Button mainMenuButton;

        private bool isPaused;
        private GUIStyle modalStyle;
        private GUIStyle titleStyle;
        private GUIStyle buttonStyle;
        private Texture2D modalBgTex;
        private Texture2D btnNormalTex;
        private Texture2D btnHoverTex;

        public bool IsPaused => isPaused;

        private void Awake()
        {
            if (pausePanel != null)
                pausePanel.SetActive(false);

            if (resumeButton != null)
                resumeButton.onClick.AddListener(Resume);

            if (restartButton != null)
                restartButton.onClick.AddListener(RestartLevel);

            if (mainMenuButton != null)
                mainMenuButton.onClick.AddListener(ReturnToMainMenu);
        }

        private void Update()
        {
            if (GameInput.GetPauseDown())
            {
                if (isPaused)
                {
                    Resume();
                }
                else
                {
                    Pause();
                }
            }
        }

        public void Pause()
        {
            isPaused = true;
            Time.timeScale = 0f;

            if (pausePanel != null)
                pausePanel.SetActive(true);

            if (GameManager.Instance != null)
                GameManager.Instance.SetState(GameState.Paused);
        }

        public void Resume()
        {
            isPaused = false;
            Time.timeScale = 1f;

            if (pausePanel != null)
                pausePanel.SetActive(false);

            if (GameManager.Instance != null)
                GameManager.Instance.SetState(GameState.Playing);
        }

        public void RestartLevel()
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

            modalBgTex = MakeColorTex(2, 2, new Color(0.04f, 0.06f, 0.1f, 0.95f));
            btnNormalTex = MakeColorTex(2, 2, new Color(0.14f, 0.22f, 0.32f, 0.95f));
            btnHoverTex = MakeColorTex(2, 2, new Color(0.22f, 0.45f, 0.6f, 1f));

            modalStyle = new GUIStyle(GUI.skin.box);
            modalStyle.normal.background = modalBgTex;

            titleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 28,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            titleStyle.normal.textColor = new Color(1f, 0.92f, 0.5f);

            buttonStyle = new GUIStyle(GUI.skin.button)
            {
                fontSize = 16,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            buttonStyle.normal.background = btnNormalTex;
            buttonStyle.normal.textColor = Color.white;
            buttonStyle.hover.background = btnHoverTex;
            buttonStyle.hover.textColor = new Color(1f, 1f, 0.6f);
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
            if (!isPaused) return;

            // If uGUI panel is active and assigned, avoid overlapping
            if (pausePanel != null && pausePanel.activeSelf) return;

            InitStyles();

            float screenW = Screen.width;
            float screenH = Screen.height;

            // Fullscreen dark tint
            GUI.color = new Color(0, 0, 0, 0.65f);
            GUI.DrawTexture(new Rect(0, 0, screenW, screenH), modalBgTex);
            GUI.color = Color.white;

            // Centered Pause Modal Box
            float modalW = 340f;
            float modalH = 280f;
            float modalX = (screenW - modalW) * 0.5f;
            float modalY = (screenH - modalH) * 0.5f;

            GUI.Box(new Rect(modalX, modalY, modalW, modalH), "", modalStyle);

            GUI.Label(new Rect(modalX, modalY + 20f, modalW, 40f), "— PAUSA —", titleStyle);

            float btnW = 240f;
            float btnX = modalX + (modalW - btnW) * 0.5f;
            float btnY = modalY + 75f;

            if (GUI.Button(new Rect(btnX, btnY, btnW, 44f), "▶  CONTINUAR", buttonStyle))
            {
                Resume();
            }

            if (GUI.Button(new Rect(btnX, btnY + 54f, btnW, 44f), "↺  REINICIAR NIVEL", buttonStyle))
            {
                RestartLevel();
            }

            if (GUI.Button(new Rect(btnX, btnY + 108f, btnW, 44f), "⌂  MENÚ PRINCIPAL", buttonStyle))
            {
                ReturnToMainMenu();
            }
        }
    }
}
