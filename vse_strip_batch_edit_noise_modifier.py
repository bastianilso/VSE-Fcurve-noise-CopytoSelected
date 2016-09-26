import bpy
from random import random

# Only selected (thus visible), editable objects
# bpy.data.objects would affect all objects in all scenes!
for ob in bpy.context.selected_sequences:
    #print(ob.id_data.animation_data)
    
    # Is there an animation?
    if ob.id_data.animation_data is not None and ob.id_data.animation_data.action is not None:
        action = ob.id_data.animation_data.action

        # Iterate over all F-Curves
        for fcu in action.fcurves:

            # Iterate over all F-Curve modifiers
            for mod in fcu.modifiers:

                # Only act upon Noise modifiers
                if mod.type == 'NOISE':
                    mod.scale = 64
                    mod.strength = 1.9
                    mod.blend_type = 'Replace'
                    
