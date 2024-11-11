# Value Calculators

## Overview

Value Calculators are a tool in the Gimm1q library that developers can use to **allow customizing equations for calculating a given value**.  
This is useful when you want to let players or modpack developers tweak the scaling of weapon damage, change the damage of a mob's given attack, or customize the way any other value in your mod is calculated.

/// warning | Warning for mod developers:

Due to the datapack-backed nature of this system, calculations can only be done after the world is loaded.That means no calculations can be done during the initialization of the mod. Make sure to handle this in your code by postponing any calculations until the world is loaded.

[This event](#reload-event) may be useful in these cases.

///

## Value Calculators' Goals:

- Provide a simple-to-use API for developers to evaluate arbitrary, datapack-or-config-defined equations at runtime
- Allow giving names to these equations, so they can be easily referenced in-code
- Allow for easy tweaking of equations by players or modpack developers

## Value Calculators' Non-Goals:

- Provide a GUI for editing or viewing equations
- Allow user to change any existing equation in the game. **Only equations explicitly defined by the developer as Value Calculators can be customized.**

## Example Use Case

Imagine a mod that adds a weapon, which deals more damage the more speed the player has. Let's say this is a part of the weapon's class:

```java
private static final ValueCalculator DAMAGE_CALCULATOR = ValueCalculator.of(
    // The identifier of the Value Calculator file
    MyMod.id("weapons/speed_sword"),
    // The name of the equation
    "damage",
    // The fallback value, in case the equation is missing or fails to evaluate
    8.0
);

// ...

public float getDamage(
    PlayerEntity player,
    ItemStack stack,
    LivingEntity target
) {
    return DAMAGE_CALCULATOR.calculate(
        ValueCalculatorContext.create()
            .with(ValueCalculatorParameter.HOLDER, player)
            .with(ValueCalculatorParameter.HOLDER_STACK, stack)
            .with(ValueCalculatorParameter.TARGET, target)
    );
}
```

Notice how the actual calculation of the damage is not defined anywhere in this code. The `ValueCalculator` here is a utility object that will look up the equation with the given identifier and name, and evaluate it with the provided context.

Value Calculator data files can be included with both datapacks and config files. **It is generally recommended that mod developers use datapacks to define Value Calculators, and players and modpack developers use config files to tweak them.**

The corresponding `data/mod_id/value_calculators/weapons/speed_sword.json` or `config/mod_id/value_calculators/weapons/speed_sword.json` file might look like this:

```json
{
  "variables": {
    // This section can be used to retrieve values from the context
    // Variables can be used in other variables or equations, by name

    // This variable is named "player_speed", will hold the player's
    // movement speed attribute value, and can be used
    "player_speed": {
      // The type of the variable source. This one is used to retrieve
      // attributes, but there's also ones for accessing enchantments,
      // nbt data and more
      "type": "gimm1q:attribute",
      // The attribute to retrieve.
      "attribute": "generic.movement_speed",
      // The selector (which entity to get the attribute from)
      // Can be "this" (the holder) or "target"
      "selector": "this"
    }
  },
  "equations": {
    // This section defines the actual equations that can be retrieved
    // by the ValueCalculator.
    // It can hold either equations as strings (like below), or plain
    // numeric values.
    "damage": "8.0 + player_speed * 2.0"
  }
}
```

All of the different types of variables are documented in [this class](https://github.com/mim1q/gimm1q/blob/value-calculators/src/main/java/dev/mim1q/gimm1q/valuecalculators/variables/VariableSourceTypes.java)

## Usage

If you have any questions about how to use Value Calculators as a developer, or how to tweak them as a player or modpack developer, please join the [Mim1q's Mods Discord Server](https://discord.gg/6TjQbSjbuB) and ask there. I'll be happy to help you out!

### Developers

The [Example Use Case section](#example-use-case) above shows a simple example of how to use Value Calculators in your mod. Most of the code in Gimm1q related to Value Calculators has documentation, so you can refer to that for more information.

Advanced usage examples:

- For examples on creating your own variable sources, see the [`VariableSourceTypes`](https://github.com/mim1q/gimm1q/blob/value-calculators/src/main/java/dev/mim1q/gimm1q/valuecalculators/variables/VariableSourceTypes.java) class
- For examples on using custom context parameters for your variable sources, see the [`ValueCalculatorParameter`](https://github.com/mim1q/gimm1q/blob/value-calculators/src/main/java/dev/mim1q/gimm1q/valuecalculators/parameters/ValueCalculatorParameter.java) class
- You can pass in "Magic Variables" through the context, which will be accessible in the equations, but will not be explicitly defined in the Value Calculator file. It is your responsibility to use them only when necessary and make it known to the user that they exist for a given equation. For an example, see [this Java code](https://github.com/mim1q/MineCells/blob/463e32ed1d2c4f0cce50b9f30e540587962c29f3/src/main/java/com/github/mim1q/minecells/entity/nonliving/projectile/CustomArrowEntity.java#L124) and [this JSON file](https://github.com/mim1q/MineCells/blob/463e32ed1d2c4f0cce50b9f30e540587962c29f3/src/main/resources/data/minecells/value_calculators/ranged/global.json). For consistency and clarity, please name these variables using `UPPERCASE_SNAKE_CASE`.

#### Reload event

Gimm1q provides a `ValueCalculatorsReloadedCallback.EVENT` event that you can subscribe to in order to execute code after the Value Calculators are reloaded (e.g. when entering a world or reloading datapacks)

When this event is fired, the Value Calculator definitions get sent over to the client, so any calculations done on their side should match the server's (Warning: some variable sources are only available on the server side, and will use the fallback value on the client side)

### Players and Modpack Developers

When you open a world with any mod using Value Calculators, a
`config/<mod_id>/value_calculators` folder will be created in your config directory. This folder will contain templates for all the Value Calculator files that are present in the mod's datapacks. In order to tweak the equations:

- Copy any given `<name>.template.json` file to a new file named `<name>.json`, in the same directory
- Tweak the equations in the new file as you see fit
- Most people will not need to touch the `variables` section, but if you do, refer to the [`VariableSourceTypes` documentation](https://github.com/mim1q/gimm1q/blob/value-calculators/src/main/java/dev/mim1q/gimm1q/valuecalculators/variables/VariableSourceTypes.java)
- Remember that in some cases, the variables may not work if the developer hasn't provided the corresponding context parameters, or if the parameters are not available in a given situation

## Performance

Of course - this approach to calculating values is less performant than hardcoding equations. The overall impact of using this system will depend on multiple factors, but shouldn't cause severe performance issues if handled responsibly. Despite this, consider whether the performance-flexibility tradeoff is worth it for your mod.

I recommend caching the the results of the calculations when dynamic calculations are not crucial (such as in item tooltips, etc.), so they're not recalculated every frame or tick.

I used the [Crunch](https://github.com/boxbeam/Crunch) library to evaluate the equations, as it was the fastest one of this kind that I could find. Refer to its README's [Performance section](https://github.com/boxbeam/Crunch?tab=readme-ov-file#performance) to see how it performs compared to other libraries.
