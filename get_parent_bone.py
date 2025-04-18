import unreal


#  1. 使用 Skeleton 获取骨骼层次信息
def get_parent_bone_name(asset, bone_name):
    """
    通过骨骼名称获取父骨骼的名称
    Args:
        asset (unreal.AnimSequence): 动画资产
        bone_name (str): 目标骨骼名称
    Returns:
        str: 父骨骼名称（如果存在），否则返回 None
    """
    skeleton = asset.get_skeleton()  # 获取动画资产的 Skeleton
    if skeleton:
        parent_bone_index = skeleton.get_parent_index(bone_name)  # 获取父骨骼索引
        if parent_bone_index != -1:  # 如果有父骨骼
            return skeleton.get_bone_name(parent_bone_index)  # 返回父骨骼的名称
    return None  # 如果没有父骨骼或骨骼名称无效


# 2. 使用骨骼索引操作
def get_parent_bone_name_via_index(asset, bone_name):
    """
    使用骨骼索引获取父骨骼名称
    Args:
        asset (unreal.AnimSequence): 动画资产
        bone_name (str): 目标骨骼名称
    Returns:
        str: 父骨骼名称（如果存在）
    """
    skeleton = asset.get_skeleton()
    if skeleton:
        bone_index = skeleton.get_bone_index(bone_name)
        if bone_index != -1:
            parent_index = skeleton.get_parent_index(bone_index)
            if parent_index != -1:
                return skeleton.get_bone_name(parent_index)
    return None


# 3. 获取骨骼树结构
def get_bone_hierarchy(asset):
    """
    获取骨骼层次结构
    Args:
        asset (unreal.AnimSequence): 动画资产
    Returns:
        dict: 骨骼到其父骨骼的映射
    """
    skeleton = asset.get_skeleton()
    if not skeleton:
        return {}

    bone_hierarchy = {}
    bone_count = skeleton.get_bone_count()

    for bone_index in range(bone_count):
        bone_name = skeleton.get_bone_name(bone_index)
        parent_index = skeleton.get_parent_index(bone_index)
        parent_name = (
            skeleton.get_bone_name(parent_index) if parent_index != -1 else None
        )
        bone_hierarchy[bone_name] = parent_name

    return bone_hierarchy


# 4. 使用 Reference Skeleton
def get_parent_bone_from_reference_skeleton(asset, bone_name):
    """
    使用 Reference Skeleton 获取父骨骼的名称
    Args:
        asset (unreal.AnimSequence): 动画资产
        bone_name (str): 目标骨骼名称
    Returns:
        str: 父骨骼名称
    """
    skeleton = asset.get_skeleton()
    if not skeleton:
        return None

    reference_skeleton = skeleton.get_reference_skeleton()  # 获取 Reference Skeleton
    bone_index = reference_skeleton.find_bone_index(bone_name)  # 获取骨骼索引

    if bone_index != -1:
        parent_index = reference_skeleton.get_parent_index(bone_index)  # 获取父骨骼索引
        if parent_index != -1:
            return reference_skeleton.get_bone_name(parent_index)  # 返回父骨骼名称
    return None
