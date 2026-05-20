# Asset Mods
This guide covers how to publish a mod that purely contains custom asset bundles, without having to write and compile any code yourself.

If you just want to test your mod without going through a mod manager, check the guide in ["Testing Mods Locally"](TestingModsLocally.md).

## Creating Mod Zip File
In the samples project find the folder "Mod Releases" at the root of the Project.

Copy the folder "AssetModTemplate". Give the new folder a name for your Mod.

Copy your exported `.metem` files to the "AssetBundles" folder within the mod folder.
_You do not need to include the files that have the ".manifest" file extension._

Update the meta data files in the folder with information regarding your mod. You will need to update manifest.json, README.md and icon.png.

When done, make a .zip file from the mod folder. To do this on Windows do the following:
- Right click your mod folder
- Go to "Send To"
- Choose "Compressed (zipped) Folder"

**Manifest.json** \
The file manifest.json contains data used by mod loaders, to display your mod from within the mod loader itself.

For now you only need to update name, and description. Update the version number as you update the mod. 

Description must be less than 250 characters.

**Readme.md** \
This file is used to display information about your mod on the Thunder Store page. 
Update the file with information regarding your mod.

## Void Manager Dependency
The "AssetModTemplate" is currently setup to require Void Manager 1.3.0 as a dependency.
This is because a separate mod needs to handle registering the asset bundles in-game, when publishing the mod without compiling your own mod with to a DLL.

The 1.3.0 Prebuild version of VoidManager by Nihility Shift is available [here](https://github.com/Nihility-Shift/VoidManager/releases/tag/1.3.0-RC1).
- Download the Void Manager zip file.
- In your mod manager, install the zip file as a local mod.

This version of Void Manager will handle loading and registering all asset bundles with the .metem extension that have been loaded by your mod manager.

```{important}
The Void Manager dependency is a temporary requirement. Hutlihut will be making a separate solution to handle the registrations.
```

# Updating Void Crew Common
If the [Void Crew Common library](https://github.com/HutlihutGames/void_crew_common) is updated by Hutlihut Games, 
you will then need to manually update the library in your Unity project. 

The library can be updated in your Unity Project by using the Unity's Package Manager.

![UnityPackageManager](img/Unity_PackageManager.png)

In the package manager, find the `void_crew_common` package, and press "Update".

![UnityPackageManager](img/Unity_VCCPackage.png)