﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Du")


# The game starts here.

label start:


    you "You are a taxi driver."
    
    call captain from _call_captain
    call clown from _call_clown
    call dance from _call_dance
    
    you "Hi"
   

    # This ends the game.

    return

