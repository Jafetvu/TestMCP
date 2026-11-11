import os
import uuid

scenes_dir = r"C:\Users\Jafet_BaGo\Desktop\TestMCP\Assets\Scenes"
os.makedirs(scenes_dir, exist_ok=True)

# GUID constants
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
GUID_LEVEL_MANAGER = "47f3e2b6088156b0a6b3c57ba4cfcc41"
GUID_CAMERA_FOLLOW = "8fb30b9195e35b298a48832070b5bae3"
GUID_ENEMY_PATROL = "ae2f6db7fa6c5b8ca78addbb774a0b3d"
GUID_HAZARD_SPIKES = "7e492d56900c5197853be7da377cb652"
GUID_MOVING_PLATFORM = "79b971c2c0305995abbed3c0f69b699d"
GUID_KILL_ZONE = "937103ba0a4953008a2d61283e98222f"
GUID_LIGHT2D = "073797afb82c5a1438f328866b10b3f0"

SCENE_HEADER = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!29 &1
OcclusionCullingSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_OcclusionBakeSettings:
    smallestOccluder: 5
    smallestHole: 0.25
    backfaceThreshold: 100
  m_SceneGUID: 00000000000000000000000000000000
  m_OcclusionCullingData: {fileID: 0}
--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 9
  m_Fog: 0
  m_FogColor: {r: 0.5, g: 0.5, b: 0.5, a: 1}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientSkyColor: {r: 0.05, g: 0.05, b: 0.08, a: 1}
  m_AmbientEquatorColor: {r: 0.03, g: 0.03, b: 0.05, a: 1}
  m_AmbientGroundColor: {r: 0.02, g: 0.02, b: 0.03, a: 1}
  m_AmbientIntensity: 1
  m_AmbientMode: 3
  m_SubtractiveShadowColor: {r: 0.42, g: 0.478, b: 0.627, a: 1}
  m_SkyboxMaterial: {fileID: 0}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {fileID: 0}
  m_SpotCookie: {fileID: 10001, guid: 0000000000000000e000000000000000, type: 0}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {fileID: 0}
  m_Sun: {fileID: 0}
  m_IndirectSpecularColor: {r: 0, g: 0, b: 0, a: 1}
  m_UseRadianceAmbientProbe: 0
--- !u!157 &3
LightmapSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 12
  m_GIWorkflowMode: 1
  m_GISettings:
    serializedVersion: 2
    m_BounceScale: 1
    m_IndirectOutputScale: 1
    m_AlbedoBoost: 1
    m_EnvironmentLightingMode: 0
    m_EnableBakedLightmaps: 0
    m_EnableRealtimeLightmaps: 0
  m_LightmapEditorSettings:
    serializedVersion: 12
    m_Resolution: 2
    m_BakeResolution: 40
    m_AtlasSize: 1024
    m_AO: 0
    m_AOMaxDistance: 1
    m_CompAOExponent: 1
    m_CompAOExponentDirect: 0
    m_ExtractAmbientOcclusion: 0
    m_Padding: 2
    m_LightmapParameters: {fileID: 0}
    m_LightmapsBakeMode: 1
    m_TextureCompression: 1
    m_FinalGather: 0
--- !u!196 &4
NavMeshSettings:
  serializedVersion: 2
  m_ObjectHideFlags: 0
  m_BuildSettings:
    serializedVersion: 2
    agentTypeID: 0
    agentRadius: 0.5
    agentHeight: 2
    agentSlope: 45
    agentClimb: 0.4
    ledgeDropHeight: 0
    maxJumpAcrossDistance: 0
    minRegionArea: 2
    manualCellSize: 0
    cellSize: 0.16666667
    manualTileSize: 0
    tileSize: 256
    accuratePlacement: 0
