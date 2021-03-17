# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Du")


# The game starts here.

label start:


    you "You are a taxi driver."
<<<<<<< HEAD
    call zeuge
=======
   
    call gameshow from _call_gameshow
>>>>>>> 54ef728be8b43cc5fe054d3a9e22be797ec1b2a8
    call captain from _call_captain
    call clown from _call_clown
    call dance from _call_dance
    call bobby from _call_bobby
    call bfj from _call_bfj
    
    you "Hi"
   

    # This ends the game.

    return

