# Glossary
This page covers terms that people may be unfamiliar with if they are new to Unity, modding, or specifically modding for Void Crew.

## Core Terms
| Term                         | Beginner-friendly definition                                                                                                                                                       |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Void Crew Common**         | A shared Unity package containing definitions and tools used by Void Crew and Void Crew mods.                                                                                      |
| **Void Crew Sample Project** | A Unity Project that has been set up to already include Void Crew Common, plus several examples. This is the recommended starting point for new modders.                           |
| **Asset Bundle**             | A packaged group of Unity assets exported from Unity so the game can load them as mod content. Void Crew asset bundles use the `.metem` file extension.                            |
| **Void Crew Mod Descriptor** | A Unity data asset that stores the publishing information for a mod. The "Export as Mod" tool uses this asset to generate the files needed for a Thunderstore/mod-manager package. |

## Setup and Software Terms
| Term                       | Beginner-friendly definition                                                                                                                        |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unity**                  | The game engine used to build Void Crew and make assets for Void Crew. Modders can use Unity to make assets, and export mod files as asset bundles. |
| **GitHub**                 | A website commonly used by developers to host code and project files. GitHub uses a form of version control called Git.                             |
| **Repository / Repo**      | A project stored in Git, and often hosted on GitHub. A repo usually contains files, folders, code, documentation, and version history.              |
| **Clone**                  | To download a full copy of a repository to your computer. Unlike a regular download, a cloned repository can be more easily updated.                |
| **Git Client**             | Software that lets your computer interact with repositories.                                                                                        |

## Unity and Asset Terms
| Term                      | Beginner-friendly definition                                                                                                                                        |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Asset**                 | Any file used by the game, such as a 3D model, texture, sound, material, prefab, icon, or animation.                                                                |
| **GameObject**            | A basic object inside Unity. Almost everything placed in a Unity scene or prefab is a GameObject.                                                                   |
| **ScriptableObject**      | A type of data object used by Unity. Unlike GameObjects, these cannot be placed within a Unity scene, but contain data that other GameObjects rely upon.            |
| **Component**             | A piece of functionality attached to a GameObject, which extends what that object is and can do.                                                                    |
| **Prefab**                | A reusable Unity GameObject saved as an asset. For Void Crew mods, a mesh usually needs to be placed into a prefab before it can be used properly.                  |
| **Mesh**                  | The 3D shape of an object. A helmet, shoulder pad, relic, or ship part all use meshes.                                                                              |
| **Skinned Mesh Renderer** | A Unity component used to display a mesh that can deform and follow the shape of a character. This is especially relevant for wearable cosmetics like armor pieces. |
| **Renderer**              | A Unity component that makes an object visible in the game. Different renderer types are used for static objects, animated objects, or character-worn objects.      |
| **Rig**                   | A skeleton structure used to animate or attach a 3D model correctly.                                                                                                |
| **Armature**              | Blender’s term for a rig or skeleton. It controls how a character or object bends, moves, or attaches to bones.                                                     |
| **Bone**                  | A part of a rig. Wearable cosmetics may need to align with the correct bones so they move properly with the character.                                              |
| **Material**              | A Unity asset that controls how a surface looks, including color, shine, transparency, metallic effects, and emissive glow.                                         |
| **Texture**               | An image file used by a material. Textures can define color, roughness, metallic surfaces, normal details, emissive areas, and more.                                |
| **Sprite**                | An image file that is usually displayed in 2D rather than on a 3D material, such as in UI                                                                           |
| **Shader**                | A rendering program that controls how a material appears in-game. Shaders affect lighting, reflections, transparency, glow, and surface style.                      |
| **UV Map**                | A layout that tells the game how a 2D texture wraps onto a 3D model.                                                                                                |
| **Blender**               | A free 3D modeling program often used to create or edit 3D models before importing them into Unity.                                                                 |

## File Terms
| Term                 | Beginner-friendly definition                                                                                                                                                                                         |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`.fbx`** file      | A filetype containing a 3D model, which is commonly exported from Blender and imported into Unity                                                                                                                    |
| **`.metem` file**    | A Void Crew asset bundle file. This is the file that contains all the exported assets needed for your mod.                                                                                                           |
| **`.manifest` file** | A companion file Unity exports along with the main asset bundle files. This file is usually not needed for distribution.                                                                                             |
| **`manifest.json`**  | A metadata file commonly used for mod-manager distribution. It tells the mod manager important information such as the mod name, version, author, and dependencies.                                                  |
| **`README.md`**      | A text file, usually written in Markdown, that explains what the mod does, how to install it, and any notes for users. The content of the README is the first thing users see when viewing your mod on Thunderstore. |

