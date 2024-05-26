# Common issues with Mine Cells

## I am experiencing issues when entering the Ramparts

If you are getting teleported to an unusual place, or are experiencing weird behavior when entering the Ramparts, you should **set the `disableFallProtection` option to `true` in the `minecells-common.json5` config file.**

## The game crashes when I enter / walk around the Promenade

This can happen in older versions of the mod due to a bug in Protector entities' code.
You can either **update to the latest available version**, or **downgrade Fabric Loader to a version below 0.15.0**.

## I can't find the tentacles that Conjunctivius spawned

The tentacles can rarely get stuck if you're unlucky. They should die out on their own after a few minutes, so **waiting might be your best choice**. 

If you're in a hurry and have admin permissions, you can **use the `/kill @e[type=minecells:sewers_tentacle,distance=..128]` command to instantly remove them.**

## I get stuck in a wall / the dungeon is missing when I enter a Mine Cells dimension 

This happens with older versions of Mine Cells if you have Sparse Structures installed. You can either figure out a custom config to exclude Mine Cells structures from that mod's configuration, remove Sparse Structures, or **update to the latest version of Mine Cells, where a workaround for this issue was implemented.**