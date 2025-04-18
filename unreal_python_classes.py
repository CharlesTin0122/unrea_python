import unreal

# 虚幻类的实例化

sys_lib = unreal.SystemLibrary()
# 编辑器工具类
editor_util_lib = unreal.EditorUtilityLibrary()
# 资产管理类
asset_editor = unreal.EditorAssetLibrary()


# 蒙皮权重修饰类
weight_modifier = unreal.SkinWeightModifier()
# 骨骼修饰类
skeleton_modifier = unreal.SkeletonModifier()
# 骨骼网格体管理类
skeletal_mesh_library = unreal.EditorSkeletalMeshLibrary()
# AnimationLibrary 是一个静态库，提供了一系列用于操作和查询动画数据的实用函数。
# 它主要用于在蓝图（Blueprints）或Python脚本中执行与动画相关的通用操作，而无需直接修改动画资产。
anim_lib = unreal.AnimationLibrary()
# AnimationDataController 是一个专门用于控制和修改动画数据的类，通常用于编辑器中对动画序列（Animation Sequence）的直接编辑。
# 它提供了对动画数据的低级别访问，允许用户动态修改动画的骨骼轨迹、帧数据等。
AnimDataCtrler = unreal.AnimationDataController()

anim_pose_ext = unreal.AnimPoseExtensions()
MathLibrary = unreal.MathLibrary()
AnimDataCtrler.set_bone_track_keys()

dir(AnimDataCtrler)
# 数学类
MathLibrary = unreal.MathLibrary()
# 字符串类
string_lib = unreal.StringLibrary()
string_lib.replace("Cherles", "e", "a", SearchCase=unreal.SearchCase.CASE_SENSITIVE)
string_lib.contains("Charles", "a")
