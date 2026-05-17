# Your First Mod
This guide walks you through creating your first Void Crew mod inside Unity.

You do not need to know how to code for this guide. We will start with the smallest possible mod: a cosmetic color scheme. After that, we will make a simple helmet cosmetic, then a carryable item that can be crafted in the fabricator.

By the end of this page, you will have exported one or more `.metem` files that can be tested in Void Crew.

```{hint}
If you have not set up Unity yet, follow the Getting Started guide first.
```

```{note}
This page is intentionally beginner friendly. Some steps may feel obvious if you already know Unity, but they are included for readers who are opening Unity for the first time.
```

## Your first Mod: Cosmetic Color Scheme
In this first tutorial, we will create a simple cosmetic color scheme.
This is a good first mod because it only uses data you can define in Unity, no models required.

### Create a folder for your mod

- In Unity, go to the **Project window**.
- Create a new folder under **Assets**.
- Name it something clear to represent your mod, such as "My_First_Color_Scheme".

![CreateFolder](img/CreateFolder.png)

We'll refer to this folder as the "mod folder" from here on.

```{important}
Keep all assets used by the mod inside the mod folder. When you export the mod later, all dependencies must be inside the selected folder. If a texture, material, prefab, or other dependency is outside the folder, it may not be included correctly.

You can still have as many sub folders as you want for organization.
```

### Create the color scheme asset

- In the **Project window**, enter your mod folder if you haven't already.
- Right click an empty space within the project window. This should open a large context menu.
- Select **Create > Void Crew > Cosmetics > Color Scheme**
- Name the new asset

![CreateFolder](img/CreateColorScheme.png)

### Fill out the color scheme information

- Select your new color scheme asset
- In the **Inspector window**, give the color scheme a name. This is the name displayed in-game.
- You do not need to add a description.
- Add an icon for representing your color scheme in UI. Make sure the icon is also placed within your mod folder.
- Define primary, secondary, and tertiary colors. These are the colors that will be applied to the armor.

![CreateFolder](img/ColorSchemeInspector.png)

