# Stat Modifiers
This chapter will go over the various stat modifiers (StatMod) you are most likely going to need to use when making modded assets for Void Crew.

Objects in Void Crew that uses stats have what is called a Stat Tag Collection. 
This is a data structure which contains definitions of various stats from HP to Damage. It is built in such a way that you can add various modifiers that affect the base value of the stat, resulting in a new value. These modifiers can even propagate to child stat collections, and target collections with specific tags.

Objects that hold Stat Tag Collections are Orbit Objects (Players, Enemies, The Player Ship, Ship Modules, Destructible Containers...).

Objects that apply stat modifiers can be many things, but most commonly: Carryable mods (weapon mods, relics, homunculi), Mutators, Perks, Sector Twists. 

Stat modifiers from weapon mods generally only propagate to stat collections within the weapon they are added to.
However, relics and homunculi will try to apply modifiers across the whole player ship and its modules.

## Stat Modifier JSON Structure
Below is an example of a simply stat modifier written in JSON. This modifier does the following:
- Target the stat with the name "PowerWanted"
- Value modification type is "PrimaryAddend" (additive to base value)
- Modifier should be dynamically toggled depending on the conditions of type:
  - "SinglePlayer"
- Modified amount when active is -2
- Affects only targets that have the required tag "Module_Brain"

```json
{
  "modifiers": [
    {
      "name": "PowerWanted",
      "type": "PrimaryAddend",
      "dynamic_condition": {
        "type": "SinglePlayer"
      },
      "amount": -2,
      "tag_config": {
        "required": [
          "Module_Brain"
        ]
      }
    }
  ]
}
```

Its important to note that **the "name" token is not the name of the modifier**, but the name of the stat you want to modify.
It has the same purpose as the "id" token in that sense, which can also be used. Using "name" is just recommended over "id" 
because it makes the data more readable.

Every modifier **must** have either a "name" or "id" token to be valid. You can see the names of relevant stats at the end of this chapter.

The name of the modifier in UI is based on the name of the source (such as the name of the relic).

## Types of Stat Modifiers
There are four types of modifiers that affect how the modifier value is mathematically applied to the base value on the stat.

In Void Crew, additive modifiers are displayed with `%` while exponential modifiers are displayed with `x`

### **Primary Addend**
JSON: `"PrimaryAddend"` \
Flat value that can be positive or negative, which is added to the base value ahead of the other modifiers.

### **Secondary Addend**
JSON: `"SecondaryAddend"` \
Flat value that can be positive or negative, which is added at the end of all other modifiers

### **Additive Multiplier**
JSON: `"AdditiveMultiplier"` \
Multiplier that can be positive or negative. A value of 0 has no effect. A value of 1 will increase value by 100%. A value of 0.5 will increase value by 50%. -0.5 will decrease by 50%.

### **Exponential Multiplier**
JSON: `"ExponentialMultiplier"` \
Multiplier that is multiplied on top of other exponential multipliers mid calculation. Each Exponential Multiplier modifier multiplies the current exponential multiplier by:
  `(1 + Modifier Amount)`


Final calculation:

`Result =
(Base Value + Primary Addends)
× (1 + Additive Multipliers)
× Exponential Multiplier + Secondary Addends`

Example:
```
BaseValue = 100  
Primary Addends = +20  
Additive Multipliers = +0.5  
Exponential Multipliers = +0.2, +0.1  
Secondary Addends = +10

Exponential Multiplier = (1 + 0.2) × (1 + 0.1) = 1.32

Result =
(100 + 20) × (1 + 0.5) × 1.32 + 10
= 247.6
```

