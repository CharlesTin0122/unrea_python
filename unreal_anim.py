# -*- coding: utf-8 -*-
"""
@FileName      : unreal_anim.py
@DateTime      : 2023/10/25 16:20:43
@Author        : Tian Chao
@Contact       : tianchao0533@163.com
@Software      : Maya 2023.3
@PythonVersion : python 3.9.7
@Description   :
"""
import unreal

myanim = unreal.load_asset("/Game/LA_MOVING_TEST2")  # Load animation sequence asset
obj_loc = unreal.Vector(-7800, -900, 200)
obj_anim = unreal.EditorLevelLibrary.spawn_actor_from_object(
    myanim, obj_loc, (0.0, -90, 0)
)  # Spawn animation into game world (Editor)
SK = obj_anim.skeletal_mesh_component  # Get skeletal mesh reference
playRate = 1
animTime = 0.1
SK.set_position(animTime, True)
SK.override_animation_data(
    myanim, True, True, animTime, playRate
)  # Set position within animation sequence
bone_loc = SK.get_socket_location("rig_LeftFoot")  # Get bone location
print(
    "Animation time: " + str(animTime) + "- Left bone world location: " + str(bone_loc)
)
unreal.EditorLevelLibrary.destroy_actor(
    obj_anim
)  # Destroy spawned animation in Editor.


"""请用unreal Python API帮我写一个脚本，该脚本用于处理动画资产中的骨骼位置"""

# 获取要处理的骨骼动画资产的引用
skeleton_asset_path = "/Game/Path/To/Your/SkeletonAsset"
skeleton_asset = unreal.load_object(None, skeleton_asset_path, unreal.UAnimSequence)

# 获取骨骼的引用
skeleton = skeleton_asset.get_skeleton()

# 获取要处理的骨骼名称
bone_name = "YourBoneName"

# 获取骨骼的引用
bone = skeleton.get_bone_by_name(bone_name)

if bone:
    # 获取骨骼的初始位置
    initial_transform = skeleton.get_ref_local_pose()[bone.bone_index]

    # 修改骨骼的位置
    new_transform = initial_transform
    new_location = unreal.Vector(100.0, 0.0, 0.0)  # 新的位置坐标
    new_transform.translation = new_location

    # 将修改后的位置应用到骨骼
    skeleton.set_ref_local_pose_for_sequential_evaluation(
        bone.bone_index, new_transform
    )
    skeleton.mark_bone_translation_mirrored(bone.bone_index, True)

    # 保存修改
    unreal.EditorAssetLibrary.save_asset(skeleton_asset)

    print(f"骨骼 {bone_name} 的位置已修改为 {new_location}")

else:
    print(f"无法找到骨骼 {bone_name}")


"""请用unreal Python API帮我写一个脚本，该脚本用于处理动画资产中的骨骼位置，处理方法是逐帧对齐两个骨骼的位置和旋转。"""

# 获取要处理的骨骼动画资产的引用
skeleton_asset_path = "/Game/Path/To/Your/SkeletonAsset"
skeleton_asset = unreal.load_object(None, skeleton_asset_path, unreal.UAnimSequence)

# 获取骨骼的引用
skeleton = skeleton_asset.get_skeleton()

# 获取第一个骨骼的名称
bone_name1 = "Bone1Name"
bone1 = skeleton.get_bone_by_name(bone_name1)

# 获取第二个骨骼的名称
bone_name2 = "Bone2Name"
bone2 = skeleton.get_bone_by_name(bone_name2)

if bone1 and bone2:
    # 获取动画序列的帧数
    frame_count = unreal.SequencerTools.get_animation_length(skeleton_asset)

    # 遍历每一帧
    for frame in range(frame_count):
        # 获取第一个骨骼的位置和旋转
        bone1_transform = skeleton.get_animation_pose(bone1, frame)

        # 获取第二个骨骼的位置和旋转
        bone2_transform = skeleton.get_animation_pose(bone2, frame)

        # 对齐第二个骨骼到第一个骨骼的位置和旋转
        new_transform = bone1_transform
        new_transform.translation = bone2_transform.translation
        new_transform.rotation = bone2_transform.rotation

        # 将修改后的位置和旋转应用到第二个骨骼
        skeleton.set_animation_pose(bone2, frame, new_transform)

    # 保存修改
    unreal.EditorAssetLibrary.save_asset(skeleton_asset)

    print(f"骨骼 {bone_name2} 已对齐到骨骼 {bone_name1} 的位置和旋转")

else:
    print("无法找到一个或两个骨骼")
