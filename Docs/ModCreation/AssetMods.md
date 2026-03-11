# Asset Mods
This guide covers how to make a mod that purely contains custom asset bundles, without having to write and compile any code yourself.

In the samples project find the folder "Mod Releases" at the root of the Project.

Copy the folder "Void Crew Banana Mod Sample-0.1.0". Give the new folder a name for your Mod.

Copy your exported asset bundles to the "AssetBundles" folder within the mod folder.
Make sure to include both the file with and without the ".manifest" filetype.

Update the meta data files in the folder with information regarding your mod. You will need to update manifest.json, README.md and icon.png.

When done, make a .zip file from the mod folder. To do this do the following:
- Select all the contents of the mod folder (CTRL+A)
- Right click the .dll file
- In the menu go to "Send To" and select "Compressed (zipped) folder"

### Manifest.json
The file manifest.json contains data used by mod loaders, to display your mod.

For now you only need to update name, and description. Update version number as you update the mod. 

Description must be less than 250 characters.

### Readme.md
This file is used to display information about your mod on the Thunder Store page. 
Update the file with information regarding your mod.

# Updating Void Crew Common
Eventually you might need to update the Void Crew Common package in Unity. 

To do this, open the package manager in Unity.

![UnityPackageManager](img/Unity_PackageManager.png)

In the package manager, find the `void_crew_common` package, and press "Update".

![UnityPackageManager](img/Unity_VCCPackage.png)