# Updating Mine Cells

When updating Mine Cells you should **reset the dimensions**.

It's highly recommended to do it when the major version of Mine Cells changes, that is when the first or second number in the version name increases.

e.g:

<div markdown class="highlight-italics">

|From   |To     | Dimension reset recommended? | 
|-------|-------|------------------------------|
|1.4.1  |1.4.2  |no                            |
|1.5.0  |1.5.8  |no                            |
|1.*4*.0|1.*5*.0|yes                           |
|1.*4*.2|1.*5*.1|yes                           |
|*1*.2.0|*2*.1.0|yes                           |

</div>

All Mine Cells-related player data gets wiped after the major updates. If you want to be sure it got wiped,
or if you forgot to reset the dimmensions immediately you can run the `/minecells:wipe_data` command to
completely clear all players' Mine Cells data. Only do it after you have deleted the old dimension folders or
if the data somehow got corrupted.

/// info | On singleplayer worlds

1. Select the world you want to play on
2. Click Edit
3. Click Open World Folder
4. Open the `dimensions` folder, then delete the `minecells` folder  
    - If you don't want to reset every dimension, you can delete only the selected directories under `minecells`
    - Only do that if you are **sure** the dimensions don't need a reset (the changelogs should say which ones are necessary)
///

/// info | As a server administrator

1. Navigate to your server's root folder
2. Open the world directory
3. Delete the directories, like in step 4. above

If only one of the players is experiencing issues related to dimension teleportation etc. you can wipe only their
data by using the `/minecells:clear_data <player>` command

///