You can use the below image as a template for the icon, 
if you want it to match Void Crew's existing color scheme icons. 
The icon template is also available on the sample project [here](https://github.com/HutlihutGames/void_crew_mods_sample/blob/master/Assets/CosmeticsHelpers/icon-color-scheme-template.png).

![ColorSchemeTemplateIcon](img/icon-color-palette.png)

- <code style="color : red">Red</code> - primary (this is where patterns appear too), this usually covers the largest parts of armor cosmetics
- <code style="color : lightgreen">Green</code> - secondary
- <code style="color : blue">Blue</code> - tertiary, usually used for embellishments or decorative elements

### Export the asset bundle
- In the **Project window**, select your mod folder (not via the tree view on the left side).

![ColorSchemeTemplateIcon](img/TheCorrectFolder.png)

- In the Unity toolbar, open the Void Crew dropdown
- Select **Export Selected**

Unity will create an Exported Assets folder at the root of your Unity project, 
and open the folder automatically after exporting is done.

In the Exported Assets folder, there will be two files named after your mod folder: the one with the `.metem` file type is what you need to test your mod in-game.

_Note: if you cannot tell the files apart, [you need to enable file extensions in Windows explorer](https://support.microsoft.com/en-us/windows/common-file-name-extensions-in-windows-da4a4430-8e76-89c5-59f7-1cdbbc75cb01#id0ebf=windows_11)._

To test the mod immediately:
- Go to your Void Crew install folder (the same folder that has Void Crew.exe).
    - Open install folder via Steam: Right click on Void Crew > Manage > Browse Local Files.
- If there is no "Mods" folder already, create one.
- Copy your `.metem` files to the Mods folder. The game will natively try to load any `.metem` files placed in this folder.

This is just a simple export for quickly testing your modded asset.
For publishing, you will want to also add a [Mod Descriptor](../ModCreation/ModDescriptor.md) asset to your mod folder. 
Go to [this guide](../ModCreation/AssetMods.md) for how to export your mod for mod managers and [this guide](../ModCreation/UploadingMods.md) for uploading on ThunderStore.

## Your first Carryable: Simple Weapon Mod

You'll first need a model for the carryable model of your weapon mod.
For simplicity's sake, we'll just use [the size reference model available in the sample project](https://github.com/HutlihutGames/void_crew_mods_sample/blob/master/Assets/SizeReferences/Weapon_Mod_SizeRef.fbx).

Add your model file to your mod folder in Unity.

### Create a prefab for the weapon mod

- In the **Hierarchy window**, right click and create an empty GameObject.

![CreateEmpty](img/CreateEmpty.png)

- Select the GameObject in the **Hierarchy window** and go to the **Inspector window**
- Give the GameObject a name, such as "My Weapon Mod"
- Reset the Transform component of the GameObject, to ensure it has no weird offset.

![ResetTransform](img/ResetTransform.png)

- Drag and drop the GameObject from the **Hierarchy window** to the **Project window** inside your mod folder. This will turn it into a Prefab.

![DragAndDropPrefab](img/PrefabDragAndDrop.png)

```{hint}
Prefabs are reusable GameObjects. This means you can open the base prefab and make changes to it, that will apply to every instance of the prefab. If you make changes to the prefab from the scene they will be "overrides" to the base prefab.
```

When you select the GameObject you'll now notice the inspector looking a little different because it is now a prefab.

![PrefabInspector](img/PrefabInspector.png)

- Press the button to open the Prefab.
  - Alternatively, you can also double click the prefab in the **Project window**
- Drag and drop your model into the prefab.

![DragAndDropModel](img/DragAndDropModel.png)

- Select the model object in the **Hierarchy window** and set the X rotation to -90 relative to the parent.

![WeaponModModelRotation](img/WeaponModModelRotation.png)

The reason this needs to be done is because the pivot points on the weapon mod slots are rotated so that the X axis points towards the ceiling, and Y axis points towards the player.

![WeaponModModelRotation](img/WeaponModPivots.png)

### Add Components
Next you'll need to add a few components to the root of the prefab.
- Select the root of the prefab

![AddComponent](img/AddComponent.png)

Add the following components:
- Void Crew Asset (needed for all carryables)
- Carryable Stat Mod Asset (makes the carryable able to modify stats of other things)
- Craftable Item (makes it possible to craft the item)
- Loot Table Item (makes it possible to acquire the item via loot drops)
- Rigidbody (adds physics to the carryable)
- Box Collider (adds collision to the carryable)

Next we'll need to fill out the different components.

- Give the carryable a name, description and an icon
  - Remember the icon asset also needs to be placed inside your mod folder.

(Your icon doesn't have to be a fancy transparent clipart, it can also be a simple screenshot of the model)

![VoidCrewAsset](img/VoidCrewAsset.png)

- Add the Box Collider to the Override Collider field
- Add the renderer of your model to the Override Renderer

![CarryableBaseModReferences](img/CarryableBaseModReferences.png)

```{hint}
If you were making a relic instead, you'd need to tick the "Is Relic" box. 
```

- Add the json data for the stat modifiers you want the weapon mod to have.

For the tutorial's sake, you can try using this simple json block for buffing damage by 40% and decreasing fire rate by 20%.

```json
{
  "modifiers": [
    {
      "name": "Damage",
      "type": "AdditiveMultiplier",
      "amount": 0.4
    },
    {
      "name": "FireRate",
      "type": "AdditiveMultiplier",
      "amount": -0.2
    }
  ]
}
```

You can find lots of examples for stat modifier json data in the [StatModExamples folder](https://github.com/HutlihutGames/void_crew_mods_sample/tree/master/Assets/StatModExamples) in the sample project.

You can later read more about stat modifiers and how they work [here](../StatModifiers/StatModifiers.md).

Setup the crafting data if needed
  - Can be advantageous to set the cost to 0 for testing purposes.

Setup the loot data
- Add an entry in Sector Completion reward if you want the the weapon mod to appear via METEM Supply Drops
  - Set weight to 1 if you want it to appear at the same rate as most other items, or higher if you want it to appear more. 
  - Set amount to 1
  - Add a chapter entry and leave the value at 0 if you want it to appear before the first boss, or to 1 if you want it to appear only after the first boss
  - Set which encounter difficulties the item can appear in as a supply drop
- Add a drop table entry if you want the weapon mod to drop from enemies or appear in chests
  - Set amount to 1
  - Set the rarity type of the weapon mod
  - Set the drop location to **Floating**
  - Set the drop category to **On Death Pilgrimage** (this makes it appear as regular drops by enemies in Pilgrimage)
    - You can read more about the different drop tables [here](../Carryables/Carryables.md#drop-table-entries).

Edit size and offset of the Box Collider to match the model of the carryable.
Since we're making a weapon mod, the following works well:
- Offset: 0x, 0.02y, 0z 
- Size: 0.3x, 0.15y, 0.5z

When done you should see a collider like so when selecting the root of the prefab:

![BoxCollider](img/BoxCollider.png)

Note that nothing needs to be changed on the RigidBody component.

Remember to save your prefab when done!
You can press CTRL+S or use save button under the **Scene window**. Here you can also find a toggle for auto save.

![SafePrefab](img/SafePrefab.png)

From here, the steps to export your weapon mod are the same as in the [previous tutorial](#export-the-asset-bundle).

## Your first Cosmetic: Helmet
In this tutorial, we will create a wearable helmet cosmetic from a 3D model.

### Preparing Your Model

```{note}
Implementing a cosmetic into a Void Crew mod is easy: the hardest part is making the model or preparing an existing model.
```

You can use a model you made yourself, or a model downloaded from the internet. Make sure you have permission to use and redistribute the model if you plan to publish your mod.

- Find or make a helmet model that you'd like. You can find many free helmets online, for example on [Sketchfab](https://sketchfab.com/search?features=downloadable&licenses=7c23a1ba438d4306920229c12afcb5f9&licenses=322a749bcfa841b29dff1e8a1bb74b0b&q=space+helmet&type=models)
  - If you find a helmet online, it is possible that you will need to do some extra work in Blender to make it compatible with Void Crew.

For the model to be Void Crew ready it should ideally:
- Use a single material slot (or two if a projection compatible helmet)
- Have textures for the base color, and optionally also normal maps, metallic, smoothness, ambient occlusion and emission.

```{hint}
Base color texture is sometimes also referred to as "Diffuse" or "Albedo". 
```

You'll likely need to make the mask map texture yourself, by combining metallic, smoothness and ambient occlusion textures.
If the model has a roughness texture instead of smoothness, then just invert the texture.

```{note}
All the armor pieces must be setup so that they only have 1 material slot, which covers the whole mesh (helmets have a second slot for projections).
If you are downloading a model from the internet, we therefore recommend finding a model that is already setup to use one material. 
We plan on expanding this functionality in the future so more complex material setups are supported, and so it becomes easier to implement modded models from various origins. 
```

The process for preparing your model will differ a lot depending on the state you found the model in, unless you made it yourself.
We won't cover all the possible steps for that here, but since they'll likely be generic Blender specific processes, you should be able to find tutorials on for example Youtube to cover anything you need.

Instead we'll keep focusing on the Void Crew modding specific steps. 

The part of the process that will be needed for every wearable cosmetic is skinning the model to the character rig. 
This is the process that will make the cosmetic move with the correct bones on the character. 
You can read about how to do that in our [Skinning Guide](../Cosmetics/SkinningGuide.md).

We recommend exporting the model into FBX format from Blender, for better Unity compatibility. 

It is also recommended to export the cosmetics together with the whole rig, as that makes the setup within Unity a bit easier.

### Preparing your textures
If you don't have all the textures needed, you can create the other textures based on the base color texture.
[Materialize](https://www.boundingboxsoftware.com/materialize/) by Bounding Box Software is a great free tool for this.

To create the mask map, you can use an image editing tool such as [GIMP](https://www.gimp.org/) to combine the metallic, smoothness and and ambient occlusion textures into one image across different color channels:
- Red → Metallic
- Green → Ambient Occlusion
- Alpha → Smoothness

A mask texture will for example look like this:
![MaskTexture](img/Helmet_Mask.png)

Then you'll also want to create a zone map to define where armor patterns will be shown, and which armor colors are applied where.
This is done by coloring your texture in full pure red, green and blue colors (or black to make certain bits unaffected).
- <code style="color : red">Red</code> - primary (this is where patterns appear too), this usually covers the largest parts of armor cosmetics
- <code style="color : lightgreen">Green</code> - secondary
- <code style="color : blue">Blue</code> - tertiary, usually used for embellishments or decorative elements
- Black - Keep the color coming from the Base Color texture

A finished zone map texture will for example look like this:
![ZoneMapTexture](img/Helmet_ZonesMap.png)

### Setup your Model in Unity

- Add your model file to your mod folder.

Some simplicity's sake, we'll reference how to setup a helmet like the [example helmet in the sample project](https://github.com/HutlihutGames/void_crew_mods_sample/tree/master/Assets/Mods/Cosmetics/Helmet).
So we will add the [Ectype_Base.fbx](https://github.com/HutlihutGames/void_crew_mods_sample/blob/master/Assets/Mods/Cosmetics/Ectype_Base.fbx) to the folder in this tutorial.

- Drag and drop the model file into the hierarchy
- Expand the GameObject to see child objects. In there you will see all your cosmetics

![DragAndDropModel](img/DragAndDropModel.png)

- Right click on the model's gameobject where you see the blue box icon
- In the context menu go to Prefab > Unpack

![UnpackModel](img/UnpackModel.png)

- Drag and drop your helmet into your mod folder to turn it into a Prefab
  - If you have multiple cosmetics on the model you are turning into cosmetics, then you can repeat this process for each one.

![PrefabEachCosmetic](img/PrefabEachCosmetic.png)

Next you'll need to create the helmet cosmetic data asset.

- In the **Project window**, right click to open the context menu
- Go to Create > Void Crew > Cosmetics > Helmet

![CreateHelmetAsset](img/CreateHelmetAsset.png)

- Add a name and icon for you helmet
  - The icon can be a simple screenshot of the helmet 
- Add your textures to each respective field. 
  - Color Map is strongly recommended for the base texture. The others are optional, but still recommended.
  - Remember to make sure each texture is located somewhere within your mod folder.
- Set an emission color if you are using an emission map.
- Set how much armor patterns should tile onto the primary zone of your cosmetic. A higher value will make the pattern appear more "zoomed out".
- Drag and drop the helmet prefab we created earlier into the **Helmet Mesh** field. This should assign the Skinned Mesh Renderer included in the prefab.

![HelmetCosmeticData](img/HelmetCosmeticData.png)

Your helmet cosmetic is now ready for export!
From here, the steps to export your helmet mod are the same as in the [previous tutorial](#export-the-asset-bundle).

If you want to create other types of wearable cosmetics, then the process will be mostly the same. 
You can read about the differences between each type on our [Armor Pieces](../Cosmetics/ArmorPieces.md) page.