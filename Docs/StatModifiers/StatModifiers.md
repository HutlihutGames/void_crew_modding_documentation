# Stat Modifiers
This chapter will go over the various stat modifiers (StatMod) you are most likely going to need to use when making modded assets for Void Crew.

Objects in Void Crew that uses stats have what is called a Stat Tag Collection. 
This is a data structure which contains definitions of various stats from HP to Damage. It is built in such a way that you can add various modifiers that affect the base value of the stat, resulting in a new value. These modifiers can even propagate to child stat collections, and target collections with specific tags.

Objects that hold Stat Tag Collections are Orbit Objects (Players, Enemies, The Player Ship, Ship Modules, Destructible Containers...).

Objects that apply stat modifiers can be many things, but most commonly: Carryable mods (weapon mods, relics, homunculi), Mutators, Perks, Sector Twists. 

Stat modifiers from weapon mods generally only propagate to stat collections within the weapon they are added to.
However, relics and homunculi will try to apply modifiers across the whole player ship and its modules.

## Types of Stat Modifiers
There are four types of modifiers that affect how the modifier value is mathematically applied to the base value on the stat.

In Void Crew, additive modifiers are displayed with `%` while exponential modifiers are displayed with `x`

- **Primary Addend**:
Flat value that can be positive or negative, which is added to the base value ahead of the other modifiers.
- **SecondaryAddend**:
Flat value that can be positive or negative, which is added at the end of all other modifiers
- **Additive Multiplier**:
Multiplier that can be positive or negative. A value of 0 has no effect. A value of 1 will increase value by 100%. A value of 0.5 will increase value by 50%. -0.5 will decrease by 50%.
- **Exponential Multiplier**:
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
| Stat                      | Description                                                                                                                                                                                                                           | Normal Base Values |
|:--------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------:|
| Damage                    | How much damage a weapon will do per shot, before multipliers <br/from damage and armor types are applied. <br/>Note that internal numbers are multiplied by 100 before they are shown in UI.                                         |           1 to 100 |
| Firerate                  | How many shots per second the weapon can fire per second. For charge-up weapons like the beamcaster, this is instead a multiplier to the charge speed.                                                                                |          0.1 to 30 |
| Range                     | The range of the weapon projectile in meters. The weapon projectile is destroyed if it moves past this range.                                                                                                                         |        500 to 2000 |
| ProjectileSpeed           | How fast the weapon projectile moves per second. Does not affect beam weapons.                                                                                                                                                        |       1000 to 2000 |
| Accuracy                  | Partly determines how much a projectile can spread (spread is a separate thing). Essentially a value of 1 here means the weapon is using the lowest spread possible, and 0 being the most spread. <br/> Does not affect beam weapons. |     Clamped 0 to 1 |
| RotationSpeed             |                                                                                                                                                                                                                                       |                    |
| DamageSecondary           |                                                                                                                                                                                                                                       |                    |
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

## Player Ship Stats
| Stat                    | Description                                                                                                     | Typical Base Values |
|:------------------------|:----------------------------------------------------------------------------------------------------------------|--------------------:|
| ShieldMaxHitPoints      | How much damage the ship can take before it is disabled.                                                        |                     |
| ShieldRechargeSpeed     | How fast the shield recharges                                                                                   |                     |
| ShieldRechargeDelay     | Delay in seconds before the shield starts recharging after taking damage.                                       |                     |
| ShieldAbsorption        | Fraction of the incoming damage the shield absorbs. Remaining damage is applied to the ship.                    |                     |
| ShieldGenerationEnabled | Used to automatically generate on enemies when they spawn, and reboot the shield.                               |              0 or 1 |
| Invulnerability         | Whether the shield is invulnerable.                                                                             |              0 or 1 |
| KineticVulnerability    | Multiplier to damage taken from the corresponding damage type. Most enemy projectiles are Kinetic               |                   1 |
| ElectricVulnerability   | Multiplier to damage taken from the corresponding damage type. Not used.                                        |                     |
| EnergyVulnerability     | Multiplier to damage taken from the corresponding damage type. Prism, Sniper and guided projectiles are Energy. |                     |
| FireVulnerability       | Multiplier to damage taken from the corresponding damage type. Fire Morph and Fire Boss attacks do Fire damage  |                     |
| FreezingVulnerability   | Multiplier to damage taken from the corresponding damage type. Ice Crystals do Freezing damage.                 |                     |
| PhysicalVulnerability   | Multiplier to damage taken from the corresponding damage type. Not used.                                        |                     |
| RadiationVulnerability  | Multiplier to damage taken from the corresponding damage type. Not used.                                        |                     |
| VoidVulnerability       | Multiplier to damage taken from the corresponding damage type. The Void Harbinger does Void damage.             |                     |
| MaxHitPoints            | Max hit points for the ship. Also determines starting hit points.                                               |        6000 to 6500 |

## Movement Stats
| Stat                          | Description | Typical Base Values |
|:------------------------------|:------------|--------------------:|
| ForwardPower                  |             |                     |
| YawTorque                     |             |                     |
| StrafePower                   |             |                     |
| EnginePower                   |             |                     |
| PilotAidLevel                 |             |                     |
| JumpChargeSpeed               |             |                     |
| VoidJumpCapable               |             |                     |
| SignatureVelocity             |             |                     |
| SignatureAngularVelocity      |             |                     |
| ThrusterBoosterDuration       |             |                     |
| ThrusterBoosterCooldown       |             |                     |
| ThrusterBoosterRechargeSpeed  |             |                     |

## Power Stats
| Stat                     | Description | Typical Base Values |
|:-------------------------|:------------|--------------------:|
| PowerWanted              |             |                     |
| PowerProvided            |             |                     |
| BatteryRechargeAmount    |             |                     |
| BreakerTemperatureShift  |             |                     |

## Utility Stats
| Stat                     | Description | Typical Base Values |
|:-------------------------|:------------|--------------------:|
| ProcessingSpeed          |             |                     |
| HealingSpeed             |             |                     |
| ActionCooldown           |             |                     |
| EffectRadius             |             |                     |
| AttractorMaxRange        |             |                     |
| AttractorPullVelocity    |             |                     |
| LifeSupportEffectivity   |             |                     |
| PassiveTemperatureShift  |             |                     |