"""

class SceneBuilder:
    def __init__(self, scene_name, level_num, level_title, next_scene):
        self.scene_name = scene_name
        self.level_num = level_num
        self.level_title = level_title
        self.next_scene = next_scene
        self.next_id = 100
        self.blocks = []

    def get_id(self):
        val = self.next_id
        self.next_id += 1
        return val

    def add_camera_and_environment(self):
        cam_go = self.get_id()
        cam_tr = self.get_id()
        cam_cmp = self.get_id()
        cam_listener = self.get_id()
        cam_follow = self.get_id()

        self.blocks.append(f"""--- !u!1 &{cam_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {cam_tr}}}
  - component: {{fileID: {cam_cmp}}}
  - component: {{fileID: {cam_listener}}}
  - component: {{fileID: {cam_follow}}}
  m_Layer: 0
  m_Name: Main Camera
  m_TagString: MainCamera
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{cam_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {cam_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 1, z: -10}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!20 &{cam_cmp}
Camera:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {cam_go}}}
  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 2
  m_BackGroundColor: {{r: 0.04, g: 0.03, b: 0.08, a: 1}}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_Iso: 200
  m_ShutterSpeed: 0.005
  m_Aperture: 16
  m_FocusDistance: 10
  m_FocalLength: 50
  m_BladeCount: 5
  m_Curvature: {{x: 2, y: 11}}
  m_BarrelClipping: 0.25
  m_Anamorphism: 0
  m_SensorSize: {{x: 36, y: 24}}
  m_LensShift: {{x: 0, y: 0}}
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.3
  far clip plane: 1000
  field of view: 60
  orthographic: 1
  orthographic size: 5.5
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {{fileID: 0}}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 1
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRT: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
--- !u!81 &{cam_listener}
AudioListener:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {cam_go}}}
  m_Enabled: 1
--- !u!114 &{cam_follow}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {cam_go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_CAMERA_FOLLOW}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  offset: {{x: 0, y: 1, z: -10}}
  smoothTime: 0.2
  useBounds: 0
