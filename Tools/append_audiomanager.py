import os

scenes_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\Scenes"

GUID_AUDIO_MANAGER = "9fe4f796f9f95f4ab7cc54939a344c58"

GUID_BGM = "323ef241e8855765ba0877a99beb70a5"
GUID_SFX_FLUTTER = "0a080eda5e1b589bb4663b07de6f3225"
GUID_SFX_CRYSTAL = "9c56bfd751e55a71b95940e30ca563c3"
GUID_SFX_DAMAGE = "18aa773ff30b5a3aac30d273935ad8ed"
GUID_SFX_PORTAL = "2d359a8405845e0abca41a2182c51990"
GUID_SFX_COMPLETE = "af06c1c3a8ed5d6d95b779b67656c6b8"
GUID_SFX_GAMEOVER = "d6fd0d28633b513a9970672b8a869cbb"

audio_block = f"""--- !u!1 &950000
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 950001}}
  - component: {{fileID: 950002}}
  m_Layer: 0
  m_Name: AudioManager
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &950001
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 950000}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &950002
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 950000}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_AUDIO_MANAGER}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  bgmCaveAmbient: {{fileID: 8300000, guid: {GUID_BGM}, type: 3}}
  sfxFlutter: {{fileID: 8300000, guid: {GUID_SFX_FLUTTER}, type: 3}}
  sfxCrystal: {{fileID: 8300000, guid: {GUID_SFX_CRYSTAL}, type: 3}}
  sfxDamage: {{fileID: 8300000, guid: {GUID_SFX_DAMAGE}, type: 3}}
  sfxPortalOpen: {{fileID: 8300000, guid: {GUID_SFX_PORTAL}, type: 3}}
  sfxLevelComplete: {{fileID: 8300000, guid: {GUID_SFX_COMPLETE}, type: 3}}
  sfxGameOver: {{fileID: 8300000, guid: {GUID_SFX_GAMEOVER}, type: 3}}
  musicVolume: 0.5
  sfxVolume: 0.7
"""

for target in ["MainMenu.unity", "Level1.unity"]:
    p = os.path.join(scenes_dir, target)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            c = f.read()
        if "AudioManager" not in c:
            with open(p, "a", encoding="utf-8") as f:
                f.write(audio_block)
            print(f"Added AudioManager to {target}")
