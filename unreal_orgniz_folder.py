import unreal
import os

# instancees of unreal classes
editor_util_lib = unreal.EditorUtilityLibrary()
sys_lib = unreal.SystemLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()
# get the selecterd assets
sel_assets = editor_util_lib.get_selected_assets()
orgnized = 0
type_name: str = None
# 遍历所有选择的资产
for asset in sel_assets:
    # 获得其路径，名称，类别
    assert isinstance(asset, unreal.Object)
    asset_path = os.path.dirname(asset.get_path_name())
    asset_name = sys_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = asset_class.get_name()
    # 根据类别给资产分组，注意逻辑运算符的使用(and或or)
    if (
        class_name == "StaticMesh"
        or class_name == "SkeletalMesh"
        or class_name == "Skeleton"
        or class_name == "PhysicsAsset"
    ):
        type_name = "mesh"
    elif (
        class_name == "AnimSequence"
        or class_name == "AnimMontage"
        or class_name == "AimOffsetBlendSpace"
        or class_name == "BlendSpace"
    ):
        type_name = "Animation"
    elif class_name == "Texture2D":
        type_name = "Texture"
    elif (
        class_name == "Material"
        or class_name == "MaterialInstanceConstant"
        or class_name == "MaterialFunction"
    ):
        type_name = "Material"
    elif class_name == "Blueprint" or class_name == "AnimBlueprint":
        type_name = "Blueprint"
    elif class_name == "ControlRigBlueprint":
        type_name = "rig"
    elif class_name == "SoundCue" or class_name == "SoundWave":
        type_name = "Sound"
    else:
        type_name = class_name
    # 获取新的路径
    new_path = os.path.join(asset_path, type_name, asset_name)
    try:
        # 从 "内容浏览器 "中重命名已加载的资产。相当于移动操作。将尝试检出文件。
        editor_asset_lib.rename_loaded_asset(asset, new_path)
        orgnized += 1
        unreal.log(f"Orgnized {asset_name} to {new_path}.")
    except Exception as e:
        unreal.log(f"Failed to rename {asset_name} to {new_path}: {e}")
unreal.log(f"Orgnized {orgnized} assets.")
