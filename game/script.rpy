# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Eileen")
define captain = Character("Captain")


# The game starts here.

label start:


    you "You are a taxi driver."
    
    jump captain
    
    you "Hi"
   

    # This ends the game.

    return
    
label captain:
    you "Bart, Augenklappe, Hakenhand, gestreifter Pulli"
    captain "Ahoi Leichtmatrose, ich muss zur Hafenkneipe, yarr!"
    menu:
        "Aye, aye Captain":
            "Yee"
        "Wie Sie wünschen":
            "Yee"
        "Okay Segel gesetzt und Kurs auf den Hafen genommen, yarr!":
            "Yee"
    captain "Mood based answer beförderung für besseres vrehalten"
    captain "Aye, bei dem Wetter haben wir heute Abend Eisregen. Zieh die Segel ein [Mood based beförderung]"
    menu:
        "Auf’s Gas drücken":
            "Yee"
        "Langsamer machen":
            "Yee"
        "Yarr... Captain? es ist eine schöne Nacht für Eisregen?": 
            "Yee"
    captain "Yarr, wir haben unseren Ankerplatz erreicht! Weißt du [Mood based beförderung], früher da bin ich 20 Schiffen über die See gefahren und hab Fische in allen Weltmeeren an Land gezogen. Heute sind die einzigen Fisch die ich Fange die Dekoration in der Hafenkneipe"

    

