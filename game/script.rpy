# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init python:
    from game import Game
    game = Game()

define you = Character("Du")

screen MoneyScreen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "[game.money] CRP"
 

label start:
    "Du bist ein Taxifahrer."
    $ base_fare = game.base_fare
    
    show screen MoneyScreen
    
    play music "audio/driving.wav" loop
    
    label day_loop:
        call day from _call_day
        if game.current_day < game.number_of_days:
            jump day_loop
   
    "Das ist alles für den Moment. Schau später wieder vorbei!"

    # This ends the game.

    return

