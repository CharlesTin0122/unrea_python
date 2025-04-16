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


def constraint_IK_joints(source_bone_name, target_bone_name):
    """
    makes the target skeleton completely match the source skeleton
    Args:
        source_bone_name (str): source_bone_name
        target_bone_name (str): target_bone_name
    """
    # 声明全局变量
    global positional_keys, rotational_keys, scaling_keys
    # 获取选中的资产
    sel_assets = editor_util_lib.get_selected_assets()
    # 遍历所有资产
    for asset in sel_assets:
        # 如果资产不是一个AnimSequence，则跳过
        if not isinstance(asset, unreal.AnimSequence):
            unreal.log_warning(f"{asset.get_name()} is not a AnimSequence")
            continue
        # 断言资产是一个AnimSequence
        assert isinstance(asset, unreal.AnimSequence)
        # 获取动画帧数
        anim_frames_num = anim_lib.get_num_frames(asset)
        # 获取目标骨骼的父骨骼
        target_parent_bone = anim_lib.find_bone_path_to_root(asset, target_bone_name)[1]
        # 遍历所有帧
        for frame_index in range(anim_frames_num):
            # 获取动画姿势
            anim_pose = anim_pose_ext.get_anim_pose_at_frame(asset, frame_index)
            # 获取目标骨骼父骨骼和源骨骼之间的相对变换,也就是源骨骼如果在目标骨骼父骨骼层架之下的话，源骨骼的局部变换
            relative_transform = anim_pose_ext.get_relative_transform(
                anim_pose,
                target_parent_bone,
                source_bone_name,
                unreal.AnimPoseSpaces.WORLD,
            )
            # 将相对变换添加到位移旋转和缩放的列表中
            assert isinstance(relative_transform, unreal.Transform)
            positional_keys.append(relative_transform.translation)
            rotational_keys.append(relative_transform.rotation)
            scaling_keys.append(relative_transform.scale3d)
        # 设置计算完成的骨骼动画，输入参数为要修改动画的骨骼名称和帧动画数组
        AnimDataCtrler.set_bone_track_keys(
            target_bone_name, positional_keys, rotational_keys, scaling_keys
        )
        # 用完清空数组，以备下个循环继续使用
        positional_keys.clear()
        rotational_keys.clear()
        scaling_keys.clear()


if __name__ == "__main__":
    # 遍历骨骼匹配的字典
    for keys, values in bone_match_dict.items():
        constraint_IK_joints(values, keys)
