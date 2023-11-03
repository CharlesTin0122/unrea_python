# Copyright Epic Games, Inc. All Rights Reserved.

import os
import unreal

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()


def rename_directory(source_directory_path, target_directory_path):
    """
    Utility method for renaming a directory; equivalent to a 'move' operation.

    .. NOTE:: rename_directory from EditorAssetLibrary seems to be broken in 5.1:
        ref: https://forums.unrealengine.com/t/python-api-rename-directory-function-no-longer-works-in-5-1/748286

    .. USE:: rename_directory("/game/old_location", "/game/new_location")

    :param str source_directory_path: Game path to rename.
    :param str target_directory_path: Game path to rename the directory to.
    """
    # discover all contents in the source directory
    source_directory_contents = unreal.EditorAssetLibrary.list_assets(
        source_directory_path, include_folder=True
    )

    # find all assets and directories
    source_directory_assets = [c for c in source_directory_contents if "." in c]
    source_directory_folders = list(
        set(source_directory_contents) - set(source_directory_assets)
    )

    # create the new directory hierarchy
    unreal.EditorAssetLibrary.make_directory(target_directory_path)
    for folder in source_directory_folders:
        new_folder_name = folder.replace(source_directory_path, target_directory_path)
        unreal.EditorAssetLibrary.make_directory(new_folder_name)

    # rename the assets to the target directory path
    for asset_name in source_directory_assets:
        new_asset_name = asset_name.replace(
            source_directory_path, target_directory_path
        )
        unreal.EditorAssetLibrary.rename_asset(asset_name, new_asset_name)

    # delete old directory if empty
    if not unreal.EditorAssetLibrary.does_directory_have_assets(source_directory_path):
        unreal.EditorAssetLibrary.delete_directory(source_directory_path)
    else:
        unreal.log_warning(
            f"Could not delete '{source_directory_path}', "
            f"directory contains assets!"
        )


def get_asset_path(asset):
    """
    Gets the unreal Object path if not a string.

    :param str or object asset: The asset to get the path for.
    :return: Returns the path to the given asset.
    :rtype str
    """
    if isinstance(asset, unreal.Object):
        return asset.get_path_name()
    return asset


def get_asset_paths(assets):
    """
    Convenience method for getting a uniform list of asset paths.

    :param list(str) assets: The list of assets to get paths for.
    :return: Returns the list of asset paths.
    :rtype: list
    """
    return [get_asset_path(asset) for asset in assets]


def select_assets(assets):
    """
    Convenience method for selecting a list of assets in the editor.
    This method will also move you to the location of the selected assets
    in the editor content browser in engine.

    :param str or list(object or str) assets: Asset list to select.
    """
    # allow for str or list
    assets = assets if isinstance(assets, list) else [assets]

    # get a uniform list of paths
    assets_to_select = get_asset_paths(assets)
    unreal.EditorAssetLibrary.sync_browser_to_objects(assets_to_select)


def get_selected_assets(as_paths=False):
    """
    Get the selected assets in the editor content browser.

    :param bool as_paths: If True, returns the selected asset's paths.
    :return: Returns the selected assets in the editor content browser.
    :rtype: list(object or str)
    """
    utility_base = unreal.GlobalEditorUtilityBase.get_default_object()
    selected_assets = list(utility_base.get_selected_assets())

    # otherwise, return a list of the selected asset objects
    return get_asset_paths(selected_assets) if as_paths else selected_assets


def save_asset(asset, force=False):
    """
    Saves the given asset.

    :param str or object asset: The asset to save.
    :param bool force: Overrides the 'only_if_is_dirty' option.
    :return: Returns True if the asset saved successfully, False otherwise.
    :rtype: bool
    """
    return unreal.EditorAssetLibrary.save_asset(get_asset_path(asset), not force)


def save_assets(assets, force=False):
    """
    Saves the the list of assets.

    :param list(str) assets: List of asset to save
    :param bool force: Overrides the 'only_if_is_dirty' option.
    :return: Returns a tuple containing the assets that did and did not save.
    :rtype: tuple(list(object), list(object))
    """
    return list(map(lambda asset: save_asset(asset, force=force), assets))


def is_valid_asset_path(asset_path):
    """
    Simple method for validating if the given asset path is valid.

    :param str asset_path: Path to validate in engine.
    :return: Returns whether or not the path is valid.
    :rtype: bool
    """
    return unreal.EditorAssetLibrary.does_asset_exist(asset_path)


def duplicate_asset(source_asset, asset_name, asset_path, prompt=False):
    """
    Convenience method for duplicating a target asset.

    :param object source_asset: Asset to duplicate.
    :param str asset_name: What to name the duplicate asset.
    :param str asset_path: Where to duplicate the asset to.
    :param bool prompt: Whether to prompt the show the dialog or not.
    :return: Returns the duplicated blueprint object.
    :rtype: object
    """
    if not prompt:
        # determine the source and destination paths
        source_path = get_asset_path(source_asset)
        destination_path = os.path.join(asset_path, asset_name).replace("\\", "/")

        # duplicate the asset using the EditorAssetLibrary
        return unreal.EditorAssetLibrary.duplicate_asset(source_path, destination_path)

    # if prompt is True, use asset tools to prompt with a dialog
    return asset_tools.duplicate_asset_with_dialog(asset_name, asset_path, source_asset)
