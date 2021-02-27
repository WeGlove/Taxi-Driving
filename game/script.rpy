# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Eileen")


# The game starts here.

label start:


    you "You are a taxi driver."
    
    jump captain
    jump clown
    
    you "Hi"
   

    # This ends the game.

    return

