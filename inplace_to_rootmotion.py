import unreal

util_lib = unreal.EditorUtilityLibrary()
asset_lib = unreal.EditorAssetLibrary()
anim_controller = unreal.AnimationDataController()
dir(unreal.AnimationDataController)
sel_assets = util_lib.get_selected_assets()
unreal.AnimationDataController.set_bone_track_keys()
