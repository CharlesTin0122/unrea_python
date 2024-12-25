# -*- coding: utf-8 -*-
"""
@FileName      : get_clothing_skeletalmesh.py
@DateTime      : 2024/01/25 16:27:50
@Author        : Tian Chao
@Software      : Unreal 4.27
@PythonVersion : python 3.7.7
@Description   : 取项目路径下所有带有布料信息的骨骼网格体
"""

import unreal


def get_clothing_assets(unreal_path: str):
    """获取项目路径下所有带有布料信息的骨骼网格体

    Args:
        unreal_path (str): 项目路径

    Returns:
        list: 带有布料信息的骨骼网格体列表
    """
    # 获取路径下所有资产路径
    asset_path = unreal.EditorAssetLibrary.list_assets(unreal_path)
    # 设置变量以接受结果
    assets = []

    # 设置进度条对话框参数
    total_asset_num = len(asset_path)
    text_label = f"Check {total_asset_num} assets..."
    running = True

    # 创建进度条对话框，范围缓慢任务，参数1遍历总数量，参数2进度条标签
    with unreal.ScopedSlowTask(total_asset_num, text_label) as slow_task:
        slow_task.make_dialog(
            True
        )  # 如果当前没有打开对话框，则为此慢速任务创建一个新对话框

        # 遍历路径下所有资产
        for path in asset_path:
            # 通过资产路径获得资产数据
            asset_data = unreal.EditorAssetLibrary.find_asset_data(path)
            # 通过资产数据获得资产类
            asset_class = asset_data.asset_class

            # 如果用户已在UI中按了"取消（Cancel）"则为True
            if slow_task.should_cancel():
                running = False
                break
            # 更新进度条，每次遍历更新进度为1。
            slow_task.enter_progress_frame(1)

            # 判断资产类是否匹配实参提供的类
            if asset_class == "SkeletalMesh":
                # 通过资产数据获得资产本身
                skeletal_asset = asset_data.get_asset()
                # 如果该资产有布料信息
                if skeletal_asset.mesh_clothing_assets:
                    # 如果是，则将资产添加到列表
                    assets.append(skeletal_asset)

            # 如果进度条被取消，则停止复制资产
            if not running:
                break
    # 返回所有获得的对象列表
    return assets


if __name__ == "__main__":
    path01 = r"/Game/Mannequin/Equipment"
    mesh_list = get_clothing_assets(path01)
    for mesh in mesh_list:
        print(mesh)
