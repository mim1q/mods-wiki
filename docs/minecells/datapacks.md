# For Datapack Creators

## Spawner Rune Data

Spawner Runes can be individually configured through datapacks.
Their definitions are available in `data/<namespace>/spawner_runes/`

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

You can define these files in a datapack to override the existing Mine Cells spawner rune definitions,
or to create custom ones.

To summon a Spawner Rune defined in `data/<namespace>/spawner_runes/<name>.json`, use the command:

```
/minecells:spawnerrune spawn <namespace>:<name>
```

### Custom attributes

{{since("1.20.1-1.6.1")}}

Modpack developers can now tweak the attributes of the entities spawned by Spawner Runes individually.
This means Mine Cells dungeons can finally be adjusted to the pack's difficulty.

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
            "generic.max_health": 200,
            "generic.movement_speed": 0.5
          }
        }
      ]
    }
  ]
}
```
