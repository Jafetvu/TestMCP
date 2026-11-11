using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Displays victory statistics and celebration at the completion of Level 3.
    /// Provides both uGUI support and instant OnGUI modal rendering.
    /// Follows the Single Responsibility Principle: handles victory presentation and restart actions.
    /// </summary>
    public class VictoryUI : MonoBehaviour
    {
        [Header("UI Text References (Optional uGUI)")]
        [SerializeField] private Text victoryTitleText;
        [SerializeField] private Text congratulationMessageText;
        [SerializeField] private Text totalCrystalsText;
        [SerializeField] private Text totalTimeText;

        [Header("Buttons (Optional uGUI)")]
        [SerializeField] private Button playAgainButton;
        [SerializeField] private Button mainMenuButton;

        private int crystalsCount;
        private float elapsedTime;
        private GUIStyle modalStyle;
        private GUIStyle titleStyle;
        private GUIStyle subtitleStyle;
        private GUIStyle statStyle;
        private GUIStyle buttonStyle;
        private Texture2D modalBgTex;
        private Texture2D btnNormalTex;
        private Texture2D btnHoverTex;

        private void Awake()
        {
            if (playAgainButton != null)
                playAgainButton.onClick.AddListener(PlayAgain);

            if (mainMenuButton != null)
                mainMenuButton.onClick.AddListener(ReturnToMainMenu);
        }

        private void Start()
        {
            Time.timeScale = 1f;

            if (GameManager.Instance != null)
            {
                crystalsCount = GameManager.Instance.TotalCrystalsCollected;
                elapsedTime = GameManager.Instance.SessionElapsedTime;
                GameManager.Instance.SetState(GameState.Victory);
            }

            if (totalCrystalsText != null)
            {
                totalCrystalsText.text = $"Cristales de Luz Reunidos: {crystalsCount}";
            }

            if (totalTimeText != null)
            {
                int minutes = Mathf.FloorToInt(elapsedTime / 60f);
                int seconds = Mathf.FloorToInt(elapsedTime % 60f);
                totalTimeText.text = $"Tiempo de Escape: {minutes:00}:{seconds:00}";
            }
        }

        public void PlayAgain()
        {
            if (GameManager.Instance != null)
            {
                GameManager.Instance.StartNewGame();
            }
            else
            {
                SceneManager.LoadScene("Level1");
            }
        }

        public void ReturnToMainMenu()
        {
            if (GameManager.Instance != null)
            {
                GameManager.Instance.ReturnToMainMenu();
            }
            else
            {
                SceneManager.LoadScene("MainMenu");
            }
        }

        private void InitStyles()
        {
            if (modalStyle != null) return;

            modalBgTex = MakeColorTex(2, 2, new Color(0.04f, 0.08f, 0.12f, 0.96f));
            btnNormalTex = MakeColorTex(2, 2, new Color(0.12f, 0.35f, 0.38f, 0.95f));
            btnHoverTex = MakeColorTex(2, 2, new Color(0.2f, 0.65f, 0.65f, 1f));

            modalStyle = new GUIStyle(GUI.skin.box);
            modalStyle.normal.background = modalBgTex;

            titleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 38,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            titleStyle.normal.textColor = new Color(1f, 0.9f, 0.35f); // Brilliant Gold

            subtitleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 16,
                fontStyle = FontStyle.Italic,
                alignment = TextAnchor.MiddleCenter,
                wordWrap = true
            };
            subtitleStyle.normal.textColor = new Color(0.7f, 0.95f, 1f);

            statStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 18,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            statStyle.normal.textColor = Color.white;

            buttonStyle = new GUIStyle(GUI.skin.button)
            {
                fontSize = 17,
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
            // If uGUI is assigned, avoid overlapping
            if (playAgainButton != null) return;

            InitStyles();

            float screenW = Screen.width;
            float screenH = Screen.height;

            float modalW = Mathf.Min(520f, screenW - 40f);
            float modalH = Mathf.Min(380f, screenH - 40f);
            float modalX = (screenW - modalW) * 0.5f;
            float modalY = (screenH - modalH) * 0.5f;

            GUI.Box(new Rect(modalX, modalY, modalW, modalH), "", modalStyle);

            GUI.Label(new Rect(modalX, modalY + 22f, modalW, 45f), "✨ ¡VICTORIA! ✨", titleStyle);
            GUI.Label(new Rect(modalX + 20f, modalY + 70f, modalW - 40f, 45f), "Has guiado a la luciérnaga hacia la luz y escapado de las profundidades de la caverna.", subtitleStyle);

            int min = Mathf.FloorToInt(elapsedTime / 60f);
            int sec = Mathf.FloorToInt(elapsedTime % 60f);
            string timeStr = $"{min:00}:{sec:00}";

            GUI.Label(new Rect(modalX, modalY + 128f, modalW, 28f), $"💎 Cristales de Luz Reunidos:  <b>{crystalsCount}</b>", statStyle);
            GUI.Label(new Rect(modalX, modalY + 160f, modalW, 28f), $"⏱️ Tiempo de Escape:  <b>{timeStr}</b>", statStyle);

            float btnW = 260f;
            float btnX = modalX + (modalW - btnW) * 0.5f;
            float btnY = modalY + 220f;

            if (GUI.Button(new Rect(btnX, btnY, btnW, 48f), "▶  JUGAR DE NUEVO", buttonStyle))
            {
                PlayAgain();
            }

            if (GUI.Button(new Rect(btnX, btnY + 58f, btnW, 44f), "⌂  MENÚ PRINCIPAL", buttonStyle))
            {
                ReturnToMainMenu();
            }
        }
    }
}
