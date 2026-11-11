import os
import uuid

prefabs_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\_Game\Prefabs"
os.makedirs(prefabs_dir, exist_ok=True)

GUID_SPR_FIREFLY = "abb5d5c5f9685b36961925c9f5bb7813"
GUID_SPR_CRYSTAL = "0083639b47d65e56891096dc64ed1183"
GUID_SPR_PORTAL = "80d0ef6552765a709e869fded111900f"
GUID_SPR_BAT = "a8da44e537a55ec2beb4bab97cffb046"
GUID_SPR_SPIKES = "32cc13c1003151ff888e371f35647ffd"
GUID_SPR_PLATFORM = "d9d07a5f4b045d30b1b6495c7dac444b"

GUID_PLAYER_CONTROLLER = "899ab378b2fc53447bdabb190260b34e"
GUID_LIGHT_ENERGY = "f241ae0220265fa1991479c438fa1a83"
GUID_COLLECTIBLE_CRYSTAL = "fdf590220be25017ab4b20c84e8640c1"
GUID_LEVEL_EXIT = "278a35d3fa2f538a81f40679e6dde363"
GUID_LIGHT2D = "073797afb82c5a1438f328866b10b3f0"

GUID_PLAYER_PREFAB = "7e1289dfb6104f699042a173874be9e1"
GUID_CRYSTAL_PREFAB = "3c2419ab0011559988aabbccddeeff01"
GUID_PORTAL_PREFAB = "3c2419ab0011559988aabbccddeeff02"

