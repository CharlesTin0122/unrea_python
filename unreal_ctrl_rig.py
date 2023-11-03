import unreal

blueprint = unreal.load_object(
    name=r"/Game/Characters/Mannequins/Rigs/CR_Mannequin_Body.CR_Mannequin_Body",
    outer=None,
)
library = blueprint.get_local_function_library()
library_controller = blueprint.get_controller(library)
hierarchy = blueprint.hierarchy
hierarchy_controller = hierarchy.get_controller()
blueprint.get_controller_by_name("RigVMModel").break_link(
    "SequenceExecution_1.B", "Backward Clavicle_1.Execute"
)
blueprint.get_controller_by_name("RigVMModel").add_link(
    "SequenceExecution_1.B", "Backward Clavicle_1.Execute"
)
