define captain = Character("Captain")

label captain:
    $current_passenger.status["storytime"] = False
    "Ein Mann mit Kotletten, Augenklappe, Hakenhand und gestreiftem Pulli steigt in dein Taxi."
    captain "Ahoi Leichtmatrose, ich muss zur Hafenkneipe, yarr!"
    menu:
        "Aye, aye Captain":
            captain "Yarr, ein guter Rum hält noch den stärkesten Segler an Deck!"
            $current_passenger.paying += game.base_fare / 4
        "Wie Sie wünschen":
            captain "Oh, du bist langweilig."
        "Okay Segel gesetzt und Kurs auf den Hafen genommen, yarr!":
            captain "Ein Narr hat auf einem Schiff nichts verloren, Landratte!"
            $current_passenger.paying -= game.base_fare / 4
    captain "Aye, bei dem Wetter haben wir heute Abend Eisregen. Zieh die Segel ein Leichtmatrose!"
    menu:
        "Auf’s Gas drücken":
            captain"Der Mann läuft grün an und übergibt sich in deinem Taxi"
            $current_passenger.paying -= game.base_fare * 0.75
        "Langsamer machen":
            captain "In diesen Gewässern gibt es manche die ihren Job schlechter machen als Sie!"
            $current_passenger.paying += game.base_fare / 4
        "Yarr... Captain? es ist eine schöne Nacht für Eisregen?": 
            captain "Yarr, ich habe den leichtesten Leichtmatrosen erwischt."
    captain "Yarr, Landratte. Willst du mal etwas echtes Seemansgarn hören?"
    menu:
        "Aye, Captain!":
            captain "Yarr, es war vor 20 Jahren, als ich noch Captain der Nusschale war"
            captain "Damals waren wir auf der Jagd nach der großen Flunder!"
            captain "Fünf Monate hatten wir bei Wind und Wetter die Meere durchkreuzt um das Biest zu finden, aber es wollte sich einfach nicht zeigen"
            captain "Als uns dann die Vorräte zu neige gingen und wir drohten mit leerer Hand zurückzukehren fasste ich einen Plan."
            captain "Einer meiner Männer, das musst du dir mal vorstellen Leichtmatrose, hat versucht mein Schiff zu meutern"
            captain "Ebenen jenen Mann band ich mit einem Seil fest und ließ ihn vor dem Schiff ins Wasser baumeln als Köder."
            captain "Und siehe da Leichtmatorse! Die Flunder erschien um den armen Mann aus der Bedrängnis zu retten."
            captain "Aber just in dem Moment als ich die Harpune feuern wollte hörten wir Sirenen und ein Schiff erschien aus dem Nebel."
            captain "Die Küstenwache hat mir danach die Lizenz zum Fischen auf Grund von Verstößen gegen die Menschenrechte entzogen..."
            "Nachdem Der Captain seine Geschichte beendet hat wart ihr schon eine gute halbe Stunde auf dem Kneipenparplatz, wodurch du neinen nächsten Kunden verpasst."
            $current_passenger.status["storytime"] = True
            $game.skip_a_character(1)
            $current_passenger.paying += game.base_fare * 0.75
        "Nein, ich kann die See nicht ausstehen":
            captain "Yarr, du bist genauso salzig wie die See..."
        "Nein danke, ich muss mich aufs Fahren konzentrieren":
            captain "Aye, Landratte, du wärst ein guter Steuermann auf meinem Schiff gewesen."
            captain "Yarr, wir haben unseren Ankerplatz erreicht! Weißt du Leichtmatrose, früher da bin ich 20 Schiffen über die See gefahren und hab Fische in allen Weltmeeren an Land gezogen. Heute sind die einzigen Fisch die ich Fange die Dekoration in der Hafenkneipe"
            $current_passenger.paying += game.base_fare / 4
    return 
    

