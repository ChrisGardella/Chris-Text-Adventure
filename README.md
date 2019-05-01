# Chris-Text-Adventure

This program is a text adventure game.

The way this game works is there will be a series of events where the player can choose what to do from two options. Depending on what the players choose it will change the story. Some choices will result in instant game over and will end the program and the player must start over. The way I made this game work was using the Random library. I imported random, which is already included with python in order to choose what type of character the player is, what enemy would spawn as well as the damage amount when fighting.

In order for this game to work properly you have to use Python version 3.7, if it is an earlier version the user inputs will not work and the program will not run. Also remember to type your answers correctly or it will not work: for example you cannot put "cheese" for a yes or no question.

As far as character type goes it has no effect besides a description of your character.

The random enemies have no difference besides their description.

When it comes to the battle sequence, both the player and enemy have 15 health, they each do random damage based on the range. The player will tend to do the most damage but there is still the chance of losing.
