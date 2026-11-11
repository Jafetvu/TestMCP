using UnityEngine;
using UnityEngine.UI;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Controls the title screen, instructions overlay, and scene dispatching to Level 1.
    /// Follows the Single Responsibility Principle: manages Main Menu interactions.
    /// </summary>
    public class MainMenuUI : MonoBehaviour
    {
        [Header("Menu Buttons")]
        [SerializeField] private Button playButton;
        [SerializeField] private Button instructionsButton;
        [SerializeField] private Button quitButton;

        [Header("Instructions Modal")]
        [SerializeField] private GameObject instructionsPanel;
        [SerializeField] private Button closeInstructionsButton;

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
                UnityEngine.SceneManagement.SceneManager.LoadScene("Level1");
            }
        }

        public void OpenInstructions()
        {
            if (instructionsPanel != null)
                instructionsPanel.SetActive(true);
        }

        public void CloseInstructions()
        {
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
    }
}
