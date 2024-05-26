# Cell Crafter Recipes

Cell crafter recipes are defined similar to regular recipes in `data/<namespace>/recipes/<name>.json` files. The `type` field needs to be set to `minecells:cell_forge_recipe`.

An example Cell Crafter recipe file looks like this:

```json
{
  "type": "minecells:cell_forge_recipe",
  // The category of the recipe. Can be any of:
  // "gear" | "decoration" | "other"
  "category": "gear", 

  // The higher the priority, the higher the recipe will appear in the list
  "priority": 60, 

  // Advancement required to unlock the recipe. 
  // If this field is missing, the recipe is unlocked by default
  "advancement": "minecells:promenade", 

  "input": { 
    // Ingredients required to craft the item. They will be displayed in the same
    // order as they are defined here
    "minecells:cell_infused_steel": 12,
    "minecraft:sugar": 4,
    "minecraft:lapis_lazuli": 8
  },
  "output": { 
    // The output item, in ItemStack json format
    "id": "minecells:assault_shield",
    "Count": 1
  }
}
```