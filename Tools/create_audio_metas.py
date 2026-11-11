import os
import uuid

audio_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\_Game\Audio"

for fname in os.listdir(audio_dir):
    if fname.endswith(".wav"):
        meta_path = os.path.join(audio_dir, fname + ".meta")
        if not os.path.exists(meta_path):
            guid = uuid.uuid5(uuid.NAMESPACE_DNS, f"firefly.audio.{fname}").hex
            content = f"""fileFormatVersion: 2
guid: {guid}
AudioImporter:
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
            print(f"Created meta for {fname} (guid: {guid})")
