import unreal

# 访问骨骼和权重
mesh_path = "/Game/Monster/Mummy_01/SK_Monster_Mummy_Sword_01"
asset_editor = unreal.EditorAssetLibrary()
skel_mesh = asset_editor.load_asset(mesh_path)

# 加载权重修饰符
weight_modifier = unreal.SkinWeightModifier()
# 加载骨架修饰符
skeleton_modifier = unreal.SkeletonModifier()

# 创建a和b两根骨骼

skeleton_modifier.set_skeletal_mesh(skel_mesh)
# skeleton_modifier.add_bones(
#     ["a", "b"], ["root", "root"], [unreal.Transform(), unreal.Transform()]
# )

# 将骨骼b设为骨骼a的父级
# skeleton_modifier.parent_bone("b", "a")

# 批量修改骨骼名称
all_bone_names = skeleton_modifier.get_all_bone_names()
for bone_name in all_bone_names:
    bone_name_str = str(bone_name)
    new_bone_name = bone_name_str.replace("-", "_")

    if new_bone_name != bone_name_str and new_bone_name not in [
        str(n) for n in all_bone_names
    ]:
        skeleton_modifier.rename_bone(bone_name, new_bone_name)
    else:
        unreal.log_warning(f"Skipping rename for {bone_name_str} to {new_bone_name}")

# 提交更改
skeleton_modifier.commit_skeleton_to_skeletal_mesh()
