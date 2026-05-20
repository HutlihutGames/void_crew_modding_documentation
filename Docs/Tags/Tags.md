# Tags
Void Crew uses a tag based system on objects that can be affected by stats. 
These tags can be used to filter what the stat modifiers are applied to.

You do not manually add these tags to anything yourself. Tags are listed here for their relation with stat modifiers.

For example, if you are making a relic you do not need to manually add the _Carryable_ and _Carryable_Relic_ tags to the object. 
Void Crew will add these tags automatically when the asset is loaded.

## Stat Modifier Tag Configuration
Tags can be used in various ways to configure where a stat modifier is applied.
Tags normally propagate downwards to other stat collections that are a part of the parent object.
This means there is a concept of _local tags_, which are tags that are placed specifically on that object.

For example, the tag "ShipPositional_Starboard" is held locally by module slots on the starboard side of the ship.
This tag is then **inherited** by modules placed on those module slots.


The tag configuration must be wrapped inside of a `"tag_config"` token in the stat modifier JSON data. For example:
```json
{
  "modifiers": [
    {
      "name": "PowerWanted",
      "type": "PrimaryAddend",
      "amount": -2,
      "tag_config": {
        "required": [
          "ShipPositional_Port",
          "Module_Category_Weapon"
        ]
      }
    },
    {
      "name": "PowerWanted",
      "type": "PrimaryAddend",
      "amount": 1,
      "tag_config": {
        "disabling": [
          "Module_Category_PowerProvider"
        ],
        "required": [
          "ShipPositional_Starboard"
        ]
      }
    }
  ]
}
```

### **Required Tags**
JSON: `"required"` \
Targets objects that have the specified tags or has inherited the specified tags from a parent object.

Tag config can specify which logic type the requirement should use.
JSON: `"required_criteria"` \
This can be either `"or"` or `"and"`.

When using `"or"`, then the criteria is met if any of the required tags are found. \
When using `"and"`, then the criteria is only met when **all** of the required tags are found. 

If the criteria is not specified, it will default to `"and"`.

Example where a modifier will apply to either port or starboard modules:
```json
{
  "modifiers": [
    {
      "name": "PowerWanted",
      "type": "PrimaryAddend",
      "amount": -1,
      "tag_config": {
        "required_criteria": "or",
        "required": [
          "ShipPositional_Port",
          "ShipPositional_Starboard"
        ]
      }
    }
  ]
}
```
### **Required Local Tags**
JSON: `"required_local"` \
Similar to required tags, but only targets objects that have the tags specified locally on itself, excluding inheritance.

Has a separate token for requirement criteria: \
JSON: `"required_local_criteria"`

### **Disabling Tags**
JSON: `"disabling"` \
This works like a tag blacklist, meaning that if an object has any of these specified tags, 
then the modifier will not apply even if all other criteria is met.

### **Dynamically Added Tags**
JSON: `"to_add"` \
This can be used to dynamically add tags to another object. 
Meaning all listed tags will be added locally to all objects affected by the modifier.

## List of Tags
| Tag                             | Held locally by                                                                                                              |
|:--------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| Ammo_Battery                    | Batteries, Payload Batteries                                                                                                 |
| Ammo_CaliberLarge               | Heavy caliber ammo magazines                                                                                                 |
| Ammo_CaliberSmall               | Light caliber ammo magazines                                                                                                 |
| Ammo_Missile                    | Payload Batteries                                                                                                            |
| Carryable                       | All carryables                                                                                                               |
| Carryable_BlankBuildBox         | Blank buildboxes                                                                                                             |
| Carryable_DataShard             | Carryables that can be inserted in the Astral Map                                                                            |
| Carryable_Homunculus            | Homunculi                                                                                                                    |
| Carryable_InscribedBuildBox     | Buildboxes inscribed with a module                                                                                           |
| Carryable_Interactive           | Copy Cube, System Upgrader, Oxygenated Blood Pack                                                                            |
| Carryable_Payload               | Payloads (not Payload Batteries)                                                                                             |
| Carryable_PowerFuse             | Power fuses                                                                                                                  |
| Carryable_Relic                 | Carryable mods that can be inserted in relic shrines                                                                         |
| Carryable_RepairPlate           | Hull Repair plates                                                                                                           |
| Carryable_WeaponMod             | Carryable mods that can be inserted into weapon modules.                                                                     |
| DamageType_Energy               | Weapons that do energy damage                                                                                                |
| DamageType_Kinetic              | Weapons that do kinetic damage                                                                                               |
| Module_Brain                    | Brain turrets, brain auto mechanic                                                                                           |
| Module_Category_BuiltIn         | Central Computer, Sarcograph, Helm, Void Drive, Built-in Life Support, Fabricator, Built-in Thruster Boosters                |
| Module_Category_Defense         | Directional shield, Kinetic point defense                                                                                    |
| Module_Category_PowerProvider   | Power generator, Central Computer                                                                                            |
| Module_Category_Utility         | Power generator, Brain auto mechanic, Charge station, Thruster station, Gravity scoop, Life support module, Payload launcher |
| Module_Category_Weapon          | All weapons modules                                                                                                          |
| Module_Category_WeaponWreck     |                                                                                                                              |
| Module_Family_Benediction       | Benediction Cannon, Benediction Brain                                                                                        |
| Module_Family_Confessor         | Confessor Carronade, Confessor Brain                                                                                         |
| Module_Family_Litany            | Litany Minigun                                                                                                               |
| Module_Family_Orison            | Orison Heavy Autocannon                                                                                                      |
| Module_Family_Recuser           | Recuser Beamcaster                                                                                                           |
| Module_Family_Shuriken          | Shruriken Energy Gatling                                                                                                     |
| Module_Family_Absolver          | Absolver Lance                                                                                                               |
| Module_Family_Bestower          | Bestower Flak Cannon                                                                                                         |
| Module_Mark_1                   | All MKI modules                                                                                                              |
| Module_Mark_2                   | All MKII modules                                                                                                             |
| Module_Mark_3                   | All MKIII modules                                                                                                            |
| Module_Type_AutoMechanic        | Brain auto mechanic                                                                                                          |
| Module_Type_BioBurner           | Unused module.                                                                                                               |
| Module_Type_CentralComputer     | Central Computer                                                                                                             |
| Module_Type_ChargeStation       | Charge Station, Built-in Charge Sockets                                                                                      |
| Module_Type_DirectionalShield   | Directional shield                                                                                                           |
| Module_Type_Fabricator          | Fabricator                                                                                                                   |
| Module_Type_GravityScoop        | Gravity scoop                                                                                                                |
| Module_Type_Helm                | Helm                                                                                                                         |
| Module_Type_KineticPointDefense | Kinetic point defense                                                                                                        |
| Module_Type_LifeSupport         | Life support module, Built-in Life Support                                                                                   |
| Module_Type_PayloadLauncher     | Payload launcher                                                                                                             |
| Module_Type_PowerGenerator      | Power generator                                                                                                              |
| Module_Type_Sarcograph          | Sarcograph                                                                                                                   |
| Module_Type_Shelves             | Shelves                                                                                                                      |
| Module_Type_ThrusterStation     | Thruster station, Built-in Thruster Boosters                                                                                 |
| Module_Type_VoidDrive           | Void Drive                                                                                                                   |
| ShipPositional_Aft              | Module slots on the aft side of the ship.                                                                                    |
| ShipPositional_Forward          | Module slots on the forward side of the ship.                                                                                |
| ShipPositional_Port             | Module slots on the port side of the ship.                                                                                   |
| ShipPositional_Starboard        | Module slots on the starboard side of the ship.                                                                              |

