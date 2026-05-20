# Creating Assets
You can create various types of assets within Unity that Void Crew can natively load [by later exporting them into asset bundles](../ModCreation/AssetMods.md).
## Void Crew Asset
This is the base component needed for the asset to be loaded into the game. It has the following fields:
- **Name**: Name of the Asset
- **Description**: Description of the asset
- **Icon**: Icon for the asset. The icon's `Texture Type` should be set to `Sprite (2D and UI)`.

![VoidCrewAsset](img/VoidCrewAsset.png)
These fields are used to populate the asset's Context Info in the game. Context info is the data structure used to fill out the tooltips you see when looking at items or hovering over them in UI.

The name of the asset will also be used for information regarding mod compatibility and other debugging info. So even assets that don't have tooltips
should at least still have a name.

**Note for Cosmetics**: Cosmetics use scriptable objects instead of prefabs for the assets. So the above fields are found on the cosmetic objects themselves instead of the Void Crew Asset component.
![ColorScheme](img/ColorScheme.png)

You can include rich text tags in the name and description to add additional styling.
Check [this link](https://docs.unity3d.com/2022.3/Documentation/Manual/UIE-supported-tags.html) to see supported rich text tags for our version of Unity.

## Never modify examples
It is **IMPORTANT** that when you make **new** assets that you either:
- Duplicate another asset and work on the duplicate
- Make a new asset from scratch, and add the necessary components if it is not a scriptable object.

**Never** make your assets by modifying other examples or templates provided by the sample project or by other modders.
Doing so will mean they have the same ID (GUID) in their metadata, which will cause problems for Void Crew loading
the assets.

By duplicating or making the asset from scratch a new ID will be generated automatically, which ensures your assets will
not conflict with assets created by others. Additionally, by ensuring your assets keep a unique ID you will also be able
to update the mod with the assets and the game to still know it is the same asset (so for example cosmetics stay equipped).

## Size References
If you want to create your own 3D assets, you will likely want some references for shape and scale. \
[In the sample project](https://github.com/HutlihutGames/void_crew_mods_sample/tree/master/Assets/SizeReferences)
we have included reference FBX files that you can use in for example Blender and Unity.

## Types of Void Crew Asset Bundles
You can read more about how to create different types of asset bundles in the below chapters.

**[Carryables](../Carryables/Carryables.md)**
Learn about how to create custom weapon mods and relics.

**[Cosmetics](../Cosmetics/Cosmetics.md)**
Learn about how to create custom cosmetics.

**[Ship and Hub Visuals](../ShipCustomization/ShipAndHubVisuals.md)**
Learn about how to create custom visuals for the Hub and different player Ships.