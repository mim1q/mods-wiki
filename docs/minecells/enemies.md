# Enemies of Mine Cells

All of these enemies aim to be faithful representations of the monster of Dead Cells.
The drops aren't very exciting right now, but will likely be improved upon as the mod's
development progresses!

---

<!-- ## Leaping Zombie

![Leaping Zombie](img/mobs/leaping_zombie.jpg){: .side-image }

The basic enemy of Mine Cells. Really common, attacks in melee range or by jumping at you.

/// info | Spawns in

- Overworld (portal structure)
- [Prisoners' Quarters](./dimensions.md#prisoners-quarters)
- [Promenade of The Condemned](./dimensions.md#promenade-of-the-condemed)
  ///

/// info | Drops

- Rotten Flesh
- Guts
- Monster's Eye (rare)
  ///

---

## Grenadier

![Grenadier](img/mobs/grenadier.jpg){: .side-image }

Throws exploding bombs in your direction.

/// info | Spawns in

- Overworld (portal structure)
- [Prisoners' Quarters](./dimensions.md#prisoners-quarters)
- [Promenade of The Condemned](./dimensions.md#promenade-of-the-condemed)
  ///

/// info | Drops

- Rotten Flesh
- Guts
- Monster's Eye (rare)
  ///

---

## Shieldbearer

![Shieldbearer](img/mobs/shieldbearer.jpg){: .side-image }

Charges their shield at you. Cannot be attacked from the front.

/// info | Spawns in

- Overworld (portal structure)
- [Prisoners' Quarters](./dimensions.md#prisoners-quarters)
  ///

/// info | Drops

- Rotten Flesh
- Guts
- Monster's Eye (rare)
  ///

---

## Undead Archer

![Undead Archer](img/mobs/undead_archer.jpg){: .side-image }

Shoots arrows. Pretty much like a regular Skeleton.

/// info | Spawns in

- [Prisoners' Quarters](./dimensions.md#prisoners-quarters)
  ///

/// info | Drops

- Rotten Flesh
- Guts
- Monster's Eye (rare)
  ///

---

## Runner

![Runner](img/mobs/runner.jpg){: .side-image }

Performs a melee attack with a long windup that deals a ton of damage. Can teleport to you if you're far.

/// info | Spawns in

- [Promenade of The Condemned](./dimensions.md#promenade-of-the-condemed)
  ///

/// info | Drops

- Phaser (rare)
  ///

---

## Mutated Bat

![Mutated Bat](img/mobs/mutated_bat.jpg){: .side-image }

Has very little health but spawns in groups. Flies around you and dashes to attack.

/// info | Spawns in

- [Promenade of The Condemned](./dimensions.md#promenade-of-the-condemed)
  ///

---

## Protector

![Protector](img/mobs/protector.jpg){: .side-image }

Grants nearby hostile mobs the [Protected](status-effects.md#protected) status effect.
Does not attack by itself.

/// info | Spawns in

- [Promenade of The Condemned](./dimensions.md#promenade-of-the-condemed)
  ///

---

## Inquisitor

![Inquisitor](img/mobs/inquisitor.jpg){: .side-image }

Shoots magic orbs that can phase through walls.

/// info | Spawns in

- Overworld (portal structure)
  ///

---

## Sewers' Tentacle

![Shieldbearer](img/mobs/sewers_tentacle.jpg){: .side-image }

Burrows under the ground and navigates toward you. Will unburrow to strike the player or perform a long-range charge if the path is clear.

/// info | Spawns in

- [Insufferable Crypt](./dimensions.md#insufferable-crypt)
  /// -->

---

{{minecells_mob("Leaping Zombie",
  description = "The basic enemy of Mine Cells. Really common, attacks in melee range or by jumping at you.",
  biomes = ["Prisoners' Quarters", "Promenade of the Condemned"],
  drops = [("Rotten Flesh", ""), ("Guts", ""), ("Monster's Eye", "")]
)}}

---

{{minecells_mob("Grenadier",
  description = "Throws exploding bombs in your direction.",
  biomes = ["Prisoners' Quarters", "Promenade of the Condemned"],
  drops = [("Rotten Flesh", ""), ("Guts", ""), ("Monster's Eye", "")]
)}}

---

{{minecells_mob("Shieldbearer",
  description = "Charges their shield at you. Cannot be attacked from the front.",
  biomes = ["Prisoners' Quarters"],
  drops = [("Rotten Flesh", ""), ("Guts", ""), ("Monster's Eye", "")]
)}}

---

{{minecells_mob("Undead Archer",
  description = "Shoots arrows. Pretty much like a regular Skeleton.",
  biomes = ["Prisoners' Quarters"],
  drops = [("Rotten Flesh", ""), ("Guts", ""), ("Monster's Eye", "")]
)}}

---

{{minecells_mob("Runner",
  description = "Performs a melee attack with a long windup that deals a ton of damage. Can teleport to you if you're far.",
  biomes = ["Promenade of the Condemned"],
  drops = [("Phaser", "weapons")]
)}}

---

{{minecells_mob("Mutated Bat",
  description = "Has little health but is quite annoying to deal with.
                 Flies around its target, dashing towards it to attack.",
  biomes = ["Promenade of the Condemned"]
)}}

---

{{minecells_mob("Protector",
  description = "Grants nearby hostile mobs the [Protected](status-effects.md#protected) status effect.
                 Does not attack by itself.",
  biomes = ["Promenade of the Condemned"]
)}}

---

{{minecells_mob("Inquisitor",
  description = "Shoots magic orbs that can phase through walls.",
  biomes = ["Overworld", "Ramparts"]
)}}

---

{{minecells_mob("Sewers' Tentacle",
  description = "Burrows under the ground and navigates toward you. Will unburrow to strike the player or perform a long-range charge if the path is clear.",
  biomes = ["Insufferable Crypt"]
)}}

---

{{minecells_mob("Sweeper",
  description = "Sweeps",
  biomes = ["Ramparts"],
  since_version = "1.20.1-1.6.0"
)}}

---

{{minecells_mob("Buzzcutter",
  description = "Buzzes",
  biomes = ["Ramparts"],
  since_version = "1.20.1-1.6.0"
)}}
