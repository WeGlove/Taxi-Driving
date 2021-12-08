define bfj = Character("Bahnfahrerjesus")

label bfj: 
    $current_passenger.status["beaten"] = False
    $current_passenger.paying = game.base_fare
    "Ein alter Mann in zerschlissenem Anzug und einem klobigen Koffer steigt ins Taxi ein"
    bfj "Schönen guten Abend. Ich würde gerne in die nächste Stadt wenn's Recht ist."
    menu:
        "Sie sehen aus, wie ein Penner, können Sie mich überhaupt bezahlen?":
            bfj "Bitte, ein Mann meines Berufes kann sich so etwas noch leisten. Sie müssen wissen, ich war mal Professor."
            $current_passenger_stats.paying -= 0.25 * game.base_fare
        "Guten Abend! Das mache ich gerne, steigen Sie ein!":
            bfj "So freundliche Menschen findet man heutzutage wirklich selten"
            $current_passenger.paying += 0.25 * game.base_fare
        "Grummeln und Nicken":
             "Er steigt ein und beginnt dir seine Geschichte zu erzählen"
        "Sagen Sie mal das hört sich jetzt vielleicht komisch an, aber könnte ich ein Foto von Ihnen haben" if game.upgrades["Bilderrahmen"]:
            bfj "Aber sicher! Ein Foto eines Professors wie mir ist sicher Motivation für junge Leute wie Sie!"
            $current_passenger.paying += 0.25 * game.base_fare
            $ game.acquired_images.append(game.current_passenger.call_label)

    bfj  "Wissen Sie, ich war mal Professor der Philosophie, da hab ich viel gemacht mit meiner Schreibmaschine"
    menu:
        "Mhm.":
            bfj "Ich habe seinerzeit viele Forschungasrbeiten veröffentlicht, haben sie schonmal gehört von..."
            "Du drehst die Musik lauter"
            $current_passenger.paying += 0.25 * game.base_fare
        "Der {i}Philosophie{/i}? Das erklärt wenigstens Ihren Aufzug!":
            bfj "Was ist denn an meiner Kleidung auszusetzen? Ihre Generation hat ja wirklich jeden Respekt verloren!"
            $current_passenger.paying -= 0.25 * game.base_fare
        "Was haben Sie denn so geschaffen?":
            bfj "Also mehrere Werke..."
            you "Welches denn spezifisch?"
            bfj "Na mehrere halt!"
    bfj "Die Jungen Leute von heute wissen auch nicht mehr wie man arbeitet, die sind {i} alle{/i} faul!"
    menu:
        "Mhm.":
            "Du drehst die Musik lauter, während er sich weiter aufregt"
        "Wie bitte? {b} ICH ZEIG IHNEN GLEICH MAL WER HIER FAUL IST HERR {i}PROFESSOR{/i}!{/b}":
            "Für einen Mann seines Alters ist dein Passagier ziemlich rüstig, wie du schnell bemerkst. Du wachst auf und ein paar {b}insert Teile oder Accesoires here{\b} fehlen an deinem Taxi!"
            $current_passenger.status["beaten"] = True
            $current_passenger.paying = -0.5 * game.base_fare
        "Ja, es gibt schon echt viele Leute heutzutage.":
            bfj"Vor allem Faule, aber zum Glück gehören Sie ja nicht dazu!"
            $current_passenger.paying += 0.25 * game.base_fare


    