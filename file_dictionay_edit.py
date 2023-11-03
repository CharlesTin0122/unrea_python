# -*- coding: utf-8 -*-
"""
@FileName      : duplicate_delete_rename.py
@DateTime      : 2023/10/24 15:39:36
@Author        : Tian Chao
@Contact       : tianchao0533@163.com
@Software      : Maya 2023.3
@PythonVersion : python 3.9.7
@Description   :
"""
import unreal

new_dir = "/Game/MyNewDirectory"


def directoryExist():
    """判断目录是否存在"""
    # 判断是否存在，把他打印出来
    print(unreal.EditorAssetLibrary.does_directory_exist(new_dir))
    # 再判断另一个
    print(unreal.EditorAssetLibrary.does_directory_exist(new_dir + "Duplicated"))


def createDirectory():
    """创建目录"""
    return unreal.EditorAssetLibrary.make_directory(new_dir)


def duplicateDirectory():
    """复制目录"""
    return unreal.EditorAssetLibrary.duplicate_directory(
        # 原来目录的名字
        new_dir,
        # 新目录的名字
        new_dir + "Duplicated",
    )


def deleteDirectory():
    """删除目录"""
    return unreal.EditorAssetLibrary.delete_directory(new_dir + "Duplicated")


def renameDirectory():
    """重命名目录"""
    return unreal.EditorAssetLibrary.rename_directory(new_dir, new_dir + "Renamed")


def assetExist(path):
    """文件是否存在"""
    print(unreal.EditorAssetLibrary.does_asset_exist(path + "Duplicated"))


def duplicateAsset(path):
    """复制文件"""
    return unreal.EditorAssetLibrary.duplicate_asset(
        # 原始资源
        path,
        # 复制的名字
        path + "Duplicated",
    )


def deleteAsset(path):
    """删除文件"""
    return unreal.EditorAssetLibrary.delete_asset(path + "Duplicated")


def duplicateAssetDialog(path, show_dialog=True):
    """复制文件的时候出现对话框

    Args:
        path (str): 路径
        show_dialog (bool, optional): 是否出现对话框. Defaults to True.

    Returns:
        _type_: _description_
    """
    # 分解路径
    # 原本/Game/Texture/MyTexture
    # 分解成['/Game/Texture','MyTexture']
    splitted_path = path.rsplit("/", 1)
    # /Game/Texture
    asset_path = splitted_path[0]
    # MyTextureDuplicated
    asset_name = splitted_path[1] + "Duplicated"
    # 带对话框
    if show_dialog:
        return unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset_with_dialog(
            # 名字是被复制出的名字
            asset_name=asset_name,
            # 包的路径
            package_path=asset_path,
            # 原始资源
            original_object=unreal.load_asset(original_asset),
        )
    else:
        return unreal.AssetToolsHelpers.get_asset_tools().duplicate_asset(
            asset_name=asset_name,
            package_path=asset_path,
            original_object=unreal.load_asset(original_asset),
        )


def renameAsset(path):
    """重命名文件"""
    # 原始文件重命名
    unreal.EditorAssetLibrary.rename_asset(path, path + "Renamed")
    # 复制一个出来，重命名
    unreal.EditorAssetLibrary.rename_asset(
        path + "Duplicated", path + "Duplicated" + "Rebaned"
    )


def renameAssetDialog(path, show_dialog=True):
    """带对话框重命名文件"""
    splitted_path = path.rsplit("/", 1)
    asset_path = splitted_path[0]
    asset_name = splitted_path[1]
    rename_data0 = unreal.AssetRenameData(
        asset=unreal.load_asset(path + "Renamed"),
        new_package_path=asset_path,
        new_name=asset_name,
    )

    splitted_path = (path + "Duplicated").rsplit("/", 1)
    asset_path = splitted_path[0]
    asset_name = splitted_path[1]
    rename_data1 = unreal.AssetRenameData(
        asset=unreal.load_asset(path + "Duplicated" + "Renamed"),
        new_package_path=asset_path,
        new_name=asset_name,
    )

    if show_dialog:
        return unreal.AssetToolsHelpers.get_asset_tools().rename_assets_with_dialog(
            assets_and_names=[rename_data0, rename_data1]
        )
    else:
        return unreal.AssetToolsHelpers.get_asset_tools().rename_assets(
            assets_and_names=[rename_data0, rename_data1]
        )


# path：路径
# force_save:强制保存
def saveAsset(path="", force_save=True):
    """文件保存"""
    # https://docs.unrealengine.com/4.26/en-US/PythonAPI/class/EditorAssetLibrary.html?highlight=editorassetlibrary#unreal.EditorAssetLibrary.save_asset
    return unreal.EditorAssetLibrary.save_asset(
        asset_to_save=path, only_if_is_dirty=True
    )


# resursive: 目录下面的目录要不要保存
def saveDirectory(path="", force_save=True, resursive=True):
    """目录保存"""
    return unreal.EditorAssetLibrary.save_directory(
        directory_path=path, only_if_is_dirty=True, recursive=resursive
    )


def getPackageFromPath(path):
    """获得包"""
    return unreal.load_package(path)


def getAllDirtyPackages():
    """获得所有脏包"""
    # 先创建一个空的列表
    packages = []
    # 从读取和保存的工具包里遍历出所有脏的内容包
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_content_packages():
        # 存入packages列表里
        packages.append(x)
    # 从读取和保存的工具包里遍历出所有脏的关卡包
    for x in unreal.EditorLoadingAndSavingUtils.get_dirty_map_packages():
        # 存入packages列表里
        packages.append(x)
    # 返回packages
    return packages


# show_dialog:显示对话框
def saveAllDirtyPackages(show_dialog=False):
    """保存所有脏包"""
    if show_dialog:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(
            save_map_packages=True, save_content_packages=True
        )
    else:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
            save_map_packages=True, save_content_packages=True
        )


def savePackages(packages=[], show_dialog=False):
    """保存包"""
    if show_dialog:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages_with_dialog(
            packages_to_save=packages, only_dirty=False
        )
    else:
        return unreal.EditorLoadingAndSavingUtils.save_dirty_packages(
            packages_to_save=packages, only_dirty=False
        )