## Weapon Stats
| Stat name                 | Description                                                                                                                                                                                                                           | Normal Base Values |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------:|
| Damage                    | How much damage a weapon will do per shot, before multipliers from damage and armor types are applied.<br/> Note that internal numbers are multiplied by 100 before they are shown in UI.                                             |           1 to 100 |
| Firerate                  | How many shots the weapon can fire per second. For charge-up weapons like the beamcaster, this is instead a multiplier to the charge speed.                                                                                           |          0.1 to 30 |
| Range                     | The range of the weapon projectile in meters. The weapon projectile is destroyed if it moves past this range.                                                                                                                         |        500 to 2000 |
| ProjectileSpeed           | How fast the weapon projectile moves per second. Does not affect beam weapons.                                                                                                                                                        |       1000 to 2000 |
| Accuracy                  | Partly determines how much a projectile can spread (spread is a separate thing). Essentially a value of 1 here means the weapon is using the lowest spread possible, and 0 being the most spread. <br/> Does not affect beam weapons. |     Clamped 0 to 1 |
| RotationSpeed             | Determines how fast weapons can rotate. Can be be used to modify how fast a weapon is able to rotate while shooting, although this functionality is not actively used.                                                                |               1000 |
| DamageSecondary           | Used internally by editor tools, not used at runtime.                                                                                                                                                                                 |                    |
| MaxZoom                   | Affects much you zoom in on the weapon when holding right click by modifying your field of view.                                                                                                                                      |           1.2 to 2 |
| ReloadTime                | How long it takes to reload the weapon without active reload. Only affects weapons using light or heavy caliber magazines.                                                                                                            |            1 to 12 |
| MagazineReservoirTick     | How long it takes between each tick for the magazine to reservoir to refill. The amount refilled per tick depends on the weapon.                                                                                                      |          1.25 to 2 |
| ActiveReloadThreshold     | Fraction of the reload time where active reload can be performed.                                                                                                                                                                     |       0.025 to 0.1 |
| HeatPerShot               | How much heat percentage is generated per shot in a weapon using heat sink magazine.                                                                                                                                                  |     0.015 to 0.085 |
| HeatDissipationPerSec     | How much heat percentage decreases per second in a weapon using a heat sink magazine.                                                                                                                                                 |         0.1 to 0.2 |
| AmmoConsumptionEfficiency | How much ammo or battery charge is consumed per shot. When less than 1, multiple units are used per shot.                                                                                                                             |                  1 |
| KpdTrackingRange          | Used by Kinetic Point Defense to determine the maximum range it can track targets.                                                                                                                                                    |                525 |
| KpdCooldownAfterBurst     | Cooldown time in seconds between each burst with the Kinetic Point Defense                                                                                                                                                            |                  1 |

## Pip Stats
All ``Pip`` stats affect the related stat in question.
For each pip added, the base stat linearly moves from a minimum to a maximum base value.
Pip stats on weapons have 3 pips, which is what is increased by the Damage MKI, Firerate MKI weapon mods for example.
Because pips modify the base value, they are powerful when combined with modifiers to the non-pip equivalent of the stat.

Beware that many pip stats are legacy and might no longer be used. Additional scripting may be needed to re-apply the functionality of certain pip stats.

## Player Ship Stats

| Stat name               | Description                                                                                                     | Typical Base Values |
|:------------------------|:----------------------------------------------------------------------------------------------------------------|--------------------:|
| ShieldMaxHitPoints      | How much damage the ship can take before it is disabled.                                                        |          150 to 450 |
| ShieldRechargeSpeed     | How fast the shield recharges                                                                                   |            10 to 15 |
| ShieldRechargeDelay     | Delay in seconds before the shield starts recharging after taking damage.                                       |                   5 |
| ShieldAbsorption        | Fraction of the incoming damage the shield absorbs. Remaining damage is applied to the ship.                    |                 0.9 |
| ShieldGenerationEnabled | Used to automatically generate on enemies when they spawn, and reboot the shield.                               |              0 or 1 |
| Invulnerability         | Whether the shield is invulnerable.                                                                             |              0 or 1 |
| KineticVulnerability    | Multiplier to damage taken from the corresponding damage type. Most enemy projectiles are Kinetic               |                   1 |
| ElectricVulnerability   | Multiplier to damage taken from the corresponding damage type. Not used.                                        |                   1 |
| EnergyVulnerability     | Multiplier to damage taken from the corresponding damage type. Prism, Sniper and guided projectiles are Energy. |                   1 |
| FireVulnerability       | Multiplier to damage taken from the corresponding damage type. Fire Morph and Fire Boss attacks do Fire damage  |                   1 |
| FreezingVulnerability   | Multiplier to damage taken from the corresponding damage type. Ice Crystals do Freezing damage.                 |                   1 |
| PhysicalVulnerability   | Multiplier to damage taken from the corresponding damage type. Not used.                                        |                   1 |
| RadiationVulnerability  | Multiplier to damage taken from the corresponding damage type. Not used.                                        |                   1 |
| VoidVulnerability       | Multiplier to damage taken from the corresponding damage type. The Void Harbinger does Void damage.             |                   1 |
| MaxHitPoints            | Max hit points for the ship. Also determines starting hit points.                                               |        6000 to 6500 |
| TargetLockDamage        | Damage multiplier applied to target locked enemies.                                                             |                   1 |
| TargetLockCount         | How many target locks can be held at a time.                                                                    |                   4 |
| ScanRange               | Maximum range the ship scanner can reach.                                                                       |                3000 |
| ScanSpeedIncreased      | Seconds to decrease the default scan time with.                                                                 |                   0 |


