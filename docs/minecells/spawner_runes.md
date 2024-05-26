# Spawner Rune definitions

Spawner Rune definitions are data files that determine which mobs should spawn from certain Spawner Runes, Elite Obelisks or in boss rooms.

They can be individually configured through datapacks.
Their definitions are available in `data/<namespace>/spawner_runes/`

You can define these files in a datapack to override the existing Mine Cells spawner rune definitions,
or to create custom ones.

To summon a Spawner Rune defined in `data/<namespace>/spawner_runes/<name>.json`, use the command:

```
/minecells:spawnerrune spawn <namespace>:<name>
```

## Spawner Rune definition index

The given path is relative to `data/minecells/spawner_runes/`, and is missing the .json suffix

| Path {:style="width:25%"}                                   | Info                                                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Spawner Runes** {: colspan=2 style="text-align:center;"}  |                                                                                 |
| prison                                                      | All Spawner Runes in the Prisoners' Quarters                                    |
| promenade/melee                                             | Melee mobs in Promenade                                                         |
| promenade/ranged                                            | Ranged mobs in Promenade                                                        |
| promenade/protector                                         | The Protector mob of the Promenade                                              |
| ramparts_flies                                              | Buzzcutters in Ramparts                                                         |
| ramparts_melee                                              | Melee mobs in Ramparts                                                          |
| ramparts_ranged                                             | Ranged mobs in Ramparts                                                         |
| ramparts_mixed                                              | Both melee and ranged mobs in Ramparts                                          |
| sweeper                                                     | The Sweeper mob of the Ramparts                                                 |
| **Elite Obelisks** {: colspan=2 style="text-align:center;"} |                                                                                 |
| elite/vine_rune                                             | The Undead Archer summoned in the Promenade, dropping a Vine Rune when defeated |
| **Boss Rooms** {: colspan=2 style="text-align:center;"}     |                                                                                 |
| boss/concierge                                              | The Concierge boss that spawns on the Black Bridge                              |
| boss/conjunctivius                                          | The Conjunctivius boss that spawns in the Insufferable Crypt                    |

## Example Spawner Rune json files

Here's an `example.json` Spawner Rune definition file:

```json
{
  // not yet implemented - should prevent the runes
  // from activating multiple times at once per each nearby player.
  // So it'll have to wait the given time after processing the 1st player,
  // (optional, defaults to 60)
  "cooldown": 120.0

   // distance that the spawned mobs should "spread" in
   // (optional, defaults to 0)
  "spawnDistance": 2.0

  // minimum player distance for the mobs to spawn
  "playerDistance": 16.0,
  "pools": [
    // 1st pool - spawns between 2 and 3 entities, each chosen randomly
    // based on their weights
    {
      "rolls": {
        "type": "uniform",
        "value": {
          "min_inclusive": 2,
          "max_inclusive": 3
        }
      },
      "entries": [
        { "weight": 5, "entity": "minecells:shieldbearer" },
        { "weight": 3, "entity": "minecells:grenadier" },
        { "weight": 2, "entity": "minecells:inquisitor" }
      ]
    },
    // 2nd pool - spawns one Leaping Zombie
    {
      "rolls": 1,
      "entries": [
        {
          // (optional, defaults to 1)
          "weight": 1,
          "entity": "minecells:leaping_zombie"
        }
      ]
    }
  ]
}
```

### Custom attributes

{{since("1.20.1-1.6.1")}}

Modpack developers can tweak the attributes of the entities spawned by Spawner Runes individually.
This means Mine Cells dungeons can be adjusted to the pack's difficulty.

To tweak the attributes, include the optional `attributes` map field in the desired element of `entries`, like so:

```json
{
  "playerDistance": 16.0,
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 1,
          "entity": "minecells:leaping_zombie",
          "attributes": {
            // set max health to 200 points (100 hearts)
            "generic.max_health": 200,    
            // set movement speed to 0.5 
            // (which is quite a bit quicker than the default)
            "generic.movement_speed": 0.5
          }
        }
      ]
    }
  ]
}
```

### Custom NBT

{{since("1.20.1-1.7.0")}}

Arbitrary NBT data can also be appended to spawned mobs.

/// info | NOTE:
  `isElite` and `additionalLootTable` used in this definition are only implemented for Mine Cells entities!  
  You'll have to research your entity-specific and generic NBT tags by yourself to make them work properly.
///

```json
{
  "playerDistance": 16.0,
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "weight": 1,
          "entity": "minecells:undead_archer",
          "attributes": {
            "generic.max_health": 100.0,
            "generic.movement_speed": 0.35,
            "generic.attack_damage": 8.0
          },
          "nbt": {
            // set the isElite NBT tag 
            // (will upscale the entity and display an "ELITE" badge above it)
            "isElite": true, 
            // setup additional loot table for the entity to drop on death
            "additionalLootTable": "minecells:entities/elite/vine_rune" 
          }
        }
      ]
    }
  ]
}
```