# -*- coding: utf-8 -*-
"""
@FileName      : tc_test.py
@DateTime      : 2023/10/19 10:25:56
@Author        : Tian Chao
@Contact       : tianchao0533@163.com
@Software      : Maya 2023.3
@PythonVersion : python 3.9.7
@Description   :
"""
import unreal
import os


def get_method():
    obj = unreal.load_asset(
        "/Game/Mannequin/Animation/Sword2h/Attack/Stand/skill/Anim_human_skill_2h_axe_001"
    )
    for attr in dir(obj):
        print(attr)


def list_asset_paths():
    """列出路径下所有文件

    Args:
        asset_path (str): 虚幻路径
    """
    for asset in unreal.EditorAssetLibrary.list_assets(
        r"/Game/Characters/Mannequins/Meshes"
    ):
        print(asset)


def get_selection_content_browser():
    """获取选中的内容"""
    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for asset in selected_assets:
        print(asset)


def get_all_actors():
    """获取所有的actor"""
    actors = unreal.EditorActorSubsystem().get_all_level_actors()
    for actor in actors:
        print(actor)


def get_selected_actors():
    selected_actors = unreal.EditorActorSubsystem().get_selected_level_actors()
    for actor in selected_actors:
        print(actor)


def get_asset_class(class_type):
    """路径下获得所有指定类型文件

    Args:
        class_type (str): 资产类(
            'StaticMesh',
            'Texture2D',
            'Skeleton',
            'SkeletalMesh',
            'AnimSequence',
            'AnimMontage',
            ...
            )

    Returns:
        _type_: list(object)
    """
    asset_path = unreal.EditorAssetLibrary.list_assets(
        r"/Game/Mannequin/Animation/Unarm/Idles"
    )
    assets = []
    for path in asset_path:
        asset_data = unreal.EditorAssetLibrary.find_asset_data(path)
        asset_class = asset_data.asset_class
        if asset_class == class_type:
            assets.append(asset_data.get_asset())
    for asset in assets:
        print(asset)
    return assets


mesh_list = get_asset_class("AnimSequence")


# use unreal python API to import asset
def import_asset(fbx_list):
    # 创建资产工具对象
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    # 创建资产导入数据对象
    asset_import_data = unreal.AutomatedAssetImportData()
    # 设置属性
    asset_import_data.destination_path = (
        r"/Game/Mannequin/Character/Unreal/Mesh"  # 设置目标路径
    )
    asset_import_data.filenames = fbx_list  # 设置导入文件名
    asset_tools.import_assets_automated(asset_import_data)  # 执行导入


asset_list = [
    r"D:\Work\SkeletonMesh\Export\Human_male_cloth_helmate_A001.fbx",
    r"D:\Work\SkeletonMesh\Export\Human_male_cloth_upper_A002.fbx",
    r"D:\Work\SkeletonMesh\Export\Human_male_cloth_lower_A003.fbx",
]
import_asset(asset_list)


# use unreal python API to export asset
def export_asset(asset_path):
    # 获取选中的对象
    sel_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    # 遍历这些对象
    for sel_asset in sel_assets:
        # 获取对象名称生成导出文件名称
        asset_name = sel_asset.get_name() + ".fbx"
        # 创建资产导出任务，并指定任务属性
        export_task = unreal.AssetExportTask()
        export_task.automated = True  # 自动化（无人留守导出）
        export_task.filename = os.path.join(asset_path, asset_name)  # 指定导出文件名
        export_task.object = sel_asset  # 指定导出对象
        export_task.prompt = False  # 是否快速导出（允许对话框提示）

        # 如果对象为骨骼模型
        if isinstance(sel_asset, unreal.SkeletalMesh):
            # 创建具体的导出器
            export_task.options = unreal.FbxExportOption()
            fbx_exporter = unreal.SkeletalMeshExporterFBX()  # 创建骨骼模型导出器
            export_task.exporter = fbx_exporter  # 为导出任务指定导出器
            fbx_exporter.run_asset_export_task(export_task)  # 导出器执行导出

        if isinstance(sel_asset, unreal.StaticMesh):
            export_task.options = unreal.FbxExportOption()
            fbxExporter = unreal.StaticMeshExporterFBX()
            export_task.exporter = fbxExporter
            fbxExporter.run_asset_export_task(export_task)
        # export textures
        if isinstance(sel_asset, unreal.Texture):
            asset_name = sel_asset.get_name() + ".tga"
            export_task.filename = os.path.join(asset_path, asset_name)
            tgaExporter = unreal.TextureExporterTGA()
            export_task.exporter = tgaExporter
            tgaExporter.run_asset_export_task(export_task)


if __name__ == "__main__":
    export_asset(r"D:\Work\Test")


