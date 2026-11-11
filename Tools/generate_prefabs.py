import os

prefabs_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\_Game\Prefabs"
os.makedirs(prefabs_dir, exist_ok=True)

GUID_SPR_FIREFLY = "abb5d5c5f9685b36961925c9f5bb7813"
GUID_PLAYER_CONTROLLER = "899ab378b2fc53447bdabb190260b34e"
GUID_LIGHT_ENERGY = "f241ae0220265fa1991479c438fa1a83"
GUID_LIGHT2D = "073797afb82c5a1438f328866b10b3f0"
GUID_PLAYER_PREFAB = "7e1289dfb6104f699042a173874be9e1"

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

def create_player_prefab():
    yaml = f"""%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1 &100000
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 100001}}
  - component: {{fileID: 100002}}
  - component: {{fileID: 100003}}
  - component: {{fileID: 100004}}
  - component: {{fileID: 100005}}
  - component: {{fileID: 100006}}
  m_Layer: 0
  m_Name: Player
  m_TagString: Player
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &100001
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100000}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: 100011}}
  - {{fileID: 100021}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &100002
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100000}}
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
  m_SortingOrder: 10
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_FIREFLY}, type: 3}}
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
--- !u!50 &100003
Rigidbody2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100000}}
  m_BodyType: 0
  m_Simulated: 1
  m_UseFullKinematicContacts: 0
  m_UseAutoMass: 0
  m_Mass: 1
  m_LinearDrag: 0.5
  m_AngularDrag: 0.05
  m_GravityScale: 2
  m_Material: {{fileID: 0}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_Interpolate: 1
  m_SleepingMode: 1
  m_CollisionDetection: 1
  m_Constraints: 4
--- !u!58 &100004
CircleCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100000}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IncludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_ExcludeLayers:
    serializedVersion: 2
    m_Bits: 0
  m_IsTrigger: 0
  m_UsedByEffector: 0
  m_UsedByComposite: 0
  m_Offset: {{x: 0, y: -0.05}}
  serializedVersion: 2
  m_Radius: 0.35
--- !u!114 &100005
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100000}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_PLAYER_CONTROLLER}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  moveSpeed: 6.5
  acceleration: 35
  deceleration: 30
  jumpForce: 10
  maxAirFlaps: 2
  flutterHoverForce: 12
  maxFallSpeed: -8
  fallGravityMultiplier: 1.6
  groundCheck: {{fileID: 100011}}
  groundCheckSize: {{x: 0.4, y: 0.15}}
  groundLayer:
    serializedVersion: 2
    m_Bits: 1
  spriteRenderer: {{fileID: 100002}}
  visualTransform: {{fileID: 100001}}
--- !u!114 &100006
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100000}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT_ENERGY}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  maxEnergy: 100
  initialEnergy: 100
  drainRatePerSecond: 4.5
  criticalThreshold: 0.25
  fireflyLight: {{fileID: 100022}}
  maxOuterRadius: 6.5
  minOuterRadius: 1.2
  maxInnerRadius: 2.0
  minInnerRadius: 0.3
  baseIntensity: 1.1
  fullEnergyColor: {{r: 1, g: 0.95, b: 0.65, a: 1}}
  criticalEnergyColor: {{r: 0.95, g: 0.35, b: 0.2, a: 1}}
  enableFlickerWhenLow: 1
  flickerSpeed: 12
  flickerAmplitude: 0.15
--- !u!1 &100010
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 100011}}
  m_Layer: 0
  m_Name: GroundCheck
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &100011
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100010}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: -0.38, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 100001}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!1 &100020
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: 100021}}
  - component: {{fileID: 100022}}
  m_Layer: 0
  m_Name: FireflyLight2D
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &100021
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100020}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 100001}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &100022
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: 100020}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT2D}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  m_ComponentVersion: 1
  m_LightType: 3
  m_BlendStyleIndex: 0
  m_FalloffIntensity: 0.5
  m_Color: {{r: 1, g: 0.95, b: 0.65, a: 1}}
  m_Intensity: 1.1
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
    m_Extent: {{x: 6.5, y: 6.5, z: 0}}
  m_PointLightInnerAngle: 360
  m_PointLightOuterAngle: 360
  m_PointLightInnerRadius: 2.0
  m_PointLightOuterRadius: 6.5
  m_ShapeLightParametricSides: 5
  m_ShapeLightParametricAngleOffset: 0
  m_ShapeLightParametricRadius: 1
"""
    write_prefab("Player", yaml, GUID_PLAYER_PREFAB)

if __name__ == "__main__":
    create_player_prefab()