""")

        # Global Light 2D (dark ambient cave)
        gl_go = self.get_id()
        gl_tr = self.get_id()
        gl_lgt = self.get_id()
        self.blocks.append(f"""--- !u!1 &{gl_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {gl_tr}}}
  - component: {{fileID: {gl_lgt}}}
  m_Layer: 0
  m_Name: Global Light 2D
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{gl_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {gl_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &{gl_lgt}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {gl_go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT2D}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  m_ComponentVersion: 1
  m_LightType: 4
  m_BlendStyleIndex: 0
  m_FalloffIntensity: 0.5
  m_Color: {{r: 0.08, g: 0.1, b: 0.16, a: 1}}
  m_Intensity: 0.08
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
""")

    def add_level_manager(self, spawn_x=0, spawn_y=0):
        spawn_go = self.get_id()
        spawn_tr = self.get_id()
        mgr_go = self.get_id()
        mgr_tr = self.get_id()
        mgr_cmp = self.get_id()

        self.blocks.append(f"""--- !u!1 &{spawn_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {spawn_tr}}}
  m_Layer: 0
  m_Name: PlayerSpawnPoint
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{spawn_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {spawn_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {spawn_x}, y: {spawn_y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!1 &{mgr_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {mgr_tr}}}
  - component: {{fileID: {mgr_cmp}}}
  m_Layer: 0
  m_Name: LevelManager
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{mgr_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {mgr_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &{mgr_cmp}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {mgr_go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LEVEL_MANAGER}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  levelNumber: {self.level_num}
  levelTitle: "{self.level_title}"
  nextSceneName: "{self.next_scene}"
  playerSpawnPoint: {{fileID: {spawn_tr}}}
  completionDelay: 1.2
  gameOverDelay: 1
""")

    def add_player(self, x=0, y=0):
        p_go = self.get_id()
        p_tr = self.get_id()
        p_sr = self.get_id()
        p_rb = self.get_id()
        p_col = self.get_id()
        p_ctrl = self.get_id()
        p_lgt_en = self.get_id()

        gc_go = self.get_id()
        gc_tr = self.get_id()

        fl_go = self.get_id()
        fl_tr = self.get_id()
        fl_lgt = self.get_id()

        self.blocks.append(f"""--- !u!1 &{p_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {p_tr}}}
  - component: {{fileID: {p_sr}}}
  - component: {{fileID: {p_rb}}}
  - component: {{fileID: {p_col}}}
  - component: {{fileID: {p_ctrl}}}
  - component: {{fileID: {p_lgt_en}}}
  m_Layer: 0
  m_Name: Player
  m_TagString: Player
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{p_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {p_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {x}, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: {gc_tr}}}
  - {{fileID: {fl_tr}}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{p_sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {p_go}}}
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
--- !u!50 &{p_rb}
Rigidbody2D:
  serializedVersion: 4
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {p_go}}}
  m_BodyType: 0
  m_Simulated: 1
  m_UseFullKinematicContacts: 0
  m_UseAutoMass: 0
  m_Mass: 1
  m_LinearDrag: 0.5
  m_AngularDrag: 0.05
  m_GravityScale: 2
  m_Material: {{fileID: 0}}
  m_Interpolate: 1
  m_SleepingMode: 1
  m_CollisionDetection: 1
  m_Constraints: 4
--- !u!58 &{p_col}
CircleCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {p_go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 0
  m_Offset: {{x: 0, y: -0.05}}
  serializedVersion: 2
  m_Radius: 0.35
--- !u!114 &{p_ctrl}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {p_go}}}
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
  groundCheck: {{fileID: {gc_tr}}}
  groundCheckSize: {{x: 0.4, y: 0.15}}
  groundLayer:
    serializedVersion: 2
    m_Bits: 1
  spriteRenderer: {{fileID: {p_sr}}}
  visualTransform: {{fileID: {p_tr}}}
--- !u!114 &{p_lgt_en}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {p_go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT_ENERGY}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  maxEnergy: 100
  initialEnergy: 100
  drainRatePerSecond: 4.5
  criticalThreshold: 0.25
  fireflyLight: {{fileID: {fl_lgt}}}
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
--- !u!1 &{gc_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {gc_tr}}}
  m_Layer: 0
  m_Name: GroundCheck
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{gc_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {gc_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: -0.38, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: {p_tr}}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!1 &{fl_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {fl_tr}}}
  - component: {{fileID: {fl_lgt}}}
  m_Layer: 0
  m_Name: FireflyLight2D
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{fl_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {fl_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: {p_tr}}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &{fl_lgt}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {fl_go}}}
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
""")

    def add_platform(self, x, y, width=3, height=1):
        go = self.get_id()
        tr = self.get_id()
        sr = self.get_id()
        col = self.get_id()

        self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {sr}}}
  - component: {{fileID: {col}}}
  m_Layer: 0
  m_Name: Platform_{x}_{y}
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {x}, y: {y}, z: 0}}
  m_LocalScale: {{x: {width / 3.0}, y: {height}, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
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
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 1
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_PLATFORM}, type: 3}}
  m_Color: {{r: 1, g: 1, b: 1, a: 1}}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {{x: 3, y: 1}}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WasSpriteAssigned: 1
  m_MaskInteraction: 0
  m_SpriteSortPoint: 0
--- !u!61 &{col}
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 0
  m_Offset: {{x: 0, y: 0}}
  m_SpriteTilingProperty:
    border: {{x: 0, y: 0, z: 0, w: 0}}
    pivot: {{x: 0.5, y: 0.5}}
    oldSize: {{x: 3, y: 1}}
    newSize: {{x: 3, y: 1}}
    adaptiveTilingThreshold: 0.5
    drawMode: 0
    adaptiveTiling: 0
  m_AutoTiling: 0
  serializedVersion: 2
  m_Size: {{x: 3, y: 1}}
  m_EdgeRadius: 0
""")

    def add_crystal(self, x, y):
        go = self.get_id()
        tr = self.get_id()
        sr = self.get_id()
        col = self.get_id()
        scr = self.get_id()
        l_go = self.get_id()
        l_tr = self.get_id()
        l_cmp = self.get_id()

        self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {sr}}}
  - component: {{fileID: {col}}}
  - component: {{fileID: {scr}}}
  m_Layer: 0
  m_Name: Crystal_{x}_{y}
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {x}, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: {l_tr}}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
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
--- !u!58 &{col}
CircleCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 1
  m_Offset: {{x: 0, y: 0}}
  serializedVersion: 2
  m_Radius: 0.4
--- !u!114 &{scr}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_COLLECTIBLE_CRYSTAL}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  energyRestored: 35
  spriteRenderer: {{fileID: {sr}}}
  crystalLight: {{fileID: {l_cmp}}}
  bobSpeed: 3
  bobHeight: 0.12
  pulseSpeed: 4
