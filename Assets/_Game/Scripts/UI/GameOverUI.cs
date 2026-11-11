using UnityEngine;
using UnityEngine.UI;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Displays the Game Over screen upon light extinction or falling into the abyss.
    /// Follows the Single Responsibility Principle: handles failure feedback and restart actions.
    /// </summary>
    public class GameOverUI : MonoBehaviour
    {
        [Header("UI References")]
        [SerializeField] private GameObject gameOverPanel;
        [SerializeField] private Text deathMessageText;
        [SerializeField] private Button retryButton;
        [SerializeField] private Button mainMenuButton;

        private bool isGameOver;

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
    }
}
