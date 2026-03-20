# Getting started

## Mod Profile
To avoid messing with your normal Void Crew profile while using or testing mods, you can use a separate Void Crew mod profile.

You can enable the mod profile by adding the following launch option to Void Crew on Steam: \
`-mods-profile`

![ModsProfile](img/modprofile.png)

Automated switching to modded profile to be implemented later.

## Mod Manager
First thing its important to know how mods are installed for Void Crew. 
You will also need a Mod Manager for testing your mods locally for testing.

Void Crew Mods are primarily distributed via [Thunderstore](https://thunderstore.io/c/void-crew/?included_categories=705&section=mods&ordering=top-rated)

1. Install a Mod Manager. We recommend either [Gale](https://kesomannen.com/gale) or [R2ModMan](https://r2modman.com/download-v3-2-9/) as they have good support for installing locally built mods.
2. With your chosen Mod Manager, install [VoidManager](https://thunderstore.io/c/void-crew/p/NihilityShift/VoidManager/). This is a community driven mod that has become the foundation behind Void Crew Modding, which we recommend all modders utilize.
3. Test installing any published community mod. When playing modded Void Crew, you need to launch the game via the Mod Manager.

## Installing Unity
Installing the Unity Editor is required for exporting custom content (asset bundles) for the game. 
We recommend using the same version as Void Crew, which currently uses **Unity Editor 2022.3.62f2**. 
1. Install [Unity Hub](https://unity.com/download), if not already installed. If you do not have a Unity account, you can create a free one. 
2. While you have Unity Hub open, use [this link](https://unity.com/releases/editor/whats-new/2022.3.62f2) to install the editor. You do not need to tick any of the optional modules for the install.

## Installing Git
We highly recommend using Git while developing mods. If you already use Git, you can skip this chapter.

Git is a version control system. It keeps track of changes you make to files, allowing you to:
- Roll back to a previous working version if something breaks
- See exactly what changed in your code
- Experiment safely without losing your work

For example, if you try a new feature and it causes your mod to stop working, Git lets you restore your project to an earlier state in seconds.

Git also makes it easy to download and update external resources such as:
- The [Void Crew Common Library](https://github.com/HutlihutGames/void_crew_common)
- The [Void Crew Samples Project](https://github.com/HutlihutGames/void_crew_mods_sample)

### Do I need GitHub?  
No, Git works entirely on your computer. GitHub is an online hosting/publishing service for Git Repositories. You do not need to upload your project anywhere, unless you want to:
- Collaborate with others
- Share your source code
- Publish your project as open source
For many, Git will simply act as a **local backup and version history system**.

### Git Client  
There are many options for Git clients available, installing most will also install Git itself on your system.

Many coding IDEs also have Git built-in, and that can also work well for simple solo projects.
If you're already comfortable using Git from within your editor, you can of course continue.

Suggested Git Clients:
- [GitHub Desktop](https://desktop.github.com/download/) (free)
- [Sourcetree](https://www.sourcetreeapp.com/) (free)
- [GitKraken](https://www.gitkraken.com/) (free for public repositories)
- [Fork](https://git-fork.com/) (free for evaluation)

Our recommendation to using a separate client is because they can give you a better overview of changes and provide
more functionality. Fork is good for both newcomers and advanced users as it has a very clean UI and is simple to use.

## Setting up the Void Crew Samples Project
Next, you will want to setup a clone of the Void Crew Samples Project. 
This template includes useful samples for getting started, and already includes the [Void Crew Common Library](https://github.com/HutlihutGames/void_crew_common).

1. Use your chosen Git client to clone the [void_crew_mods_sample](https://github.com/HutlihutGames/void_crew_mods_sample) repository. _If you are not using a Git client, you can clone it directly from Github._
2. In Unity Hub, press "Add" and select the folder containing the Void Crew Samples Project

## Other Tools
### 3D Assets
If you plan on including new 3D assets in your Mod, we recommend installing [Blender](https://www.blender.org/).
Blender will allow you to create custom 3D assets for free. 

It is also possible you will be using 3D assets made by others found on the internet. 
In that case Blender will also be a useful tool for modifying those assets, or converting them to FBX format for use in Unity. 

You can find example 3D assets in the samples project. This also includes simple scale models, so you can make the models fit neatly into our various socket shapes in the game.

### Images and Sprites
If you're making new 3D assets you'll likely also need to create new textures and sprites for UI icons.
Some free editors include: [Paint.Net](https://www.getpaint.net/), [GIMP](https://www.gimp.org/) and [Krita](https://krita.org/en/)