--- !u!1 &{l_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {l_tr}}}
  - component: {{fileID: {l_cmp}}}
  m_Layer: 0
  m_Name: Light
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{l_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {l_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: {tr}}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &{l_cmp}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {l_go}}}
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
""")

    def add_spikes(self, x, y, count=1):
        for i in range(count):
            sp_x = x + (i * 0.9)
            go = self.get_id()
            tr = self.get_id()
            sr = self.get_id()
            col = self.get_id()
            scr = self.get_id()

            self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {sr}}}
  - component: {{fileID: {col}}}
  - component: {{fileID: {scr}}}
  m_Layer: 0
  m_Name: Spikes_{sp_x}_{y}
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {sp_x}, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
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
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 3
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_SPIKES}, type: 3}}
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
--- !u!61 &{col}
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 1
  m_Offset: {{x: 0, y: -0.15}}
  m_SpriteTilingProperty:
    border: {{x: 0, y: 0, z: 0, w: 0}}
    pivot: {{x: 0.5, y: 0.5}}
    oldSize: {{x: 1, y: 1}}
    newSize: {{x: 1, y: 1}}
    adaptiveTilingThreshold: 0.5
    drawMode: 0
    adaptiveTiling: 0
  m_AutoTiling: 0
  serializedVersion: 2
  m_Size: {{x: 0.9, y: 0.7}}
  m_EdgeRadius: 0
--- !u!114 &{scr}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_HAZARD_SPIKES}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  damageAmount: 30
  knockbackForce: 9
  damageCooldown: 0.6
""")

    def add_bat(self, x, y, patrol_dist=4.0, speed=2.5):
        go = self.get_id()
        tr = self.get_id()
        sr = self.get_id()
        col = self.get_id()
        scr = self.get_id()
        l_go = self.get_id()
        l_tr = self.get_id()
        l_cmp = self.get_id()

        self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {sr}}}
  - component: {{fileID: {col}}}
  - component: {{fileID: {scr}}}
  m_Layer: 0
  m_Name: EnemyBat_{x}_{y}
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {x}, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: {l_tr}}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
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
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 8
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_BAT}, type: 3}}
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
--- !u!58 &{col}
CircleCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 1
  m_Offset: {{x: 0, y: 0}}
  serializedVersion: 2
  m_Radius: 0.45
--- !u!114 &{scr}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_ENEMY_PATROL}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  speed: {speed}
  patrolDistance: {patrol_dist}
  flyWaveSpeed: 6
  flyWaveHeight: 0.25
  damageAmount: 25
  knockbackForce: 10
  hitCooldown: 0.75
  spriteRenderer: {{fileID: {sr}}}
  eyeGlowLight: {{fileID: {l_cmp}}}
--- !u!1 &{l_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {l_tr}}}
  - component: {{fileID: {l_cmp}}}
  m_Layer: 0
  m_Name: EyesLight
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{l_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {l_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: {tr}}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &{l_cmp}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {l_go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LIGHT2D}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  m_ComponentVersion: 1
  m_LightType: 3
  m_BlendStyleIndex: 0
  m_FalloffIntensity: 0.5
  m_Color: {{r: 1, g: 0.15, b: 0.2, a: 1}}
  m_Intensity: 0.8
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
    m_Extent: {{x: 2, y: 2, z: 0}}
  m_PointLightInnerAngle: 360
  m_PointLightOuterAngle: 360
  m_PointLightInnerRadius: 0.2
  m_PointLightOuterRadius: 2.0
  m_ShapeLightParametricSides: 5
  m_ShapeLightParametricAngleOffset: 0
  m_ShapeLightParametricRadius: 1
""")

    def add_moving_platform(self, x, y, offset_x=4.0, offset_y=0.0, speed=2.0):
        go = self.get_id()
        tr = self.get_id()
        sr = self.get_id()
        col = self.get_id()
        scr = self.get_id()

        self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {sr}}}
  - component: {{fileID: {col}}}
  - component: {{fileID: {scr}}}
  m_Layer: 0
  m_Name: MovingPlatform_{x}_{y}
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {x}, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
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
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: 1
  m_Sprite: {{fileID: 21300000, guid: {GUID_SPR_PLATFORM}, type: 3}}
  m_Color: {{r: 1, g: 1, b: 1, a: 1}}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {{x: 3, y: 1}}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WasSpriteAssigned: 1
  m_MaskInteraction: 0
  m_SpriteSortPoint: 0
--- !u!61 &{col}
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 0
  m_Offset: {{x: 0, y: 0}}
  m_SpriteTilingProperty:
    border: {{x: 0, y: 0, z: 0, w: 0}}
    pivot: {{x: 0.5, y: 0.5}}
    oldSize: {{x: 3, y: 1}}
    newSize: {{x: 3, y: 1}}
    adaptiveTilingThreshold: 0.5
    drawMode: 0
    adaptiveTiling: 0
  m_AutoTiling: 0
  serializedVersion: 2
  m_Size: {{x: 3, y: 1}}
  m_EdgeRadius: 0
--- !u!114 &{scr}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_MOVING_PLATFORM}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  moveOffset: {{x: {offset_x}, y: {offset_y}}}
  speed: {speed}
  waitTimeAtEnds: 0.5
""")

    def add_exit_portal(self, x, y):
        go = self.get_id()
        tr = self.get_id()
        sr = self.get_id()
        col = self.get_id()
        scr = self.get_id()
        l_go = self.get_id()
        l_tr = self.get_id()
        l_cmp = self.get_id()

        self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {sr}}}
  - component: {{fileID: {col}}}
  - component: {{fileID: {scr}}}
  m_Layer: 0
  m_Name: ExitPortal
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: {x}, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children:
  - {{fileID: {l_tr}}}
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!212 &{sr}
SpriteRenderer:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
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
--- !u!61 &{col}
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 1
  m_Offset: {{x: 0, y: 0}}
  serializedVersion: 2
  m_Size: {{x: 1.2, y: 1.4}}
  m_EdgeRadius: 0
