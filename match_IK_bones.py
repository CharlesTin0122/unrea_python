import unreal

# 骨骼匹配的字典
bones_to_match = {
    "ik_foot_root": "root",
    "ik_foot_l": "foot_l",
    "ik_foot_r": "foot_r",
    "ik_hand_root": "root",
    "ik_hand_gun": "hand_r",
    "ik_hand_l": "hand_l",
    "ik_hand_r": "hand_r",
}

# 载入要使用的类库
editor_util_lib = unreal.EditorUtilityLibrary()
anim_lib = unreal.AnimationLibrary()
anim_data_ctrler = unreal.AnimationDataController()
editor_util_lib = unreal.EditorUtilityLibrary()
anim_pose_ext = unreal.AnimPoseExtensions()
skeleton_modifier = unreal.SkeletonModifier()

# 存放位移旋转和缩放逐帧数值的列表
positional_keys = []
rotational_keys = []
scaling_keys = []


for source_bone_name, target_bone_name in bones_to_match.items():
    # 获取当前所选择的资产
    selected_assets = editor_util_lib.get_selected_assets()
    if not selected_assets:
        unreal.log("No assets selected.")
    # 遍历资产
    for asset in selected_assets:
        if isinstance(asset, unreal.AnimSequence):
            assert isinstance(asset, unreal.AnimSequence)
            # 获取当前的动画序列帧数
            num_frames = anim_lib.get_num_frames(asset)
            # 获取目标骨骼的父骨骼
            target_parent_bone_name = anim_lib.find_bone_path_to_root(
                asset, target_bone_name
            )[1]
            # 遍历所有帧
            for frame in range(num_frames - 1):
                # 获取当前帧的Pose
                evaluation_options = unreal.AnimPoseEvaluationOptions(
                    unreal.AnimDataEvalType.RAW, True, False, True, None, True, True
                )
                current_pose = anim_pose_ext.get_anim_pose_at_frame(
                    asset, frame, evaluation_options
                )
                # 获取源骨骼相对于目标骨骼父骨骼的变换
                relative_transform = anim_pose_ext.get_relative_transform(
                    current_pose,
                    source_bone_name,
                    target_parent_bone_name,
                    unreal.AnimPoseSpaces.WORLD,
                )
                # 填充位移旋转和缩放动画数值的列表
                positional_keys.append(relative_transform.translation)
                rotational_keys.append(relative_transform.rotation)
                scaling_keys.append(relative_transform.scale3d)
    # 设置骨骼动画
    anim_data_ctrler.set_bone_track_keys(
        target_bone_name, positional_keys, rotational_keys, scaling_keys
    )
unreal.load_asset
