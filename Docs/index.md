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
GettingStarted/TutorialFirstMod
GettingStarted/TutorialCarryable
GettingStarted/TutorialCosmetic
Cosmetics/SkinningGuide
CreatingAssets/CreatingAssets
CreatingAssets/ArtDirection
GettingStarted/Glossary
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Cosmetics

Cosmetics/Cosmetics
Cosmetics/CosmeticColors
Cosmetics/CosmeticPatterns
Cosmetics/ArmorPieces
Cosmetics/HelmetProjections
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Ship & Hub Customization

ShipCustomization/ShipAndHubVisuals
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
ModCreation/ModDescriptor
ModCreation/TestingModsLocally
ModCreation/UploadingMods
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Mod Scripting

ModScripting/ScriptedMods
ModScripting/HarmonyPatching
```

```{toctree}
:hidden:
:maxdepth: -1
:caption: Debugging

Debugging/DebugCamera
Debugging/CheckingLogs
Debugging/CommonIssues
```

Welcome to the official documentation for Void Crew Modding!

Use the table of contents on the left or the search function to learn about more specific modding topics.

The site covers documentation for how to create mods for Void Crew and how to use:
- The [Void Crew Common Library](https://github.com/HutlihutGames/void_crew_common): Public library used by Void Crew that mods can utilize for increased capabilities. 
- The [Void Crew Samples Project](https://github.com/HutlihutGames/void_crew_mods_sample): Public sample Unity project which includes the common library, and features examples and helpers to get you started making Void Crew assets.

Follow the guides below in order to get started and progress through the full modding workflow.

# Documentation Topics

- **[Getting Started](GettingStarted/GettingStarted.md)**  
   Introduction and initial setup required before creating mods.
    - [How to make your first mod](GettingStarted/TutorialFirstMod.md)
    - [How to make a simple weapon stat mod](GettingStarted/TutorialCarryable.md)
    - [How to make a wearable cosmetic](GettingStarted/TutorialCosmetic.md)
    - [How to skin cosmetics](Cosmetics/SkinningGuide.md)

- **[Creating Assets](CreatingAssets/CreatingAssets.md)**  
   Introduction on how to create assets for Void Crew, including:
   - [Carryable Weapon Mods and Relics](Carryables/Carryables.md)
   - [Custom Cosmetics](Cosmetics/Cosmetics.md)
   - [Custom Ship Visuals](ShipCustomization/ShipAndHubVisuals.md)

- **[Asset Bundle Mods](ModCreation/AssetMods.md)**  
   Guide on how to make mods purely from assets created within Unity.

- **[Testing Mods Locally](ModCreation/TestingModsLocally.md)**  
   Guide for testing your mods locally before publishing.

- **[Uploading Mods](ModCreation/UploadingMods.md)**  
   Guide to uploading and publishing your mods.

- **[Stat Modifiers](StatModifiers/StatModifiers.md)**  
   Documentation on Void Crew Stat Modifiers (StatMod).

- **[Dynamic Modifiers](StatModifiers/DynamicModifiers.md)**  
   Documentation on how dynamic stat modifiers work in Void Crew.

- **[Tags](Tags/Tags.md)**  
    Documentation on Void Crew's tag system.

- **[Compiling Mods](ModScripting/ScriptedMods.md)**  
  Introduction on how to compile your own mods, which can include your own custom scripts.

- **[Code Injection with Harmony Patching](ModScripting/HarmonyPatching.md)**  
  Introduction on how to inject code into Void Crew using Harmony.

# License and Contribution
The documentation is licensed under our [Void Crew Modding Documentation License](https://github.com/HutlihutGames/void_crew_modding_documentation/blob/main/LICENSE). \
This allows anyone to contribute and improve the documentation! \
Contribution can be done via the [GitHub repository](https://github.com/HutlihutGames/void_crew_modding_documentation) where the documentation is hosted.
