### MLSSE - Mario and Luigi Superstar Saga Editor

This is an editor for the new 3DS release of Mario and Luigi Superstar Saga.

**BACK UP YOUR SAVES**

You can grab your save using [JKSM](https://gbatemp.net/threads/release-jks-savemanager-homebrew-cia-save-manager.413143/), you want the `ML1_001.sav` file for slot one and `ML1_002.sav` for slot two.

Usage is as follows:
```
usage: MLSSE.py [-h] -i IN_FILE [-o OUT_FILE] [--level LEVEL]
                [--mario-level MARIO_LEVEL] [--luigi-level LUIGI_LEVEL]
                [--coins COINS] [--mushrooms MUSHROOMS]
                [--super-mushrooms SUPER_MUSHROOMS]
                [--ultra-mushrooms ULTRA_MUSHROOMS]
                [--max-mushrooms MAX_MUSHROOMS] [--nuts NUTS]
                [--super-nuts SUPER_NUTS] [--ultra-nuts ULTRA_NUTS]
                [--max-nuts MAX_NUTS] [--syrups SYRUPS]
                [--super-syrups SUPER_SYRUPS] [--ultra-syrups ULTRA_SYRUPS]
                [--max-syrups MAX_SYRUPS] [--one-ups ONE_UPS]
                [--one-up-supers ONE_UP_SUPERS]
                [--golden-mushrooms GOLDEN_MUSHROOMS]
                [--refreshing-herbs REFRESHING_HERBS]
                [--boo-biscuits BOO_BISCUITS] [--red-peppers RED_PEPPERS]
                [--green-peppers GREEN_PEPPERS] [--woo-beans WOO_BEANS]
                [--hoo-beans HOO_BEANS] [--chuckle-beans CHUCKLE_BEANS]
                [--hee-beans HEE_BEANS] [--max-coins] [--max-levels]
                [--max-beans] [--max-items] [--max-all] [--list-mario-xp]
                [--list-luigi-xp] [--list-mario-bonuses]
                [--list-luigi-bonuses] [--list-xp] [--list-coins]
                [--list-items] [--list-beans] [--list-all] [--no-backup]

A save editor for Mario and Luigi Superstar Saga for 3DS

optional arguments:
  -h, --help            show this help message and exit
  -o OUT_FILE, --out-file OUT_FILE
                        The output save file
  --no-backup           Disable making a backup of your save

required arguments:
  -i IN_FILE, --in-file IN_FILE
                        The input save file

modifications:
  --level LEVEL         The level you want Mario and Luigi to have
  --mario-level MARIO_LEVEL
                        The level you want Mario to have
  --luigi-level LUIGI_LEVEL
                        The level you want Luigi to have
  --coins COINS         The amount of coins you want
  --mushrooms MUSHROOMS
                        The amount of mushrooms you want
  --super-mushrooms SUPER_MUSHROOMS
                        The amount of super mushrooms you want
  --ultra-mushrooms ULTRA_MUSHROOMS
                        The amount of ultra mushrooms you want
  --max-mushrooms MAX_MUSHROOMS
                        The amount of max mushrooms you want
  --nuts NUTS           The amount of nuts you want
  --super-nuts SUPER_NUTS
                        The amount of super nuts you want
  --ultra-nuts ULTRA_NUTS
                        The amount of ultra nuts you want
  --max-nuts MAX_NUTS   The amount of max nuts you want
  --syrups SYRUPS       The amount of syrups you want
  --super-syrups SUPER_SYRUPS
                        The amount of super syrups you want
  --ultra-syrups ULTRA_SYRUPS
                        The amount of ultra syrups you want
  --max-syrups MAX_SYRUPS
                        The amount of max syrups you want
  --one-ups ONE_UPS     The amount of 1-ups you want
  --one-up-supers ONE_UP_SUPERS
                        The amount of 1-up supers you want
  --golden-mushrooms GOLDEN_MUSHROOMS
                        The amount of golden mushrooms you want
  --refreshing-herbs REFRESHING_HERBS
                        The amount of refreshing herbs you want
  --boo-biscuits BOO_BISCUITS
                        The amount of boo biscuits you want
  --red-peppers RED_PEPPERS
                        The amount of red peppers you want
  --green-peppers GREEN_PEPPERS
                        The amount of green peppers you want
  --woo-beans WOO_BEANS
                        The amount of woo beans you want
  --hoo-beans HOO_BEANS
                        The amount of hoo beans you want
  --chuckle-beans CHUCKLE_BEANS
                        The amount of chuckle beans you want
  --hee-beans HEE_BEANS
                        The amount of hee beans you want
  --max-coins           Set coins to 999999
  --max-levels          Set Mario and Luigi's XP to 999999
  --max-beans           Set all beans to 99
  --max-items           Set all items to 99
  --max-all             Max coins, levels, beans, and items

information:
  --list-mario-xp       List Mario's current XP
  --list-luigi-xp       List Luigi's current XP
  --list-mario-bonuses  List Mario's bonus attributes
  --list-luigi-bonuses  List Luigi's bonus attributes
  --list-xp             List both Mario and Luigi's XP
  --list-coins          List your current coins
  --list-items          List all items
  --list-beans          List all beans
  --list-all            List everything
```