def slow_task():
    """如果你的脚本需要在同一个操作中处理多个资源或Actor，可能需要较长的时间才能完成。
    但是，当虚幻编辑器运行Python脚本时，其UI处于被封锁状态中，不允许其他的用户交互。
    为了向用户提供大型任务的进度信息，从而避免使编辑器让用户产生冻结或挂起的错觉，可以使用`unreal.ScopedSlowTask`范围。
    """
    total_frames = 100
    text_label = "Working!"
    with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
        slow_task.make_dialog(True)  # 如果对话不可见，使其可见
        for i in range(total_frames):
            if slow_task.should_cancel():  # 如果用户已在UI中按了"取消（Cancel）"则为True
                break
            slow_task.enter_progress_frame(1)  # 使进度前进一帧。
            # 如果希望，也可以更新本调用中的对话文本。
            ...  # 现在在此处执行针对当前帧的工作！


unreal.EditorSkeletalMeshLibrary

a = unreal.AnimationLibrary()
unreal.log(dir(a))
[
    "__class__",
    "__delattr__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "_post_init",
    "_wrapper_meta_data",
    "add_animation_notify_event",
    "add_animation_notify_event_object",
    "add_animation_notify_state_event",
    "add_animation_notify_state_event_object",
    "add_animation_notify_track",
    "add_animation_sync_marker",
    "add_curve",
    "add_float_curve_key",
    "add_float_curve_keys",
    "add_meta_data",
    "add_meta_data_object",
    "add_transformation_curve_key",
    "add_transformation_curve_keys",
    "add_vector_curve_key",
    "add_vector_curve_keys",
    "add_virtual_bone",
    "call_method",
    "cast",
    "contains_meta_data_of_class",
    "copy_anim_notifies_from_sequence",
    "does_bone_name_exist",
    "does_curve_exist",
    "finalize_bone_animation",
    "find_bone_path_to_root",
    "get_additive_animation_type",
    "get_additive_base_pose_type",
    "get_anim_notify_event_trigger_time",
    "get_animation_curve_names",
    "get_animation_interpolation_type",
    "get_animation_notify_event_names",
    "get_animation_notify_events",
    "get_animation_notify_events_for_track",
    "get_animation_notify_track_names",
    "get_animation_sync_markers",
    "get_animation_sync_markers_for_track",
    "get_animation_track_names",
    "get_bone_compression_settings",
    "get_bone_pose_for_frame",
    "get_bone_pose_for_time",
    "get_bone_poses_for_frame",
    "get_bone_poses_for_time",
    "get_class",
    "get_curve_compression_settings",
    "get_default_object",
    "get_editor_property",
    "get_float_keys",
    "get_fname",
    "get_frame_at_time",
    "get_full_name",
    "get_meta_data",
    "get_meta_data_of_class",
    "get_name",
    "get_num_frames",
    "get_outer",
    "get_outermost",
    "get_path_name",
    "get_rate_scale",
    "get_raw_track_data",
    "get_raw_track_position_data",
    "get_raw_track_rotation_data",
    "get_raw_track_scale_data",
    "get_root_motion_lock_type",
    "get_sequence_length",
    "get_time_at_frame",
    "get_transformation_keys",
    "get_typed_outer",
    "get_unique_marker_names",
    "get_vector_keys",
    "get_world",
    "is_root_motion_enabled",
    "is_root_motion_lock_forced",
    "is_valid_anim_notify_track_name",
    "is_valid_animation_sync_marker_name",
    "is_valid_raw_animation_track_name",
    "is_valid_time",
    "modify",
    "remove_all_animation_notify_tracks",
    "remove_all_animation_sync_markers",
    "remove_all_bone_animation",
    "remove_all_curve_data",
    "remove_all_meta_data",
    "remove_all_virtual_bones",
    "remove_animation_notify_events_by_name",
    "remove_animation_notify_events_by_track",
    "remove_animation_notify_track",
    "remove_animation_sync_markers_by_name",
    "remove_animation_sync_markers_by_track",
    "remove_bone_animation",
    "remove_curve",
    "remove_meta_data",
    "remove_meta_data_of_class",
    "remove_virtual_bone",
    "remove_virtual_bones",
    "rename",
    "replace_anim_notifies",
    "replace_anim_notify_states",
    "set_additive_animation_type",
    "set_additive_base_pose_type",
    "set_animation_interpolation_type",
    "set_bone_compression_settings",
    "set_curve_compression_settings",
    "set_editor_properties",
    "set_editor_property",
    "set_is_root_motion_lock_forced",
    "set_rate_scale",
    "set_root_motion_enabled",
    "set_root_motion_lock_type",
    "static_class",
    "write_anim_bone_trans_forms",
]
