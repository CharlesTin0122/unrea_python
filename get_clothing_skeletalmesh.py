# -*- coding: utf-8 -*-
'''
@FileName      : get_clothing_skeletalmesh.py
@DateTime      : 2024/01/25 16:27:50
@Author        : Tian Chao
@Software      : Unreal 4.27
@PythonVersion : python 3.7.7
@Description   : 取项目路径下所有带有布料信息的骨骼网格体
'''

import unreal


def get_clothing_assets(unreal_path:str):
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
    # 遍历路径下所有资产
    for path in asset_path:
        # 通过资产路径获得资产数据
        asset_data = unreal.EditorAssetLibrary.find_asset_data(path)
        # 通过资产数据获得资产类
        asset_class = asset_data.asset_class
        # 判断资产类是否匹配实参提供的类
        if asset_class == "SkeletalMesh":
            # 通过资产数据获得资产本身
            skeletal_asset = asset_data.get_asset()
            # 如果该资产有布料信息
            if skeletal_asset.mesh_clothing_assets:
                # 如果是，则将资产添加到列表
                assets.append(skeletal_asset)
    # 返回所有获得的对象列表
    return assets

if __name__ == '__main__':
    path01 = r'/Game/Mannequin/Equipment/Cloth_WJ/Cloth_WJ_Male'
    mesh_list = get_clothing_assets(path01)
    for mesh in mesh_list:
        print(mesh)