import unreal


def modify_bone_name(mesh_path: str, search_pattern: str, replace_pattern: str):
    """_summary_

    Args:
        mesh_path (str): 骨骼网格体路径
        search_pattern (str): 查找字段
        replace_pattern (str): 替换字段
    """

    # 加载网格体资产
    asset_editor = unreal.EditorAssetLibrary()
    skel_mesh = asset_editor.load_asset(mesh_path)
    if not skel_mesh:
        unreal.log_error(f"Failed to load skeletal mesh at {mesh_path}")
        return
    if not isinstance(skel_mesh, unreal.SkeletalMesh):
        unreal.log_error(f"Asset at {mesh_path} is not a SkeletalMesh")
        return
    # 加载骨架修饰符
    skeleton_modifier = unreal.SkeletonModifier()
    skeleton_modifier.set_skeletal_mesh(skel_mesh)
    # 加载字符串库
    string_lib = unreal.StringLibrary()

    # 批量修改骨骼名称
    all_bone_names = skeleton_modifier.get_all_bone_names()
    for bone_name in all_bone_names:
        bone_name_str = str(bone_name)
        new_bone_name_str = string_lib.replace(
            bone_name_str, search_pattern, replace_pattern
        )

        if new_bone_name_str != bone_name_str and new_bone_name_str not in [
            str(n) for n in all_bone_names
        ]:
            skeleton_modifier.rename_bone(
                unreal.Name(bone_name_str), unreal.Name(new_bone_name_str)
            )
            unreal.log(f"rename for {bone_name_str} to {new_bone_name_str}")
        else:
            unreal.log_warning(
                f"Skipping rename for {bone_name_str} to {new_bone_name_str}"
            )

    # 提交更改
    try:
        skeleton_modifier.commit_skeleton_to_skeletal_mesh()
        unreal.log("Bone names modified successfully.")
    except Exception as e:
        unreal.log_error(f"Failed to commit skeleton changes: {str(e)}")


if __name__ == "__main__":
    mesh_path = "/Game/Monster/Mummy_01/SK_Monster_Mummy_Sword_01"
    search_pattern = "-"
    replace_pattern = "_"
    modify_bone_name(mesh_path, search_pattern, replace_pattern)
