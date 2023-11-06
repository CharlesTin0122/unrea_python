import unreal

anim_lib = unreal.AnimationLibrary()
anim_path = r"/Game/Mannequin/Animation/ClimbStart_Anim_Retargeted"
anim_asset = unreal.load_asset(anim_path)

assert isinstance(anim_asset, unreal.AnimSequence)
num_frames = anim_lib.get_num_frames(anim_asset)
for frame in range(num_frames):
    bone_transform = anim_lib.get_bone_pose_for_frame(
        anim_asset, "ball_r", frame, False
    )
    curve_name = "ik_foot_l"
    anim_lib.add_transformation_curve_key(anim_asset, curve_name, frame, bone_transform)
    unreal.log(bone_transform)
