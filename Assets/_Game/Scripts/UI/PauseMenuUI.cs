using UnityEngine;
using UnityEngine.UI;
using Firefly.Core;

namespace Firefly.UI
{
    /// <summary>
    /// Handles the pause menu toggle, timeScale freeze, and navigation buttons.
    /// Follows the Single Responsibility Principle: handles pause state and UI interaction.
    /// </summary>
    public class PauseMenuUI : MonoBehaviour
    {
        [Header("UI References")]
        [SerializeField] private GameObject pausePanel;
        [SerializeField] private Button resumeButton;
        [SerializeField] private Button restartButton;
        [SerializeField] private Button mainMenuButton;

        private bool isPaused;

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
    }
}
