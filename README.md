## AOEII Discord Bot

This is a simple Discord Bot built with discord.py which returns a randomly selected civilisation or location map for Age of Empires II HD Edition.

#### Required liberies

```
configparser
discord.py
```

#### How to use

+ Store your discord token and channel information in the 'config.ini' file.


Once the bot has been invited to the channel the bot can be called by using the following commands.


+ !civ
  + This will return a randomly selected civilisation
+ !map
  + This will return a randomly selected location map
+ !3
  + This will return a randomly selcted location map out of the three most played location maps
    + Blackforest, Islands, Team Islands
+ !roll
  + This takes in two parameters (number of die, number of sides) then returns the value from the dice rolls
+ !mitch
  + This is a bonus command which will return a randomly selected dad joke