--- !u!114 &{scr}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_LEVEL_EXIT}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
  portalRenderer: {{fileID: {sr}}}
  portalLight: {{fileID: {l_cmp}}}
  lockedColor: {{r: 0.4, g: 0.45, b: 0.5, a: 0.6}}
  unlockedColor: {{r: 0.2, g: 0.95, b: 1, a: 1}}
  lockedLightRadius: 1.5
  unlockedLightRadius: 5
  unlockedLightIntensity: 1.6
--- !u!1 &{l_go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {l_tr}}}
  - component: {{fileID: {l_cmp}}}
  m_Layer: 0
  m_Name: PortalLight
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{l_tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {l_go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 0, y: 0, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: {tr}}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!114 &{l_cmp}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {l_go}}}
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
""")

    def add_kill_zone(self, y=-10, width=120):
        go = self.get_id()
        tr = self.get_id()
        col = self.get_id()
        scr = self.get_id()

        self.blocks.append(f"""--- !u!1 &{go}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
  - component: {{fileID: {tr}}}
  - component: {{fileID: {col}}}
  - component: {{fileID: {scr}}}
  m_Layer: 0
  m_Name: KillZone
  m_TagString: Untagged
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!4 &{tr}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  serializedVersion: 2
  m_LocalRotation: {{x: 0, y: 0, z: 0, w: 1}}
  m_LocalPosition: {{x: 20, y: {y}, z: 0}}
  m_LocalScale: {{x: 1, y: 1, z: 1}}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {{fileID: 0}}
  m_LocalEulerAnglesHint: {{x: 0, y: 0, z: 0}}
--- !u!61 &{col}
BoxCollider2D:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_Density: 1
  m_Material: {{fileID: 0}}
  m_IsTrigger: 1
  m_Offset: {{x: 0, y: 0}}
  serializedVersion: 2
  m_Size: {{x: {width}, y: 4}}
  m_EdgeRadius: 0
--- !u!114 &{scr}
MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {go}}}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {GUID_KILL_ZONE}, type: 3}}
  m_Name: 
  m_EditorClassIdentifier: 
""")

    def build(self):
        content = SCENE_HEADER + "".join(self.blocks)
        scene_path = os.path.join(scenes_dir, f"{self.scene_name}.unity")
        meta_path = scene_path + ".meta"

        with open(scene_path, "w", encoding="utf-8") as f:
            f.write(content)

        if not os.path.exists(meta_path):
            guid = uuid.uuid5(uuid.NAMESPACE_DNS, f"firefly.scene.{self.scene_name}").hex
            meta_content = f"""fileFormatVersion: 2
