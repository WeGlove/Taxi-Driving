define captain = Character("Captain")

label captain:
    you "Bart, Augenklappe, Hakenhand, gestreifter Pulli"
    captain "Ahoi Leichtmatrose, ich muss zur Hafenkneipe, yarr!"
    menu:
        "Aye, aye Captain":
            captain "Yarr, ein guter Rum hält noch den stärkesten Seegler an Deck!"
        "Wie Sie wünschen":
            captain "Du bist langweilig."
        "Okay Segel gesetzt und Kurs auf den Hafen genommen, yarr!":
            captain "Ein Narr hat auf einem Schiff nichts verloren"
    captain "Mood based answer beförderung für besseres vrehalten"
    captain "Aye, bei dem Wetter haben wir heute Abend Eisregen. Zieh die Segel ein <Mood based beförderung>"
    menu:
        "Auf’s Gas drücken":
            captain"Der Mann läuft grün an und übergibt sich in dein Taxi"
        "Langsamer machen":
            captain"In diesen Gewässern gibt es manche die ihren Job schlechter machen als Sie!"
        "Yarr... Captain? es ist eine schöne Nacht für Eisregen?": 
            captain "Yarr, ich habe den leichtesten Leichtmatrosen erwischt."
    captain "Yarr, wir haben unseren Ankerplatz erreicht! Weißt du <Mood based beförderung>, früher da bin ich 20 Schiffen über die See gefahren und hab Fische in allen Weltmeeren an Land gezogen. Heute sind die einzigen Fisch die ich Fange die Dekoration in der Hafenkneipe"
    
    return 
    

