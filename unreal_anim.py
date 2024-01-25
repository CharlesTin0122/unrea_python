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
skeleton_asset_path = r'/Game/Maps/Test/FHY/mod1Weapon/AnimSequence/CrossBow_Stand_Aim_Fire_To_Relax_IPC_mod1'
skeleton_asset = unreal.load_object(None, skeleton_asset_path, unreal.AnimSequence)

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






'''在Unreal Python API 中有办法修改动画资产中的骨骼位置么？比如让一个骨骼完全跟随另一个骨骼，如果有的话，应该怎么写脚本？'''


# 获取要修改的骨骼的引用
skeleton = unreal.Skeleton()
skeleton_asset = unreal.SkeletonAsset()
skeleton_asset.skeleton = skeleton

# 获取要跟随的骨骼的引用
follow_bone_name = "BoneToFollow"
follow_bone_index = skeleton_asset.get_bone_index(follow_bone_name)

# 获取要修改的骨骼的引用
target_bone_name = "BoneToModify"
target_bone_index = skeleton_asset.get_bone_index(target_bone_name)

# 获取动画资产的所有骨骼
animation_assets = unreal.AnimationAsset().get_all_animation_assets()

# 遍历所有动画资产，并修改骨骼位置
for animation_asset in animation_assets:
    animation_sequence = animation_asset.get_editor_property("sequence")
    if animation_sequence:
        # 获取动画序列的轨道
        bone_track = animation_sequence.find_track(target_bone_index)
        if bone_track:
            # 获取轨道上的关键帧
            bone_track_keys = bone_track.get_editor_property("pos_keys")
            for key in bone_track_keys:
                # 获取跟随骨骼的位置
                follow_bone_transform = skeleton_asset.get_ref_pose_transform(follow_bone_index)
                # 设置目标骨骼的位置为跟随骨骼的位置
                key.position = follow_bone_transform.translation

# 保存修改后的动画资产
unreal.EditorAssetLibrary.save_loaded_asset(animation_assets)
