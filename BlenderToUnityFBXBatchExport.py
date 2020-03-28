import bpy


import os
import math
from mathutils import Matrix

#example path to store files
path = 'C:/Users/x/Desktop/Low Poly World/Exports/Trees/'

minusNinety = Matrix.Rotation(math.radians(-90.0), 4, 'X');
plusNinety = Matrix.Rotation(math.radians(90.0), 4, 'X');


#store selection
obs = bpy.context.selected_objects
    
for ob in obs:
    #deselect all but just one object and make it active
    bpy.ops.object.select_all(action='DESELECT')
    ob.select_set(state=True)
    bpy.context.view_layer.objects.active = ob
    
    #store object location then zero it out
    location = ob.location.copy()
    bpy.ops.object.location_clear()
    
    
    #rotate object to unitys coordinates
    
    #rotate object -90 on x axis
    ob.matrix_world = minusNinety @ ob.matrix_world
    #apply rotation
    bpy.ops.object.transform_apply( rotation = True )
    #rotate object 90 on x axis
    ob.matrix_world = plusNinety @ ob.matrix_world
    
    
    #export fbx
    filename = path + ob.name + '.fbx'
    bpy.ops.export_scene.fbx(filepath=filename, use_selection=True, apply_scale_options='FBX_SCALE_UNITS')
    
    #restore location
    ob.location = location
    #restore rotation
    bpy.ops.object.transform_apply( rotation = True )
  
#reselect originally selected objects  
for ob in obs:
    ob.select_set(state=True)