## Installation & Publishing Terms
| Term                                             | Beginner-friendly definition                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mod Manager**                                  | A piece of software that installs, updates, enables, disables, and organizes mods for players.                                                                                                                                                                                                                               |
| **r2modman**                                     | A commonly used mod manager for Thunderstore-hosted mods.                                                                                                                                                                                                                                                                    |
| **Gale**                                         | A newer alternative to r2modman.                                                                                                                                                                                                                                                                                             |
| **Void Crew Mods Folder**                        | The local folder adjacent to `Void Crew.exe` where Void Crew looks for `.metem` files to load, without depending on a Mod Manager. This can be useful for testing quick iterations of a mod. The folder does not exist by default. If it does not exist: create it.                                                          |
| **Direct `.metem` file Install**                 | Installing a mod by placing `.metem` files directly in the Void Crew Mods Folder.                                                                                                                                                                                                                                            |
| **Mod Manager Install**                          | Installing a mod through a manager such as Gale or r2modman. This usually means the mod manager handles the folder layout, dependencies, and launch profile.                                                                                                                                                                 |
| **Mod Manager Import from File / Local Install** | Installing a mod from a file already on your computer instead of downloading it from Thunderstore. Some mod managers call this a Local Install, but it is different from placing .metem files in the Void Crew Mods folder.                                                                                                  |
| **Thunderstore Install**                         | Installing a published mod from Thunderstore through a supported mod manager.                                                                                                                                                                                                                                                |
| **Thunderstore Package**                         | A packaged mod prepared for Thunderstore or mod-manager distribution. This may include files such as `manifest.json`, `README.md`, icon files, dependencies, asset files, and sometimes a `.dll`, depending on the mod type and packaging requirements.                                                                      |
| **BepInEx Plugin Install**                       | Installing a code/plugin-based mod by placing files into the BepInEx folder structure, commonly inside a `plugins` folder, which itself is placed inside a folder managed by your mod manager. Some mods may refer to this as **"Manual Install"**. Generally this form of installation is _obsolete_ for native asset mods. |
| **Export Asset Bundles**                         | Exporting assets into `.metem` files, suitable for quickly testing via Direct Install.                                                                                                                                                                                                                                       |
| **Export as Mod**                                | A tool that exports and wraps assets into a folder suitable for publishing on Thunderstore/Mod Manager publishing. The folder will contain relevant files based on a `Void Crew Mod Descriptor`.                                                                                                                             |
| **Native Asset Mod**                             | A mod containing only asset bundles, which can be loaded through the game’s native code via `.metem` files.                                                                                                                                                                                                                  |
| **Scripted Mod**                                 | A mod that includes custom code, not just exported assets. Scripted mods are more advanced and may require Visual Studio, C#, compiling, and BepInEx-style packaging.                                                                                                                                                        |
| **VoidManager**                                  | A community made mod by Nihility-Shift, which is used as a dependency by many mods.                                                                                                                                                                                                                                          |
| **Dependency**                                   | Another mod or framework that must be installed for a mod to work. Mod managers usually install dependencies automatically when they are listed correctly.                                                                                                                                                                   |


## Advanced Modding Terms
These terms are likely only relevant to understand if making advanced mods that require custom scripts.

| Term                | Definition                                                                                                                                         |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **`.dll` file**     | A compiled code file used by scripted/plugin-based mods. Some asset-mod packaging workflows may also include a `.dll` for mod-manager recognition. |
| **BepInEx**         | A Unity modding framework used for loading plugin/code-based mods.                                                                                 |
| **BepInExPack**     | A packaged version of BepInEx commonly distributed through mod managers.                                                                           |
| **Visual Studio**   | A code editor and development environment used for creating or compiling scripted mod files.                                                       |
| **Solution**        | A Visual Studio container for one or more code projects.                                                                                           |
| **Project**         | In Visual Studio, a set of code files and settings that build into an output such as a `.dll`.                                                     |
| **Namespace**       | A programming label used to organize code and avoid naming conflicts.                                                                              |
| **Compile / Build** | Turning code into an output file, such as a `.dll`, that the game or framework can load.                                                           |
| **Plugin**          | A code-based mod component loaded by a framework such as BepInEx.                                                                                  |
