using System;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace Firefly.Core
{
    public enum GameState
    {
        MainMenu,
        Playing,
        Paused,
        GameOver,
        LevelComplete,
        Victory
    }

    /// <summary>
    /// Persistent global manager that survives scene transitions.
    /// Manages high-level state, session statistics (total crystals, run timer),
    /// and scene switching.
    /// Follows the Single Responsibility Principle: coordinates game-wide persistence and states.
    /// </summary>
    public class GameManager : MonoBehaviour
    {
        public static GameManager Instance { get; private set; }

        [Header("Global Session State")]
        [SerializeField] private GameState currentState = GameState.Playing;
        [SerializeField] private int totalCrystalsCollected = 0;
        [SerializeField] private float sessionElapsedTime = 0f;

        public GameState CurrentState => currentState;
        public int TotalCrystalsCollected => totalCrystalsCollected;
        public float SessionElapsedTime => sessionElapsedTime;

        public static event Action<GameState> OnGameStateChanged;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }

            Instance = this;
            DontDestroyOnLoad(gameObject);
        }

        private void Update()
        {
            if (currentState == GameState.Playing)
            {
                sessionElapsedTime += Time.deltaTime;
            }
        }

        public void SetState(GameState newState)
        {
            if (currentState == newState) return;

            currentState = newState;
            OnGameStateChanged?.Invoke(newState);
        }

        public void AddTotalCrystals(int amount)
        {
            totalCrystalsCollected += amount;
        }

        public void ResetGameSession()
        {
            totalCrystalsCollected = 0;
            sessionElapsedTime = 0f;
            SetState(GameState.Playing);
        }

        public void StartNewGame()
        {
            ResetGameSession();
            Time.timeScale = 1f;
            SceneManager.LoadScene("Level1");
        }

        public void RestartCurrentScene()
        {
            Time.timeScale = 1f;
            SetState(GameState.Playing);
            Scene current = SceneManager.GetActiveScene();
            SceneManager.LoadScene(current.buildIndex);
        }

        public void LoadScene(string sceneName)
        {
            Time.timeScale = 1f;
            SceneManager.LoadScene(sceneName);
        }

        public void ReturnToMainMenu()
        {
            Time.timeScale = 1f;
            SetState(GameState.MainMenu);
            SceneManager.LoadScene("MainMenu");
        }

        public void QuitGame()
        {
#if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
#else
            Application.Quit();
#endif
        }
    }
}
