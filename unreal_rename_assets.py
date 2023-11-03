# -*- coding: utf-8 -*-
"""
@FileName      : unreal_rename.py
@DateTime      : 2023/10/24 16:50:36
@Author        : Tian Chao
@Contact       : tianchao0533@163.com
@Software      : Maya 2023.3
@PythonVersion : python 3.9.7
@Description   :
"""
import unreal


def rename_assets(search_pattern: str, replace_pattern: str, use_case: bool):
    """批量重命名选定资产

    Args:
        search_pattern (str): 查询字符串
        replace_pattern (str): 替换字符串
        use_case (bool): 是否区分大小写
    """
    # 实例化虚幻类
    system_lib = unreal.SystemLibrary()
    editor_util_lib = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # 获取所选资产
    selected_assets = editor_util_lib.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0
    # 遍历所选资产
    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)
        unreal.log(asset_name)
        # 检查资产名称是否包含替换字符串(资产名称，子字符串，是否忽略大小写)，返回此资产名称是否包含指定的子字符串。
        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            # 如果use_case为真则替换规则使用CASE_SENSITIVE（区分大小写），否则使用IGNORE_CASE（忽略大小写）
            search_case = (
                unreal.SearchCase.CASE_SENSITIVE
                if use_case
                else unreal.SearchCase.IGNORE_CASE
            )
            replaced_name = string_lib.replace(
                asset_name, search_pattern, replace_pattern, search_case=search_case
            )
            editor_util_lib.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log(f"{asset_name} was replaced with {replaced_name}")
        else:
            unreal.log(f"{asset_name} did not match the search pattern,was skipped")

    unreal.log(f"replaced{replaced} of {num_assets} assets ")


rename_assets("attack", "skill", False)
