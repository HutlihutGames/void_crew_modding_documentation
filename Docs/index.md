# Void Crew Modding Documentation

```{toctree}
:hidden:
:maxdepth: -1
:caption: About

About/About
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Introduction

GettingStarted/GettingStarted
CreatingAssetBundles/CreatingAssetBundles
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Cosmetics

Cosmetics/Cosmetics
Cosmetics/CosmeticColors
Cosmetics/CosmeticPatterns
Cosmetics/ArmorPieces
Cosmetics/SkinningGuide
Cosmetics/HelmetProjections
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Carryables

Carryables/Carryables
StatModifiers/StatModifiers
StatModifiers/DynamicModifiers
Tags/Tags
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Mod Creation

ModCreation/AssetMods
ModCreation/CompilingMods
ModCreation/TestingModsLocally
ModCreation/UploadingMods
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Mod Scripting

ModScripting/HarmonyPatching
```

Welcome to the official documentation for Void Crew Modding!

Use the table of contents on the left or the search function to learn about more specific modding topics.

The site covers documentation for how to create mods for Void Crew and how to use:
- The [Void Crew Common Library](https://github.com/HutlihutGames/void_crew_common): Public library used by Void Crew that mods can utilize for increased capabilities. 
- The [Void Crew Samples Project](https://github.com/HutlihutGames/void_crew_mods_sample): Public sample Unity project which includes the common library, and features examples and helpers to get you started making Void Crew assets.

Disclaimer: much of the below documentation is still WIP.

Follow the guides below in order to get started and progress through the full modding workflow.

# Documentation Topics

- **[Getting Started](GettingStarted/GettingStarted.md)**  
   Introduction and initial setup required before creating mods.

- **[Creating Asset Bundles](CreatingAssetBundles/CreatingAssetBundles.md)**  
   Introduction on how to create asset bundles for Void Crew, including:
   - [Carryable Weapon Mods and Relics](Carryables/Carryables.md)
   - [Custom Cosmetics](Cosmetics/Cosmetics.md)

- **[Asset Mods](ModCreation/AssetMods.md)**  
   Introduction on how to make mods without custom code, using only asset bundles.

- **[Compiling Mods](ModCreation/CompilingMods.md)**  
   Introduction on how to compile your own mods, which can include your own custom scripts.

- **[Code Injection with Harmony Patching](ModScripting/HarmonyPatching.md)**  
   Introduction on how to inject code into Void Crew using Harmony.

- **[Testing Mods Locally](ModCreation/TestingModsLocally.md)**  
   Steps for testing your mods locally before publishing.

- **[Uploading Mods](ModCreation/UploadingMods.md)**  
   How to upload and share your mods.

- **[Stat Modifiers](StatModifiers/StatModifiers.md)**  
   Documentation on Void Crew Stat Modifiers (StatMod).

- **[Dynamic Modifiers](StatModifiers/DynamicModifiers.md)**  
   Documentation on how dynamic stat modifiers work in Void Crew.

- **[Tags](Tags/Tags.md)**  
    Documentation on Void Crew's tag system.

# License and Contribution
The documentation is licensed under our [Void Crew Modding Documentation License](https://github.com/HutlihutGames/void_crew_modding_documentation/blob/main/LICENSE). \
This allows anyone to contribute and improve the documentation! \
Contribution can be done via the [GitHub repository](https://github.com/HutlihutGames/void_crew_modding_documentation) where the documentation is hosted.
