import unreal


def add_prefix():
    """资产批量增加前缀"""
    # instance of unreal classes
    editor_util_lib = unreal.EditorUtilityLibrary()
    system_lib = unreal.SystemLibrary()

    # prefix mapping
    prefix_mapping = {
        "StaticMesh": "SM_",
        "Skeleton": "SK_",
        "SkeletalMesh": "SK_",
        "AnimSequence": "AS_",
        "AnimMontage": "AM_",
        "Texture2D": "T_",
        "Material": "M_",
        "Blueprint": "BP_",
        "MaterialInstanceConstant": "MI_",
        "MaterialFunction": "MF_",
        "AnimBlueprint": "AB_",
    }
    # get selected assets
    sel_assets = editor_util_lib.get_selected_assets()
    prefixed = 0
    # 遍历所有资产
    for asset in sel_assets:
        # 获取资产名称(字符串)
        asset_name = system_lib.get_object_name(asset)
        # 获取资产类名称
        asset_class = asset.get_class()
        class_name = asset_class.get_name()
        unreal.log(f"{asset_name} with class {class_name}")
        # 通过类名称获取前缀，如果没有则返回None
        class_prefix = prefix_mapping.get(class_name, None)
        # 如果前缀为空,则跳过
        if class_prefix is None:
            unreal.log_warning(f"No mapping for asset{asset_name} of type{class_name}")
            continue
        # 如果资产名称没有使用正确的前缀，则用正确的前缀重命名资产
        if not asset_name.startswith(class_prefix):
            new_name = class_prefix + asset_name
            editor_util_lib.rename_asset(asset, new_name)
            prefixed += 1
            unreal.log(
                f"Prefixed {asset_name} of type {class_name} with {class_prefix}"
            )
        else:
            unreal.log(
                f"Asset {asset_name} of type {class_name} is already prefixed with {class_prefix}"
            )

    unreal.log(f"Prefixed {prefixed} of {class_name} assets")


if __name__ == "__main__":
    add_prefix()
