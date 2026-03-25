# Skinning Guide
This is a simple guide for how to skin a mesh to a bone in Blender. 
You will need to do this to make your armor pieces follow the correct bones on the Ectype rig.

You can find more advanced guides elsewhere on the internet.

First you need to open the Rig. You can do this by either importing the [Ectype_Base.fbx](https://github.com/HutlihutGames/void_crew_mods_sample/blob/master/Assets/Mods/Cosmetics/Ectype_Base.fbx) or opening the [Ectype_Base.blend](https://github.com/HutlihutGames/void_crew_mods_sample/tree/master/Blend).

Importing FBX:
![OpenFBX](img/opening_fbx.png)

Alternatively open Blend file (requires Blender 5.0+):
![OpenBlend](img/opening_blend.png)

Once open, use the to import process to also add your cosmetic mesh.

First you'll want to position your mesh relative to where you want it to be positioned on the rig. In this guide we'll attach it to the Head bone.

![MeshPositioning](img/mesh_positioning.png)

Once you're satisfied, you can start the process of making it actually follow the bone.

Parent the mesh to the rig by first selecting the mesh, and then selecting the Rig second with CTRL+Click. 
Then while the mouse is in the viewport, use CTRL+P to open the parenting menu and select Armature Deform.

![MeshParenting](img/mesh_parenting.png)

The mesh should now by a child of the rig and have an armature modifier.

![MeshParentingResult](img/mesh_parenting_result.png)

The mesh now knows which rig (skeleton) to use, but not which bone yet. For this, you will need to learn the name of the bone you want the mesh to follow.
Go to Edit mode while having the Rig selected:

![MeshEditMode](img/mesh_edit_mode.png)

Select the bone you want the mesh to follow, then press F2 and copy the name of the bone. 

![MeshEditMode](img/mesh_bone_name.png)

Once you have the name of the bone, go back to Object Mode and make a new vertex group. Name the vertex group after the bone. 
It is important that the name of the vertex group and the bone are exactly the same.

![MeshEditMode](img/mesh_vertex_group.png)

To make the vertex group follow our bone completely, go back to Edit mode and assign the a weight of 1. 

![MeshEditMode](img/mesh_assign_weight.png)

**That's it!** 
If you want to check that the mesh was completely weight painted, go to Weight Paint mode. The Mesh should be colored red now.

![MeshEditMode](img/mesh_weight_mode.png)

You can also test the mesh is correctly following the bone. To do this, select the Rig and go to Pose mode. Then try moving a relevant bone.

![MeshEditMode](img/mesh_pose.png)