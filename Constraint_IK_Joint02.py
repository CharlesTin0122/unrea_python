import unreal

# 骨骼匹配的字典
bone_match_dict = {
    "ik_foot_l": "foot_l",
    "ik_foot_r": "foot_r",
    "ik_hand_gun": "hand_r",
    "ik_hand_l": "hand_l",
    "ik_hand_r": "hand_r",
}

# 虚幻类的实例化
editor_util_lib = unreal.EditorUtilityLibrary()
anim_lib = unreal.AnimationLibrary()
anim_pose_ext = unreal.AnimPoseExtensions()
MathLibrary = unreal.MathLibrary()
AnimDataCtrler = unreal.AnimationDataController()

# 存放位移旋转和缩放逐帧数值的列表
positional_keys: list[unreal.Vector] = []
rotational_keys: list[unreal.Quat] = []
scaling_keys: list[unreal.Vector] = []


def get_relative_transform_at_frame(
    asset, frame_index, source_bone_name, target_parent_bone
):
    """
    获取指定帧的源骨骼相对于目标骨骼父骨骼的变换
    Args:
        asset (unreal.AnimSequence): 动画资产
        frame_index (int): 帧索引
        source_bone_name (str): 源骨骼名称
        target_parent_bone (str): 目标骨骼父骨骼名称
    Returns:
        unreal.Transform: 源骨骼相对于目标骨骼父骨骼的变换
    """
    anim_pose = anim_pose_ext.get_anim_pose_at_frame(asset, frame_index)
    relative_transform = anim_pose_ext.get_relative_transform(
        anim_pose,
        target_parent_bone,
        source_bone_name,
        unreal.AnimPoseSpaces.WORLD,
    )
    return relative_transform


def process_asset(asset, source_bone_name, target_bone_name):
    """
    处理单个动画资产，更新骨骼动画
    Args:
        asset (unreal.AnimSequence): 动画资产
        source_bone_name (str): 源骨骼名称
        target_bone_name (str): 目标骨骼名称
    """
    # 获取动画帧数
    anim_frames_num = anim_lib.get_num_frames(asset)
    # 获取目标骨骼的父骨骼
    target_parent_bone = anim_lib.find_bone_path_to_root(asset, target_bone_name)[1]

    # 存储逐帧的位移、旋转、缩放数据
    positional_keys.clear()
    rotational_keys.clear()
    scaling_keys.clear()

    # 遍历所有帧并获取相对变换
    for frame_index in range(anim_frames_num):
        relative_transform = get_relative_transform_at_frame(
            asset, frame_index, source_bone_name, target_parent_bone
        )
        positional_keys.append(relative_transform.translation)
        rotational_keys.append(relative_transform.rotation)
        scaling_keys.append(relative_transform.scale3d)

    # 更新骨骼动画
    AnimDataCtrler.set_bone_track_keys(
        target_bone_name, positional_keys, rotational_keys, scaling_keys
    )


def constraint_IK_joints(source_bone_name, target_bone_name):
    """
    Makes the target skeleton completely match the source skeleton
    Args:
        source_bone_name (str): 源骨骼名称
        target_bone_name (str): 目标骨骼名称
    """
    # 获取选中的资产
    sel_assets = editor_util_lib.get_selected_assets()

    # 遍历所有选中的资产
    for asset in sel_assets:
        if not isinstance(asset, unreal.AnimSequence):
            unreal.log_warning(f"{asset.get_name()} is not an AnimSequence")
            continue

        # 处理资产
        process_asset(asset, source_bone_name, target_bone_name)


if __name__ == "__main__":
    # 遍历骨骼匹配的字典并应用IK约束
    for source_bone, target_bone in bone_match_dict.items():
        constraint_IK_joints(source_bone, target_bone)
