import unreal

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

for soure_bone_name, target_bone_name in bones_to_match.items():
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
            # 遍历所有帧
            for frame in range(num_frames - 1):
                # 获取当前帧的Pose
                evaluation_options = unreal.AnimPoseEvaluationOptions(
                    unreal.AnimDataEvalType.RAW, True, False, True, None, True, True
                )
                current_pose = anim_pose_ext.get_anim_pose_at_frame(
                    asset, frame, evaluation_options
                )
                anim_pose_ext.get_relative_transform(
                    current_pose, "root", "hand_r", unreal.AnimPoseSpaces.WORLD
                )
                asset.get_skeleton()
