using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Controls the title screen, instructions overlay, and scene dispatching to Level 1.
    /// Provides both uGUI support and an instant, foolproof OnGUI interface that renders
    /// immediately without missing-reference dependencies.
    /// </summary>
    public class MainMenuUI : MonoBehaviour
    {
        [Header("Menu Buttons (Optional uGUI)")]
        [SerializeField] private Button playButton;
        [SerializeField] private Button instructionsButton;
        [SerializeField] private Button quitButton;

        [Header("Instructions Modal (Optional uGUI)")]
        [SerializeField] private GameObject instructionsPanel;
        [SerializeField] private Button closeInstructionsButton;

        private bool showInstructionsModal = false;
        private GUIStyle titleStyle;
        private GUIStyle subtitleStyle;
        private GUIStyle buttonStyle;
        private GUIStyle modalBoxStyle;
        private GUIStyle headerStyle;
        private GUIStyle bodyStyle;
        private Texture2D darkBoxTex;
        private Texture2D buttonNormalTex;
        private Texture2D buttonHoverTex;
        private Texture2D modalBgTex;

        private void Awake()
        {
            if (playButton != null)
                playButton.onClick.AddListener(PlayGame);

            if (instructionsButton != null)
                instructionsButton.onClick.AddListener(OpenInstructions);

            if (closeInstructionsButton != null)
                closeInstructionsButton.onClick.AddListener(CloseInstructions);

            if (quitButton != null)
                quitButton.onClick.AddListener(QuitGame);

            if (instructionsPanel != null)
                instructionsPanel.SetActive(false);
        }

        private void Start()
        {
            Time.timeScale = 1f;
            if (GameManager.Instance != null)
            {
                GameManager.Instance.SetState(GameState.MainMenu);
            }
        }

        public void PlayGame()
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

        public void OpenInstructions()
        {
            showInstructionsModal = true;
            if (instructionsPanel != null)
                instructionsPanel.SetActive(true);
        }

        public void CloseInstructions()
        {
            showInstructionsModal = false;
            if (instructionsPanel != null)
                instructionsPanel.SetActive(false);
        }

        public void QuitGame()
        {
            if (GameManager.Instance != null)
            {
                GameManager.Instance.QuitGame();
            }
            else
            {
#if UNITY_EDITOR
                UnityEditor.EditorApplication.isPlaying = false;
#else
                Application.Quit();
#endif
            }
        }

        private void InitStyles()
        {
            if (titleStyle != null) return;

            darkBoxTex = MakeColorTex(2, 2, new Color(0.06f, 0.08f, 0.12f, 0.88f));
            buttonNormalTex = MakeColorTex(2, 2, new Color(0.12f, 0.22f, 0.32f, 0.95f));
            buttonHoverTex = MakeColorTex(2, 2, new Color(0.22f, 0.55f, 0.65f, 1f));
            modalBgTex = MakeColorTex(2, 2, new Color(0.04f, 0.05f, 0.08f, 0.96f));

            titleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 42,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            titleStyle.normal.textColor = new Color(1.0f, 0.92f, 0.45f); // Golden yellow

            subtitleStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 18,
                fontStyle = FontStyle.Italic,
                alignment = TextAnchor.MiddleCenter
            };
            subtitleStyle.normal.textColor = new Color(0.5f, 0.85f, 0.95f); // Soft cyan

            buttonStyle = new GUIStyle(GUI.skin.button)
            {
                fontSize = 18,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            buttonStyle.normal.background = buttonNormalTex;
            buttonStyle.normal.textColor = Color.white;
            buttonStyle.hover.background = buttonHoverTex;
            buttonStyle.hover.textColor = new Color(1f, 1f, 0.6f);

            modalBoxStyle = new GUIStyle(GUI.skin.box);
            modalBoxStyle.normal.background = modalBgTex;

            headerStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 24,
                fontStyle = FontStyle.Bold,
                alignment = TextAnchor.MiddleCenter
            };
            headerStyle.normal.textColor = new Color(0.2f, 0.95f, 1f);

            bodyStyle = new GUIStyle(GUI.skin.label)
            {
                fontSize = 15,
                alignment = TextAnchor.UpperLeft,
                wordWrap = true
            };
            bodyStyle.normal.textColor = new Color(0.9f, 0.9f, 0.95f);
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
            // If uGUI panel is active and assigned, avoid overlapping
            if (instructionsPanel != null && instructionsPanel.activeSelf) return;

            InitStyles();

            float screenW = Screen.width;
            float screenH = Screen.height;

            if (showInstructionsModal)
            {
                DrawInstructionsModal(screenW, screenH);
                return;
            }

            // Title Header
            float titleWidth = 500f;
            float titleX = (screenW - titleWidth) * 0.5f;
            float titleY = screenH * 0.18f;

            GUI.Label(new Rect(titleX, titleY, titleWidth, 55f), "LUCIÉRNAGA", titleStyle);
            GUI.Label(new Rect(titleX, titleY + 52f, titleWidth, 30f), "— Enciende la oscuridad —", subtitleStyle);

            // Menu Buttons Container
            float menuWidth = 320f;
            float menuX = (screenW - menuWidth) * 0.5f;
            float menuY = titleY + 115f;

            if (GUI.Button(new Rect(menuX, menuY, menuWidth, 52f), "▶  INICIAR AVENTURA", buttonStyle))
            {
                PlayGame();
            }

            if (GUI.Button(new Rect(menuX, menuY + 64f, menuWidth, 48f), "📖  CÓMO JUGAR", buttonStyle))
            {
                OpenInstructions();
            }

            if (GUI.Button(new Rect(menuX, menuY + 124f, menuWidth, 44f), "❌  SALIR", buttonStyle))
            {
                QuitGame();
            }

            // Version info footer
            GUIStyle footerStyle = new GUIStyle(GUI.skin.label) { fontSize = 12, alignment = TextAnchor.MiddleCenter };
            footerStyle.normal.textColor = new Color(0.6f, 0.65f, 0.75f, 0.8f);
            GUI.Label(new Rect(0, screenH - 35f, screenW, 25f), "Unity 6 (6000.6.0f1) • URP 2D • Hecho con C#", footerStyle);
        }

        private void DrawInstructionsModal(float screenW, float screenH)
        {
            float modalW = Mathf.Min(600f, screenW - 40f);
            float modalH = Mathf.Min(480f, screenH - 40f);
            float modalX = (screenW - modalW) * 0.5f;
            float modalY = (screenH - modalH) * 0.5f;

            GUI.Box(new Rect(modalX, modalY, modalW, modalH), "", modalBoxStyle);

            float pad = 25f;
            float contentX = modalX + pad;
            float contentW = modalW - (pad * 2f);

            GUI.Label(new Rect(contentX, modalY + 18f, contentW, 35f), "GUÍA DE SUPERVIVENCIA", headerStyle);

            string instructions =
                "<b>1. TU LUZ ES TU VIDA:</b>\n" +
                "La cueva está inmersa en la oscuridad. Tu luz se gasta cada segundo. Si se apaga por completo, pierdes.\n\n" +
                "<b>2. RECOLECTA CRISTALES DE LUZ:</b>\n" +
                "Los cristales ancestrales recargan tu energía de luz y desbloquean el portal de salida al final del nivel.\n\n" +
                "<b>3. CONTROLES:</b>\n" +
                "• <b>A / D</b> o <b>Flechas:</b> Moverse horizontalmente.\n" +
                "• <b>Espacio</b> o <b>W:</b> Saltar y aletear (hasta 2 aleteos en el aire).\n" +
                "• <b>Mantener Espacio:</b> Planear suavemente.\n" +
                "• <b>Escape</b> o <b>P:</b> Pausar la partida.\n" +
                "• <b>R:</b> Reintentar nivel tras perder.\n\n" +
                "<b>4. PELIGROS:</b>\n" +
                "Evita los pinchos afilados y a los murciélagos con ojos rojos que patrullan la oscuridad.";

            GUI.Label(new Rect(contentX, modalY + 60f, contentW, modalH - 130f), instructions, bodyStyle);

            if (GUI.Button(new Rect(modalX + (modalW - 180f) * 0.5f, modalY + modalH - 55f, 180f, 40f), "VOLVER", buttonStyle))
            {
                CloseInstructions();
            }
        }
    }
}