guid: {guid}
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
"""
            with open(meta_path, "w", encoding="utf-8") as f:
                f.write(meta_content)
        print(f"Built scene: {self.scene_name}")

# --- BUILD LEVEL 1 ---
def build_level1():
    b = SceneBuilder("Level1", 1, "Nivel 1 - Cueva Umbría", "Level2")
    b.add_camera_and_environment()
    b.add_level_manager(spawn_x=0, spawn_y=0.5)
    b.add_player(x=0, y=0.5)

    # Platforms
    b.add_platform(0, -0.6, width=6)      # Start platform
    b.add_platform(5.5, 0.8, width=3.5)   # First elevated step
    b.add_crystal(5.5, 2.0)               # Crystal 1

    # Spike gap
    b.add_spikes(8.5, -2.5, count=4)
    b.add_platform(11, 2.0, width=4)      # Platform over gap
    b.add_crystal(11, 3.2)                # Crystal 2

    # Patrolling bat over gap
    b.add_bat(11, 4.2, patrol_dist=2.5, speed=2.0)

    # High step
    b.add_platform(16.5, 1.2, width=3.5)
    b.add_platform(20.5, 3.0, width=3.0)
    b.add_crystal(20.5, 4.2)              # Crystal 3

    # Exit platform
    b.add_platform(25, 1.5, width=5)
    b.add_exit_portal(26, 2.7)

    # Bottom abyss kill zone
    b.add_kill_zone(y=-10, width=80)
    b.build()

# --- BUILD LEVEL 2 ---
def build_level2():
    b = SceneBuilder("Level2", 2, "Nivel 2 - El Nido del Eco", "Level3")
    b.add_camera_and_environment()
    b.add_level_manager(spawn_x=0, spawn_y=0.5)
    b.add_player(x=0, y=0.5)

    # Platform 1
    b.add_platform(0, -0.6, width=5)
    b.add_platform(4.5, 1.2, width=3)
    b.add_crystal(4.5, 2.4)               # Crystal 1

    # Large spike pit
    b.add_spikes(7, -3.5, count=7)

    # Moving platform across pit
    b.add_moving_platform(7.5, 1.5, offset_x=4.5, offset_y=0, speed=2.2)
    b.add_bat(9.5, 3.2, patrol_dist=2.8, speed=2.5) # Bat guarding chasm

    # Intermediate ledge
    b.add_platform(15, 1.5, width=4)
    b.add_crystal(15, 2.7)                # Crystal 2

    # Low spikes hazard
    b.add_spikes(18, -1.0, count=3)
    b.add_platform(20.5, 3.2, width=3)
    b.add_crystal(20.5, 4.4)              # Crystal 3

    # Bat 2
    b.add_bat(22, 2.2, patrol_dist=3.0, speed=2.8)

    # Final ledge
    b.add_platform(25, 1.0, width=3.5)
    b.add_crystal(25, 2.2)                # Crystal 4

    # Exit altar
    b.add_platform(29.5, 1.0, width=5)
    b.add_exit_portal(30.5, 2.2)

    b.add_kill_zone(y=-10, width=90)
    b.build()

# --- BUILD LEVEL 3 ---
def build_level3():
    b = SceneBuilder("Level3", 3, "Nivel 3 - El Abismo de Cristal", "VictoryScene")
    b.add_camera_and_environment()
    b.add_level_manager(spawn_x=0, spawn_y=0.5)
    b.add_player(x=0, y=0.5)

    # Base platform
    b.add_platform(0, -0.6, width=5)

    # Massive abyss of spikes below entire level
    b.add_spikes(4, -5.5, count=14)

    # Ledge 1
    b.add_platform(4.5, 0.8, width=3)
    b.add_crystal(4.5, 2.0)               # Crystal 1

    # Vertical Moving platform
    b.add_moving_platform(8.5, 1.0, offset_x=0, offset_y=3.5, speed=2.4)
    b.add_bat(8.5, 5.2, patrol_dist=2.0, speed=2.2)

    # High ledge 2
    b.add_platform(12, 4.8, width=3.5)
    b.add_crystal(12, 6.0)                # Crystal 2

    # Mid descent platform
    b.add_platform(16, 2.8, width=3)
    b.add_crystal(16, 4.0)                # Crystal 3

    # Horizontal moving platform across deep cavern
    b.add_moving_platform(20, 3.2, offset_x=4.0, offset_y=0, speed=2.5)
    b.add_bat(22, 4.5, patrol_dist=3.0, speed=3.0) # Fast Bat 2

    # Upper ascent
    b.add_platform(26.5, 4.2, width=3)
    b.add_crystal(26.5, 5.4)              # Crystal 4

    b.add_bat(28.5, 6.8, patrol_dist=2.5, speed=2.8) # Bat 3

    # Final high chamber
    b.add_platform(30.5, 6.5, width=3)
    b.add_crystal(30.5, 7.7)              # Crystal 5 (final crystal!)

    # Exit Portal to freedom!
    b.add_platform(35, 6.5, width=5)
    b.add_exit_portal(36, 7.7)

    b.add_kill_zone(y=-10, width=100)
    b.build()

if __name__ == "__main__":
    build_level1()
    build_level2()
    build_level3()
