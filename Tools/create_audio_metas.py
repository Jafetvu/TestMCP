import os
import uuid

audio_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\_Game\Audio"

for fname in os.listdir(audio_dir):
    if fname.endswith(".wav"):
        meta_path = os.path.join(audio_dir, fname + ".meta")
        guid = uuid.uuid5(uuid.NAMESPACE_DNS, f"firefly.audio.{fname}").hex
        content = f"""fileFormatVersion: 2
guid: {guid}
AudioImporter:
  serializedVersion: 2
  defaultSetup:
    loadType: 0
    sampleRateSetting: 0
    sampleRateOverride: 44100
    compressionFormat: 0
    quality: 1
    conversionMode: 0
  customUploadSetting: []
  userData: 
  assetBundleName: 
  assetBundleVariant: 
"""
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated meta with serializedVersion: 2 for {fname}")