def write_prefab(name, content, guid):
    prefab_path = os.path.join(prefabs_dir, f"{name}.prefab")
    meta_path = prefab_path + ".meta"

    with open(prefab_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

    if not os.path.exists(meta_path):
        meta_content = f"""fileFormatVersion: 2
guid: {guid}
PrefabImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
"""
        with open(meta_path, "w", encoding="utf-8") as f:
            f.write(meta_content)
    print(f"Generated prefab: {name}")

def create_crystal_prefab():
    yaml = f"""%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1 &200000
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 200001}}
  - component: {{fileID: 200002}}
  - component: {{fileID: 200003}}
  - component: {{fileID: 200004}}
  m_Layer: 0
  m_Name: Crystal
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &200001
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 200000}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: 200011}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &200002
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 200000}}
  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RayTracingMode: 0
  m_RayTraceProcedural: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_Materials:
  - {{fileID: 10754, guid: 0000000000000000f000000000000000, type: 0}}
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {{fileID: 0}}
  m_ProbeAnchor: {{fileID: 0}}
  m_LightProbeVolumeOverride: {{fileID: 0}}
  m_ScaleInLightmap: 1
  m_ReceiveGI: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 1
  m_SelectedEditorRenderState: 0
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {{fileID: 0}}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 5
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_CRYSTAL}, type: 3}}
  m_Color: {{r: 1, g: 1, b: 1, a: 1}}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {{x: 1, y: 1}}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WasSpriteAssigned: 1
  m_MaskInteraction: 0
  m_SpriteSortPoint: 0
--- !u!58 &200003
CircleCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 200000}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_IsTrigger: 1
  m_UsedByEffector: 0
  m_UsedByComposite: 0
  m_Offset: {{x: 0, y: 0}}
  serializedVersion: 2
  m_Radius: 0.4
--- !u!114 &200004
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 200000}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_COLLECTIBLE_CRYSTAL}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  energyRestored: 35
  spriteRenderer: {{fileID: 200002}}
  crystalLight: {{fileID: 200012}}
  bobSpeed: 3
  bobHeight: 0.12
  pulseSpeed: 4
--- !u!1 &200010
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 200011}}
  - component: {{fileID: 200012}}
  m_Layer: 0
  m_Name: CrystalLight2D
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &200011
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 200010}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 200001}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &200012
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 200010}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT2D}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  m_ComponentVersion: 1
  m_LightType: 3
  m_BlendStyleIndex: 0
  m_FalloffIntensity: 0.5
  m_Color: {{r: 0.2, g: 0.9, b: 1, a: 1}}
  m_Intensity: 1.2
  m_LightVolumeIntensity: 1
  m_LightVolumeIntensityEnabled: 0
  m_ApplyToSortingLayers: 00000000
  m_LightCookieSprite: {{fileID: 0}}
  m_DeprecatedPointLightCookieSprite: {{fileID: 0}}
  m_LightOrder: 0
  m_OverlapOperation: 0
  m_NormalMapDistance: 3
  m_NormalMapQuality: 2
  m_UseNormalMap: 0
  m_ShadowIntensityEnabled: 0
  m_ShadowIntensity: 0.75
  m_ShadowVolumeIntensityEnabled: 0
  m_ShadowVolumeIntensity: 0.75
  m_LocalBounds:
    m_Center: {{x: 0, y: 0, z: 0}}
    m_Extent: {{x: 2.5, y: 2.5, z: 0}}
  m_PointLightInnerAngle: 360
  m_PointLightOuterAngle: 360
  m_PointLightInnerRadius: 0.4
  m_PointLightOuterRadius: 2.5
  m_ShapeLightParametricSides: 5
  m_ShapeLightParametricAngleOffset: 0
  m_ShapeLightParametricRadius: 1
"""
    write_prefab("Crystal", yaml, GUID_CRYSTAL_PREFAB)

def create_portal_prefab():
    yaml = f"""%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1 &300000
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 300001}}
  - component: {{fileID: 300002}}
  - component: {{fileID: 300003}}
  - component: {{fileID: 300004}}
  m_Layer: 0
  m_Name: ExitPortal
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &300001
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 300000}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: 300011}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &300002
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 300000}}
  m_Enabled: 1
  m_CastShadows: 0
  m_ReceiveShadows: 0
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RayTracingMode: 0
  m_RayTraceProcedural: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_Materials:
  - {{fileID: 10754, guid: 0000000000000000f000000000000000, type: 0}}
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {{fileID: 0}}
  m_ProbeAnchor: {{fileID: 0}}
  m_LightProbeVolumeOverride: {{fileID: 0}}
  m_ScaleInLightmap: 1
  m_ReceiveGI: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 1
  m_SelectedEditorRenderState: 0
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {{fileID: 0}}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 2
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_PORTAL}, type: 3}}
  m_Color: {{r: 0.4, g: 0.45, b: 0.5, a: 0.6}}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {{x: 1.5, y: 1.5}}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WasSpriteAssigned: 1
  m_MaskInteraction: 0
  m_SpriteSortPoint: 0
--- !u!61 &300003
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 300000}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_IsTrigger: 1
  m_UsedByEffector: 0
  m_UsedByComposite: 0
  m_Offset: {{x: 0, y: 0}}
  m_SpriteTilingProperty:
    border: {{x: 0, y: 0, z: 0, w: 0}}
    pivot: {{x: 0.5, y: 0.5}}
    oldSize: {{x: 1.5, y: 1.5}}
    newSize: {{x: 1.5, y: 1.5}}
    adaptiveTilingThreshold: 0.5
    drawMode: 0
    adaptiveTiling: 0
  m_AutoTiling: 0
  serializedVersion: 2
  m_Size: {{x: 1.2, y: 1.4}}
  m_EdgeRadius: 0
--- !u!114 &300004
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 300000}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LEVEL_EXIT}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  portalRenderer: {{fileID: 300002}}
  portalLight: {{fileID: 300012}}
  lockedColor: {{r: 0.4, g: 0.45, b: 0.5, a: 0.6}}
  unlockedColor: {{r: 0.2, g: 0.95, b: 1, a: 1}}
  lockedLightRadius: 1.5
  unlockedLightRadius: 5
  unlockedLightIntensity: 1.6
--- !u!1 &300010
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 300011}}
  - component: {{fileID: 300012}}
  m_Layer: 0
  m_Name: PortalLight2D
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &300011
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 300010}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 300001}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &300012
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 300010}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT2D}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  m_ComponentVersion: 1
  m_LightType: 3
  m_BlendStyleIndex: 0
  m_FalloffIntensity: 0.5
  m_Color: {{r: 0.4, g: 0.45, b: 0.5, a: 1}}
  m_Intensity: 0.5
  m_LightVolumeIntensity: 1
  m_LightVolumeIntensityEnabled: 0
  m_ApplyToSortingLayers: 00000000
  m_LightCookieSprite: {{fileID: 0}}
  m_DeprecatedPointLightCookieSprite: {{fileID: 0}}
  m_LightOrder: 0
  m_OverlapOperation: 0
  m_NormalMapDistance: 3
  m_NormalMapQuality: 2
  m_UseNormalMap: 0
  m_ShadowIntensityEnabled: 0
  m_ShadowIntensity: 0.75
  m_ShadowVolumeIntensityEnabled: 0
  m_ShadowVolumeIntensity: 0.75
  m_LocalBounds:
    m_Center: {{x: 0, y: 0, z: 0}}
    m_Extent: {{x: 1.5, y: 1.5, z: 0}}
  m_PointLightInnerAngle: 360
  m_PointLightOuterAngle: 360
  m_PointLightInnerRadius: 0.3
  m_PointLightOuterRadius: 1.5
  m_ShapeLightParametricSides: 5
  m_ShapeLightParametricAngleOffset: 0
  m_ShapeLightParametricRadius: 1
"""
    write_prefab("ExitPortal", yaml, GUID_PORTAL_PREFAB)

if __name__ == "__main__":
    create_crystal_prefab()
    create_portal_prefab()
