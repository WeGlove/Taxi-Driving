﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Du")


# The game starts here.

label start:


    you "You are a taxi driver."
   
    call captain from _call_captain
    call clown from _call_clown
    call bobby from _call_bobby
    call bfj from _call_bfj
    
    you "Hi"
   

    # This ends the game.

    return

