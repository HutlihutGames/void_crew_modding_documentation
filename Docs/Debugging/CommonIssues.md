# Common Issues
## Black Screen on Launch
This usually means the game ran into an exception while initializing services or other core systems.
You can usually find the cause relatively early in the logs.

## Exception in Convert Asset
If you get an error like below, the asset conversion encountered a null reference.
This is likely due to an asset not being included in the asset bundle, because it was outside the asset bundle folder.
It might also be that a required reference was empty (for example: Suit assets require an Arm renderer reference even if it is the same renderer as the suit).
```
NullReferenceException: Object reference not set to an instance of an object
  at RuntimeAssets.RuntimeAssetConverter.ConvertAsset (VC.Common.VoidCrewScriptableObject asset, System.Nullable`1[T] overrideGuid) [0x00347] in <9fecb71473e0461f92027e24b2c938f6>:0 
  at RuntimeAssets.RuntimeAssetsAPI.LoadAsset (VC.Common.VoidCrewScriptableObject vcso, System.Nullable`1[T] overrideId) [0x00027] in <9fecb71473e0461f92027e24b2c938f6>:0 
  at RuntimeAssets.RuntimeAssetsAPI.LoadAsset (UnityEngine.Object asset) [0x00048] in <9fecb71473e0461f92027e24b2c938f6>:0 
  at RuntimeAssets.RuntimeAssetsAPI.LoadAssetBundle (System.String fullPath) [0x0002b] in <9fecb71473e0461f92027e24b2c938f6>:0 
  at RuntimeAssets.RuntimeAssetLoadingService+<Initialize>d__1.MoveNext () [0x00119] in <9fecb71473e0461f92027e24b2c938f6>:0 
  at UnityEngine.SetupCoroutine.InvokeMoveNext (System.Collections.IEnumerator enumerator, System.IntPtr returnValueAddress) [0x00026] in <c39a522eee05469b8171a6cfeb646c59>:0
```

## My asset is missing textures
This likely means that the missing textures weren't placed inside the mod folder you exported from.
Place them inside your mod folder and export again.

## My carryable is invisible
The materials on carryable might be using a shader type that is unsupported. 

Make sure your Unity project is setup to use HDRP.
- In the Unity Toolbar, go to Edit > Project Settings
- Go to Graphics Settings and ensure you have a Scriptable Render Pipeline Settings asset assigned.
- If it is missing, create one
  - In the Project window under the Assets folder, open the HDRPSettings folder
  - Right click an empty space go to Create > Rendering > HDRP Asset
  - Assign the asset in Graphics settings

Verify that the materials on your carryable are using an HDRP compatible shader.
- If not, create new materials using shaders that are HDRP compatible (for example HDRP/Lit)
- Assign the new materials to the renderer of your carryable.

## I worked from a sample asset by mistake, do I have to start over?
This can mean the assets won't be compatible for other mods due to duplicate GUIDs.

In Unity's Project Window, select your mod folder. Then press CTRL+D. 
This will duplicate the folder, and automatically generate new GUIDs for everything within. 