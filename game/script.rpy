# The script of the game goes in this file.

init python:
    from game import Game
    game = Game()

define you = Character("Du")

# Shows the Money the Charater currently has
screen MoneyScreen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "[game.money] CRP"


# Shows the items the player currently has
screen InventoryScreen():
    tag InventoryScreen
    $ test = game.get_acquired_upgrades()
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            textbutton "Inventar verlassen" action Hide("InventoryScreen")
            for item in test:
                if item == "Bilderrahmen":
                    textbutton "Bilderrahmen" action Show("BilderrahmenScreen")
                else:
                    text item

# Shows an image of the players favorite chars.   
screen BilderrahmenScreen():
    tag BilderrahmenScreen
    frame:
        xalign 0.5 yalign 0.5
        $acquired = game.acquired_images
        $lenac = len(acquired)
        if (lenac == 0):
            text "Du hast keine Bilder um sie in deinen Bilderrahmen zu füllen. Versuch doch mal einen Passagier nach einem zu fragen!"
        else :
            vbox:
                text "Wähle ein Bild um es in den Bilderrahmen zu füllen. Dieser Passagier wird dir das doppelte zahlen! WARNUNG: DIESER EFFEKT VERDOPPELT IM MOMENT AUCH NEGATIVE  WERTE"
                for photo in acquired:
                    textbutton photo action SetVariable("game.get_favorite_passenger()", photo)
        frame:
            xalign 0.5 yalign 0.9
            textbutton "Bilderrahmen-Menü verlassen" action Hide("BilderrahmenScreen")

screen InventoryButtonScreen():
    frame:
        xalign 1.0 yalign 1.0
        vbox:
            textbutton "Inventar" action Show("InventoryScreen")
 

# GAME STARTS HERE
label start:
    "Du bist ein Taxifahrer."

    $base_fare = game.get_base_fare()

    show screen MoneyScreen
    show screen InventoryButtonScreen
    
    play music "audio/LearnAbout-Drive.ogg" loop
    
    label day_loop:
        call day from _call_day
        if game.get_current_day() < game.get_number_of_days():
            jump day_loop
   
    "Das ist alles für den Moment. Schau später wieder vorbei!"

    # GAME ENDS HERE

    return

