using UnityEngine;
using UnityEngine.UI;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Displays victory statistics and celebration at the completion of Level 3.
    /// Follows the Single Responsibility Principle: handles victory presentation and restart actions.
    /// </summary>
    public class VictoryUI : MonoBehaviour
    {
        [Header("UI Text References")]
        [SerializeField] private Text victoryTitleText;
        [SerializeField] private Text congratulationMessageText;
        [SerializeField] private Text totalCrystalsText;
        [SerializeField] private Text totalTimeText;

        [Header("Buttons")]
        [SerializeField] private Button playAgainButton;
        [SerializeField] private Button mainMenuButton;

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

            int crystals = 0;
            float time = 0f;

            if (GameManager.Instance != null)
            {
                crystals = GameManager.Instance.TotalCrystalsCollected;
                time = GameManager.Instance.SessionElapsedTime;
                GameManager.Instance.SetState(GameState.Victory);
            }

            if (totalCrystalsText != null)
            {
                totalCrystalsText.text = $"Cristales de Luz Reunidos: {crystals}";
            }

            if (totalTimeText != null)
            {
                int minutes = Mathf.FloorToInt(time / 60f);
                int seconds = Mathf.FloorToInt(time % 60f);
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
                UnityEngine.SceneManagement.SceneManager.LoadScene("Level1");
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
                UnityEngine.SceneManagement.SceneManager.LoadScene("MainMenu");
            }
        }
    }
}
