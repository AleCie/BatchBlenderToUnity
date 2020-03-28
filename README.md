# BatchBlenderToUnity
Python script for Blender 2.8 for batch exporting models to Unity.

* Works with Blender 2.8
* Exports selected objects as separate files to predefined path (you have to edit the path in the script)
* Correctly applies transforms (scale and rotation in Unity is as it should be)

I claim no resposibility for corrupted blender files. Back up your project and use it at your own risk.

# How to use

* Create new script in Blender and paste source code from BlenderToUnityFBXBatchExport.py
* Change `path = 'C:/yourpath/'` to the path where you want your files to be exported
* Make sure you have names your objects in Blender, exported files will have the same name
* Select all the objects that you want to export
* Press Run Script

![Blender](/scr/scr1.png)

![Folder](/scr/scr2.png)

![Unity](/scr/scr3.png)

