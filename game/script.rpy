﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Du")


# The game starts here.

label start:
    $money = 0

    you "Du bist ein Taxifahrer."

    call baby from _call_baby
    call mime from _call_mime
    call maffay from _call_maffay
    call gameshow from _call_gameshow
    call zeuge from _call_zeuge
    call captain from _call_captain
    call clown from _call_clown
    call dance from _call_dance
    call bobby from _call_bobby
    call bfj from _call_bfj
    
    you "Glückwunsch! Du hast heute [money] CRP verdient!"
   

    # This ends the game.

    return

