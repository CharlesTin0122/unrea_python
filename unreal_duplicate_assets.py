# -*- coding: utf-8 -*-
'''
@FileName      : unreal_duplicate_assets.py
@DateTime      : 2023/11/18 11:46:53
@Author        : Tian Chao
@Contact       : tianchao0533@163.com
@Software      : unreal 4.27
@PythonVersion : python 3.7.7
@Description   :
'''
import os
import time
import unreal

def duplicate_assets(num_dupl: int):
    """
    复制虚幻资产到当前目录

    Args:
        num_dupl (int): 复制资产数量
    """
    # 记录开始时间
    start_time = time.time()

    # 获取虚幻的编辑工具类和资产库类
    editor_util_lib = unreal.EditorUtilityLibrary()
    editor_asset_lib = unreal.EditorAssetLibrary()

    # 获取选中的资产列表和数量
    sel_assets = editor_util_lib.get_selected_assets()
    num_assets = len(sel_assets)

    # 计算要复制的总资产数量，并设置进度条标签
    total_num_dupl = num_assets * num_dupl
    text_label = f"Duplicate {total_num_dupl} assets..."
    running = True

    # 创建进度条对话框，范围缓慢任务，参数1遍历总数量，参数2进度条标签
    with unreal.ScopedSlowTask(total_num_dupl, text_label) as slow_task:
        slow_task.make_dialog(True) # 如果当前没有打开对话框，则为此慢速任务创建一个新对话框

        # 遍历选中的资产列表
        for asset in sel_assets:
            assert isinstance(asset, unreal.Object)

            # 获取资产的名称、类名、路径
            asset_name = asset.get_name()
            asset_class_name = asset.get_class().get_name()
            asset_path = asset.get_path_name()

            # 获取资产所在目录的路径
            source_path = os.path.dirname(asset_path)

            # 复制指定数量的资产
            for i in range(num_dupl):
                # 如果用户要求取消慢速任务
                if slow_task.should_cancel():
                    running = False
                    break

                # 更新进度条，每次遍历更新进度为1。
                slow_task.enter_progress_frame(1)

                # 生成新的资产名称和目标路径
                new_name = f"{asset_name}_{i}"
                dest_path = os.path.join(source_path, new_name).replace("\\", "/")

                # 复制资产
                dupl_assets = editor_asset_lib.duplicate_asset(asset_path, dest_path)

                # 更新进度条
                slow_task.enter_progress_frame(1)

                # 检查复制是否成功
                if dupl_assets is None:
                    unreal.log_warning(f"Failed to duplicate {new_name}, maybe already exists.")

            # 如果进度条被取消，则停止复制资产
            if not running:
                break

        # 记录结束时间，并打印复制完成信息
        end_time = time.time()
        unreal.log(f"Duplicated {total_num_dupl} assets in {end_time - start_time:.2f} seconds.")  # :.2f 保留两位小数的浮点数


if __name__ == "__main__":
    duplicate_assets(5)
