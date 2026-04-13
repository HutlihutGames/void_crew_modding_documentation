# Testing Mods Locally
It's a good idea to test your mods locally before publishing them for other people to use.
You can also use this method to test mods in multiplayer with friends by sharing the necessary files and having them follow this same guide.

Always test your mods before distributing!

## Testing Asset Bundles without a Mod Manager
It's possible to test your asset bundles without installing them via a mod manager. 
This can be useful when testing quick iterations of the assets.

- To do this, go to your Void Crew install folder (the same folder that has Void Crew.exe).
  - Open install folder via Steam: Right click on Void Crew > Manage > Browse Local Files.
- If there is no "Mods" folder already, create one.
- Copy your asset bundle .metem files to the Mods folder. The game will natively try to load any asset bundles in the "Mods" folder.

## Testing Mods Locally Using Gale
- In Gale, go to "Import" on the toolbar and select "local mod"
- Select your zipped mod file. It should now be visible in Gale and enabled.
- Launch game via Gale to test your mod

## Testing Mods Locally Using R2ModMan
- In R2ModMan, click on your Void Crew profile in the bottom left corner
- Choose "Import local mod" and then "Select file"
- Select your zipped mod file
- Start modded game via R2ModMan

## Testing Carryables
It is useful to be able to spawn carryables directly, so you can test modded carryables without having to first acquire them naturally.
Official tools to do this are not available yet. 

For the time being, we recommend using the debugging tools published by Nihility-Shift [here](https://github.com/Nihility-Shift/VoidCrew.DebugTools).
- [Download the latest DebugTools zip file](https://github.com/Nihility-Shift/VoidCrew.DebugTools/releases/tag/0.0.4)
- Install the DebugTools zip file as a local mod via your mod manager.
- In-game, press F5 to open the Void Manager menu, then go to the settings menu for Debug Tools.
- In the Debug Tools settings menu, press the disable progress button.
- From the Hub or Ship, Press F10 to open the Spawn Menu. 
- In the Spawn menu, you can now search for your modded carryables and spawn them for testing.