import os
import wave
import struct
import math
import random

audio_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\_Game\Audio"
os.makedirs(audio_dir, exist_ok=True)

SAMPLE_RATE = 44100

def write_wav(filename, samples):
    filepath = os.path.join(audio_dir, filename)
    with wave.open(filepath, "w") as wav:
        wav.setnchannels(1)        # Mono
        wav.setsampwidth(2)        # 16-bit
        wav.setframerate(SAMPLE_RATE)
        # Convert float (-1.0 to 1.0) to 16-bit signed PCM
        packed = bytearray()
        for s in samples:
            clamped = max(-1.0, min(1.0, s))
            val = int(clamped * 32767.0)
            packed.extend(struct.pack("<h", val))
        wav.writeframes(packed)
    print(f"Generated audio: {filename} ({len(samples)/SAMPLE_RATE:.2f}s)")

# 1. Wing Flutter / Jump SFX (0.15s, soft airy chirp with envelope)
def gen_sfx_flutter():
    duration = 0.16
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-18.0 * t) # fast exponential decay
        # Soft frequency slide from 380Hz to 620Hz
        freq = 380 + (240 * (t / duration))
        osc = math.sin(2.0 * math.pi * freq * t)
        noise = (random.random() * 2.0 - 1.0) * 0.15 # breathy air sound
        samples.append((osc + noise) * env * 0.45)
    write_wav("sfx_flutter.wav", samples)

# 2. Crystal Collect SFX (0.45s, sparkling celestial arpeggio chime)
def gen_sfx_crystal():
    duration = 0.5
    n_samples = int(SAMPLE_RATE * duration)
    samples = [0.0] * n_samples

    # 3 ascending sine tones: E6 (1318Hz), G#6 (1661Hz), B6 (1975Hz)
    tones = [(0.0, 1318.5), (0.07, 1661.2), (0.14, 1975.5)]
    for start_t, freq in tones:
        start_idx = int(start_t * SAMPLE_RATE)
        for i in range(start_idx, n_samples):
            t = (i - start_idx) / SAMPLE_RATE
            env = math.exp(-7.0 * t)
            samples[i] += math.sin(2.0 * math.pi * freq * t) * env * 0.35
            # overtone
            samples[i] += math.sin(2.0 * math.pi * (freq * 2) * t) * env * 0.12

    write_wav("sfx_crystal.wav", samples)

# 3. Damage / Hazard Hit SFX (0.22s, low impact punch with noisy crunch)
def gen_sfx_damage():
    duration = 0.25
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-14.0 * t)
        # pitch drop from 220Hz down to 60Hz
        freq = max(50, 220 * (1.0 - (t / duration) ** 0.5))
        osc = math.sin(2.0 * math.pi * freq * t)
        noise = (random.random() * 2.0 - 1.0) * 0.3
        samples.append((osc * 0.7 + noise) * env * 0.6)
    write_wav("sfx_damage.wav", samples)

# 4. Portal Unlocked SFX (0.8s, magical ascending resonance chord)
def gen_sfx_portal():
    duration = 0.85
    n_samples = int(SAMPLE_RATE * duration)
    samples = [0.0] * n_samples

    chords = [440.0, 554.37, 659.25, 880.0] # A Major chord
    for c_idx, freq in enumerate(chords):
        offset = c_idx * 0.08
        start_idx = int(offset * SAMPLE_RATE)
        for i in range(start_idx, n_samples):
            t = (i - start_idx) / SAMPLE_RATE
            env = math.sin(math.pi * min(1.0, t / (duration - offset))) ** 0.7 * math.exp(-2.5 * t)
            samples[i] += math.sin(2.0 * math.pi * freq * t) * env * 0.22

    write_wav("sfx_portal_open.wav", samples)

# 5. Level Complete SFX (0.9s, triumphant fanfare chime)
def gen_sfx_level_complete():
    duration = 1.0
    n_samples = int(SAMPLE_RATE * duration)
    samples = [0.0] * n_samples

    notes = [(0.0, 523.25), (0.12, 659.25), (0.24, 783.99), (0.40, 1046.5)] # C5, E5, G5, C6
    for start_t, freq in notes:
        start_idx = int(start_t * SAMPLE_RATE)
        for i in range(start_idx, n_samples):
            t = (i - start_idx) / SAMPLE_RATE
            env = math.exp(-4.5 * t)
            samples[i] += math.sin(2.0 * math.pi * freq * t) * env * 0.3

    write_wav("sfx_level_complete.wav", samples)

# 6. Game Over / Darkness Extinction SFX (1.2s, low descending minor drone)
def gen_sfx_game_over():
    duration = 1.3
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        env = math.exp(-2.2 * t)
        freq = max(35, 160 * math.exp(-1.8 * t))
        osc = math.sin(2.0 * math.pi * freq * t)
        sub = math.sin(2.0 * math.pi * (freq * 0.5) * t) * 0.5
        samples.append((osc + sub) * env * 0.5)
    write_wav("sfx_game_over.wav", samples)

# 7. Ambient Cave Music / Drone (4.0s seamless loop, low atmospheric cave pad)
def gen_bgm_ambient():
    duration = 4.0
    n_samples = int(SAMPLE_RATE * duration)
    samples = []
    for i in range(n_samples):
        t = i / SAMPLE_RATE
        # Seamless loop: frequencies are integer harmonics of (1 / duration = 0.25Hz)
        # Sub-bass root D (73.4Hz -> 294 cycles in 4s), 5th A (110Hz -> 440 cycles)
        f1 = 73.5
        f2 = 110.25
        f3 = 147.0 # octave D
        f4 = 220.5
        mod = 1.0 + 0.15 * math.sin(2.0 * math.pi * 0.5 * t)
        s1 = math.sin(2.0 * math.pi * f1 * t) * 0.4
        s2 = math.sin(2.0 * math.pi * f2 * t) * 0.25
        s3 = math.sin(2.0 * math.pi * f3 * t) * 0.15
        s4 = math.sin(2.0 * math.pi * f4 * t) * 0.08
        # gentle cave rumble
        noise = (random.random() * 2.0 - 1.0) * 0.03
        samples.append((s1 + s2 + s3 + s4 + noise) * mod * 0.4)
    write_wav("bgm_cave_ambient.wav", samples)

if __name__ == "__main__":
    gen_sfx_flutter()
    gen_sfx_crystal()
    gen_sfx_damage()
    gen_sfx_portal()
    gen_sfx_level_complete()
    gen_sfx_game_over()
    gen_bgm_ambient()
