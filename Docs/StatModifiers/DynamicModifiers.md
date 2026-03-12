# Dynamic Modifiers
Modifiers can be configured to be dynamic, meaning they will scale and/or toggle depending on other rules. 
There are two types of dynamic modifiers: Dynamic Conditions and Dynamic Values.

Each modifier can only have one dynamic condition and one dynamic value.

## Dynamic Conditions
Dynamic conditions will enable or disable the modifier depending on a certain condition. 

The dynamic condition must be wrapped inside of a `"dynamic_condition"` token, which must include
a `"type"` token to specify which type of condition it is.

All dynamic conditions can be inverted by adding the "invert" token to the JSON data.
Normally, the modifier is enabled **when** the condition is met. 
Invert makes it so the modifier is instead enabled **when not** met.

The below modifier example will increase damage of energy weapons by 100% while the Void Drive is charging, 
and decrease by 50% when not charging using the inverted condition.

```json
{
  "modifiers": [
    {
      "name": "Damage",
      "amount": 1.0,
      "type": "AdditiveMultiplier",
      "tag_config": {
        "required": [
          "DamageType_Energy"
        ]
      },
      "dynamic_condition": {
        "type": "VoidDriveCharging"
      }
    },
    {
      "name": "Damage",
      "amount": -0.5,
      "type": "AdditiveMultiplier",
      "tag_config": {
        "required": [
          "DamageType_Energy"
        ]
      },
      "dynamic_condition": {
        "type": "VoidDriveCharging",
        "invert": true
      }
    }
  ]
}
```

### **Void Drive Charging**
`"type": "VoidDriveCharging"` \
Enables the modifier when the void drive is charging.

### **Thruster Boosters Active**
`"type": "ThrusterBooster"` \
Enables the modifier when the ship is actively boosted by thruster boosters.

### **Single Player**
`"type": "SinglePlayer"` \
Enables the modifier when only a single player is in the room.

### **Resource Count**
`"type": "ResourceCount"` \
Enables the modifier if a specified resource count is less than or greater than a certain threshold.

By default will enable when value is **greater** than the threshold. 
If inverted, will instead enable when less than the threshold.
Value equal to the threshold will not enable the condition in either case.

#### **Properties**
`"resource_type"` \
Which resource the condition is based on. Can be `"Alloys"` or `"Biomass"`.

`"threshold"` \
Integer value threshold for the condition.

### **Power Overdraw**
`"type": "PowerOverdraw"` \
Enables the modifier if the ship is using more power than is being generated.

### **Charged Battery Magazine**
`"type": "ChargedBatteryMagazine"` \
Enables the modifier if the object has a battery magazine with a battery that has any charge left.

### **Room Temperature**
`"type": "CellModuleTemperatureThreshold"` \
Checks the atmosphere data for the room the object is in, and enables the modifier if the temperature (°C) 
is less than or greater than a certain threshold.

By default will enable when value is **less** than the threshold.
If inverted, will instead enable when greater than the threshold.
Value equal to the threshold will not enable the condition in either case.

#### **Properties**
`"threshold"` \
Integer value threshold for the condition. \
Default value: 0

### **Circuit Breakers Flipped**
`"type": "BreakersFlipped"` \
Enables the modifier if any circuit breakers are inactive.

A circuit breaker is **active** when it is nominal (green icon). \
A circuit breaker is **inactive** when it needs a player to flip the lever (red icon). \

---
## Dynamic Values
Dynamic values will scale a modifier based on another external value. 

Each dynamic values must be wrapped inside of a `"dynamic_value"` token, which must include
a `"type"` token to specify which type of value it is.

### **Shared Properties**
The following properties can be specified on all dynamic scaling values.

`"base_value"` \
Base value provided per count (e.g., 0.05 for 5% per count).

`"scaling_type"` \
How the dynamic modifier should scale with the dynamic base value. This can be either:
- `"Linear"`: modifier will scale linearly with the dynamic base value.
- `"Exponential"`: modifier will scale exponentially with the dynamic base value.
- `"Diminishing"`: modifier will scale with diminishing returns based on the base value.

`"diminishing_cap"` \
If the scaling type is `"Diminishing"`, then this token can be used to specify the asymptotic limit for the 
diminishing returns (e.g., 0.95 to never reach 100%). \
Default value: 0.95

### **Ship Speed**
`"type": "ShipSpeed"` \
Scales the base value for each covered threshold of ship's current speed.

#### **Properties**
`"tier_threshold"` \
The threshold of speed (m/s) the modifier is scaled by.
The base value is scaled on each count of the threshold: _speed / threshold_ \
Default value: 10.0

### **Resource Count**
`"type": "ResourceCount"` \
Scales the base value for each covered threshold of a resource.

#### **Properties**
`"tier_threshold"` \
The threshold of resource count the modifier is scaled by.
The base value is scaled on each count of the threshold: _resource count / threshold_ \
Default value: 10.0

`"resource_type"` \
Which resource the value is based on. Can be `"Alloys"` or `"Biomass"`. \
Default value: Alloys

`"max_tiers"` \
Defines a cap for how many counts of the resource the modifier can be scaled by.\
If the max tiers is less than 1, then the scaling will be uncapped. \
Default value: -1

### **Power Usage**
`"type": "PowerUsage"` \
Scales the base value for each point of available or overdrawn power.

#### **Properties**
`"available_power"` \
If `true` then will scale based on how much power is currently available in surplus: _power generated - power used_ \
If `false` then will scale based on how much power is currently overdrawn: _power used - power generated_ \
Default value: false

### **Defect Count**
`"type": "DefectCount"` \
Scales the base value for each covered active or inactive defect across the ship.

#### **Properties**
`"active_defects"` \
If `true` then will scale based on how many defects are active. \
If `false` then will scale based on how many defects are inactive \
Default value: false

### **Breakers Flipped**
`"type": "BreakersFlipped"` \
Scales the base value for each active / inactive circuit breaker. \

A circuit breaker is **active** when it is nominal (green icon). \
A circuit breaker is **inactive** when it needs a player to flip the lever (red icon). \

#### **Properties**
`"active_breakers"` \
If `true` then will scale based on how many circuit breakers are active. \
If `false` then will scale based on how many circuit breakers are inactive. \
Default value: false