using UnityEngine;
using Firefly.Core;
using Firefly.Environment;
using Firefly.Player;
using Firefly.Light;

namespace Firefly.Audio
{
    /// <summary>
    /// Central audio manager that handles sound effects and ambient cave music.
    /// Follows the Single Responsibility Principle: coordinates sound playback and audio event binding.
    /// </summary>
    public class AudioManager : MonoBehaviour
    {
        public static AudioManager Instance { get; private set; }

        [Header("Audio Sources")]
        [SerializeField] private AudioSource musicSource;
        [SerializeField] private AudioSource sfxSource;

        [Header("Music Tracks")]
        [SerializeField] private AudioClip bgmCaveAmbient;

        [Header("Sound Effects")]
        [SerializeField] private AudioClip sfxFlutter;
        [SerializeField] private AudioClip sfxCrystal;
        [SerializeField] private AudioClip sfxDamage;
        [SerializeField] private AudioClip sfxPortalOpen;
        [SerializeField] private AudioClip sfxLevelComplete;
        [SerializeField] private AudioClip sfxGameOver;

        [Header("Volume Controls")]
        [Range(0f, 1f)] [SerializeField] private float musicVolume = 0.5f;
        [Range(0f, 1f)] [SerializeField] private float sfxVolume = 0.7f;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }

            Instance = this;
            DontDestroyOnLoad(gameObject);

            SetupAudioSources();
        }

        private void Start()
        {
            PlayAmbientMusic();
            SubscribeToEvents();
        }

        private void OnDestroy()
        {
            if (Instance == this)
            {
                UnsubscribeFromEvents();
            }
        }

        private void SetupAudioSources()
        {
            if (musicSource == null)
            {
                musicSource = gameObject.AddComponent<AudioSource>();
            }
            musicSource.loop = true;
            musicSource.playOnAwake = false;
            musicSource.volume = musicVolume;

            if (sfxSource == null)
            {
                sfxSource = gameObject.AddComponent<AudioSource>();
            }
            sfxSource.loop = false;
            sfxSource.playOnAwake = false;
            sfxSource.volume = sfxVolume;
        }

        private void SubscribeToEvents()
        {
            CollectibleCrystal.OnAnyCrystalCollected += HandleCrystalCollected;
            LevelExit.OnPortalUnlocked += HandlePortalUnlocked;
            LevelExit.OnPortalEntered += HandlePortalEntered;
        }

        private void UnsubscribeFromEvents()
        {
            CollectibleCrystal.OnAnyCrystalCollected -= HandleCrystalCollected;
            LevelExit.OnPortalUnlocked -= HandlePortalUnlocked;
            LevelExit.OnPortalEntered -= HandlePortalEntered;
        }

        public void PlayAmbientMusic()
        {
            if (bgmCaveAmbient != null && musicSource != null)
            {
                if (musicSource.clip != bgmCaveAmbient || !musicSource.isPlaying)
                {
                    musicSource.clip = bgmCaveAmbient;
                    musicSource.volume = musicVolume;
                    musicSource.Play();
                }
            }
        }

        public void PlayFlutter()
        {
            PlaySFX(sfxFlutter, pitchRange: 0.08f, volumeScale: 0.75f);
        }

        public void PlayCrystal()
        {
            PlaySFX(sfxCrystal, pitchRange: 0.05f, volumeScale: 1.0f);
        }

        public void PlayDamage()
        {
            PlaySFX(sfxDamage, pitchRange: 0.04f, volumeScale: 1.0f);
        }

        public void PlayPortalUnlocked()
        {
            PlaySFX(sfxPortalOpen, pitchRange: 0.0f, volumeScale: 1.0f);
        }

        public void PlayLevelComplete()
        {
            PlaySFX(sfxLevelComplete, pitchRange: 0.0f, volumeScale: 1.0f);
        }

        public void PlayGameOver()
        {
            PlaySFX(sfxGameOver, pitchRange: 0.0f, volumeScale: 1.0f);
        }

        private void PlaySFX(AudioClip clip, float pitchRange = 0f, float volumeScale = 1.0f)
        {
            if (clip == null || sfxSource == null) return;

            if (pitchRange > 0f)
            {
                sfxSource.pitch = 1.0f + Random.Range(-pitchRange, pitchRange);
            }
            else
            {
                sfxSource.pitch = 1.0f;
            }

            sfxSource.PlayOneShot(clip, volumeScale * sfxVolume);
        }

        // Automatic Event Handlers
        private void HandleCrystalCollected(CollectibleCrystal crystal)
        {
            PlayCrystal();
        }

        private void HandlePortalUnlocked()
        {
            PlayPortalUnlocked();
        }

        private void HandlePortalEntered()
        {
            PlayLevelComplete();
        }

        /// <summary>
        /// Registers a newly spawned player's controller and light events for sound feedback.
        /// </summary>
        public void BindPlayer(PlayerController player, LightEnergy light)
        {
            if (player != null)
            {
                player.OnJump += PlayFlutter;
                player.OnFlutter += PlayFlutter;
                player.OnDamaged += PlayDamage;
            }

            if (light != null)
            {
                light.OnEnergyDepleted += PlayGameOver;
            }
        }
    }
}