## Movement Stats

| Stat name                    | Description                                                                                                                                            | Typical Base Values |
|:-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------:|
| ForwardPower                 | Scales how strongly the ship moves forward and backwards.                                                                                              |                   1 |
| YawTorque                    | Scales the ship's movement torque along its Y rotation.                                                                                                |                   1 |
| StrafePower                  | Scales how strongly the ship moves sideways.                                                                                                           |                   1 |
| ElevationPower               | Scales how strongly the ship moves up and down.                                                                                                        |                   1 |
| EnginePower                  | Scales all the above movement stats.                                                                                                                   |          0.5 to 1.7 |
| EnginePowerPip               | Pip stat for the engine power, which scales all the above movement stats by 3% per pip. This is the stat affected by engine trims. Starts at max pips. |          0.5 to 1.7 |
| PilotAidLevel                | Scales engine thrust input while cruise mode is enabled.                                                                                               |                 0.1 |
| JumpChargeSpeed              | Affects how fast the void drive is charged. Charge percent goes up by this value multiplied by 1.5 each second.                                        |       0.01 to 0.015 |
| VoidJumpCapable              | Determines if the ship can void jump. Hollow interdiction units add a -1 modifier to this stat. If the stat is 0 or less, the ship cannot void jump.   |                   1 |
| ThrusterBoosterDuration      | How many seconds the thruster boost should stay active.                                                                                                |                   9 |
| ThrusterBoosterCooldown      | How many seconds the thruster booster needs to cool down before they can be recharged.                                                                 |                   6 |
| ThrusterBoosterRechargeSpeed | Scales how much the thruster boosters recharge per second. Total charge time is by default 15 seconds.                                                 |                   1 |

Note: ForwardPowerPip, YawTorquePip, ElevationPowerPip, StrafePowerPip, PilotAidLevelPip, SignatureVelocity, and SignatureAngularVelocity are legacy stats which are no longer used.

## Power Stats

| Stat name               | Description                                                                                                                                                                  | Typical Base Values |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------:|
| PowerWanted             | How many power units is used by the module when active.                                                                                                                      |              1 to 6 |
| PowerProvided           | How much power is produced by a power provider (Central Computer and Power Generators).                                                                                      |              1 to 3 |
| BatteryRechargeAmount   | How much battery charge is generated per second. Battery sockets apply a modifier from this stat's value to the same stat on the battery (value is 0 on battery by default). |             2 to 20 |
| BreakerTemperatureShift | How much breaker temperature will change per second for each power unit the ship is overloaded by. Breaker chance to trigger is determined by its temperature.               |           -0.5 to 1 |

## Utility Stats

| Stat name               | Description                                                                                                                  | Typical Base Values |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------|--------------------:|
| ProcessingSpeed         | Scales fabricator speed and auto mechanic action cooldown time. Also used by download stations to determine download speed.  |                   1 |
| HealingSpeed            | How much Sarcograph will heal the occupant per second.                                                                       |                 0.2 |
| ActionCooldown          | Intended for interactive modules that should have an action cooldown. Currently unused, but may be used for future modules.  |                     |
| EffectRadius            | Intended for interactive modules that should have an AOE effect. Currently unused, but may be used for future modules later. |                     |
| AttractorMaxRange       | Maximum range of the Gravity Scoop.                                                                                          |                 200 |
| AttractorPullVelocity   | How many meters items are pulled towards the gravity scoop per second.                                                       |                  10 |
| LifeSupportEffectivity  | Multiplier used to scale the effectivity of life support modules.                                                            |                   1 |
| PassiveTemperatureShift | How much the ship passively changes the temperature of interior room atmospheres.                                            |                   0 |