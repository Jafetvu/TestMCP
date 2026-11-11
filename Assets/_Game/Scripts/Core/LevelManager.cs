using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using Firefly.Environment;
using Firefly.Light;
using Firefly.Player;
using Firefly.Audio;

namespace Firefly.Core
{
    /// <summary>
    /// Per-level manager that tracks crystal objectives, player lifecycle,
    /// level completion and transitions.
    /// Follows the Single Responsibility Principle: coordinates level-specific gameplay flow.
    /// </summary>
    public class LevelManager : MonoBehaviour
    {
        public static LevelManager Instance { get; private set; }

        [Header("Level Information")]
        [SerializeField] private int levelNumber = 1;
        [SerializeField] private string levelTitle = "Nivel 1 - Cueva Umbría";
        [SerializeField] private string nextSceneName = "Level2";

        [Header("Player References")]
        [SerializeField] private Transform playerSpawnPoint;
        [SerializeField] private GameObject playerPrefab;

        [Header("Transitions")]
        [SerializeField] private float completionDelay = 1.2f;
        [SerializeField] private float gameOverDelay = 1.0f;

        // Events
        public event Action<int, int> OnCrystalCountChanged;
        public event Action OnAllCrystalsCollected;
        public event Action OnLevelCompleted;
        public event Action OnLevelFailed;

        // Crystal tracking
        private readonly List<CollectibleCrystal> registeredCrystals = new List<CollectibleCrystal>();
        private int collectedCrystalsCount;
        private int totalCrystalsCount;
        private bool isLevelCompleted;
        private bool isLevelFailed;
        private LightEnergy playerLightEnergy;

        public int LevelNumber => levelNumber;
        public string LevelTitle => levelTitle;
        public int CollectedCrystals => collectedCrystalsCount;
        public int TotalCrystals => totalCrystalsCount;
        public bool IsLevelCompleted => isLevelCompleted;
        public bool IsLevelFailed => isLevelFailed;

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
            Time.timeScale = 1f;

            // Find existing player or instantiate at spawn point
            FindOrSpawnPlayer();

            // Find any crystals already in scene
            CollectibleCrystal[] crystals = FindObjectsByType<CollectibleCrystal>(FindObjectsSortMode.None);
            foreach (var c in crystals)
            {
                RegisterCrystal(c);
            }

            OnCrystalCountChanged?.Invoke(collectedCrystalsCount, totalCrystalsCount);
        }

        private void OnDestroy()
        {
            if (Instance == this)
            {
                Instance = null;
            }

            if (playerLightEnergy != null)
            {
                playerLightEnergy.OnEnergyDepleted -= HandlePlayerDeath;
            }
        }

        private void FindOrSpawnPlayer()
        {
            GameObject player = GameObject.FindWithTag("Player");

            if (player == null && playerPrefab != null && playerSpawnPoint != null)
            {
                player = Instantiate(playerPrefab, playerSpawnPoint.position, Quaternion.identity);
            }
            else if (player != null && playerSpawnPoint != null)
            {
                player.transform.position = playerSpawnPoint.position;
            }

            if (player != null)
            {
                playerLightEnergy = player.GetComponent<LightEnergy>();
                PlayerController controller = player.GetComponent<PlayerController>();

                if (playerLightEnergy != null)
                {
                    playerLightEnergy.OnEnergyDepleted += HandlePlayerDeath;
                    playerLightEnergy.OnDamaged += (dmg) =>
                    {
                        if (CameraFollow2D.Instance != null)
                        {
                            CameraFollow2D.Instance.TriggerShake(0.2f, 0.22f);
                        }
                    };
                }

                if (AudioManager.Instance != null)
                {
                    AudioManager.Instance.BindPlayer(controller, playerLightEnergy);
                }
            }
        }

        public void RegisterCrystal(CollectibleCrystal crystal)
        {
            if (!registeredCrystals.Contains(crystal))
            {
                registeredCrystals.Add(crystal);
                totalCrystalsCount = registeredCrystals.Count;
                OnCrystalCountChanged?.Invoke(collectedCrystalsCount, totalCrystalsCount);
            }
        }

        public void OnCrystalCollected(CollectibleCrystal crystal)
        {
            if (isLevelCompleted || isLevelFailed) return;

            collectedCrystalsCount++;
            OnCrystalCountChanged?.Invoke(collectedCrystalsCount, totalCrystalsCount);

            if (GameManager.Instance != null)
            {
                GameManager.Instance.AddTotalCrystals(1);
            }

            if (collectedCrystalsCount >= totalCrystalsCount)
            {
                OnAllCrystalsCollected?.Invoke();
            }
        }

        public void CompleteLevel()
        {
            if (isLevelCompleted || isLevelFailed) return;

            isLevelCompleted = true;
            OnLevelCompleted?.Invoke();

            if (GameManager.Instance != null)
            {
                GameManager.Instance.SetState(GameState.LevelComplete);
            }

            StartCoroutine(TransitionToNextRoutine());
        }

        private IEnumerator TransitionToNextRoutine()
        {
            yield return new WaitForSeconds(completionDelay);

            if (!string.IsNullOrEmpty(nextSceneName))
            {
                SceneManager.LoadScene(nextSceneName);
            }
            else
            {
                SceneManager.LoadScene("VictoryScene");
            }
        }

        private void HandlePlayerDeath()
        {
            if (isLevelCompleted || isLevelFailed) return;

            isLevelFailed = true;
            OnLevelFailed?.Invoke();

            if (GameManager.Instance != null)
            {
                GameManager.Instance.SetState(GameState.GameOver);
            }
        }

        public void RestartLevel()
        {
            Time.timeScale = 1f;
            Scene currentScene = SceneManager.GetActiveScene();
            SceneManager.LoadScene(currentScene.buildIndex);
        }

        public void ReturnToMainMenu()
        {
            Time.timeScale = 1f;
            SceneManager.LoadScene("MainMenu");
        }
    }
}
