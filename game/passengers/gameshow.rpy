define gameshow = Character("Host")

label gameshow:
    "Eine Frau in Make-Up und einem heruntergekommenen Anzug steigt in das Taxi."
    gameshow "Hallo und herzlich Willkommen meine Damen und Herren zu unserer heutigen Gameshow!"
    gameshow "Sie sind unser heutiger Gast. Wie fühlen Sie sich?"
    menu:
        "Gute Frau, das hier ist ein Taxi.":
            gameshow "Die Frau lacht"
            gameshow "Aber nicht doch, sehen Sie sich doch um!"
            gameshow "Überall um uns herum sind Scheinwerfer und solches Qualitätspolster bekommen Sie nur in unserem Studio!"
        "Ich fühle mich gut, ich habe mich lange auf meinen Auftritt vorbereitet":
            gameshow "Na, das wollen wir doch hören."
        "..., was?":
            "Die Frau lacht"
            gameshow "Ja, so ist das meine Damen und Herren, diese Gameshow lässt Sie sprachlos!"
    gameshow "Hier also die Regeln für das heutige Spiel."
    gameshow "Sie müssen so schnell wie möglich von hier bis zum Mensch-Rathaus und dabei 2 knifflige Fragen beantworten."
    gameshow "Wenn Sie sie korrekt beantworten können, wartet ein Geldpreis auf Sie!"
    gameshow "Haben Sie die Regeln verstanden?"
    menu:
        "Ja":
           "Fantstisch, fangen wir an!"
        "Nein":
           "Fantstisch, fangen wir an!"
        "Entschuldigung?":
            "Fantstisch, fangen wir an!"
    gameshow "Kommen wir zu ersten Frage, keine Angst wir starten ganz einfach."
    gameshow "Was ist 11*11"
    menu:
        "A) 121":
             gameshow "Korrekt! Herzlichen Glückwunsch, damit haben sie sich den ersten von zwei Geldpreisen verdient"
             $current_passenger.paying += game.base_fare / 4
        "B) 112":
            gameshow "Netter Versuch, aber leider falsch!"
        "C) Ein Stern zwischen zwei Elfern":
            gameshow "Korrekt! Herzlichen Glückwunsch, damit haben sie sich den ersten von zwei Geldpreisen verdient"
            $current_passenger.paying += game.base_fare / 4
        "D) Eine Zahl":
            gameshow "Korrekt! Herzlichen Glückwunsch, damit haben sie sich den ersten von zwei Geldpreisen verdient"
            $current_passenger.paying += game.base_fare / 4
    
    gameshow "Kommen wir zur zweiten und schwierigsten Frage..."
    gameshow "Wenn Sie eine Hit Gameshow leiten würden, aber in ihrer Lebensituation komplett verzweifelt sind, würden Sie:"
    menu:
        "A) Zum Rathaus fahren um sich Hilfe zu holen":
            gameshow "Nun, meine Damen und Herren dann müssen die Quoten ja grauenvoll sein"
            "Sie zwinkert in die Luft"
            gameshow "Aber korrekt, den zweiten Geldpreis haben sie sich wirklich verdient"
            $current_passenger.paying += game.base_fare / 4
        "B) Zum nächsten Supermarkt fahren, um sich Alkoholische Getränke zu kaufen":
            gameshow "Nein..., welcher Gameshowhost trinkt denn bei der Arbeit?"
            "Sie schaut mit einem vielsagenden Blick in eine Richtung in der nichts ist."
            gameshow "Tut mir Leid der Preis bleibt für Sie heute aus."
        "C) Zum Rathaus fahren, um ihre Gameshow den Mitgliedern zu präsentieren":
            gameshow "Haha! Nur Mut zum Risiko, so muss das sein!"
            gameshow "Den Geldpreis haben Sie sich verdient!"
            $current_passenger.paying += game.base_fare / 4
        "D) Zum Rathaus fahren um einen Anschlag zu verüben":
            gameshow "Es tut mir Leid meine Damen und Herren ich habe grade Wort aus der Regie bekommen das wir das geplante Programm unterbrechen müssen!"
            gameshow "Damit fällt leider auch der Geldpresis weg der für Sie ausgelegt war, es tut uns Leid!"
    
    gameshow "Und das war unsere Zeit für heute. Danke meine Damen und Herren das sie auch heute wieder eingeschaltet haben und natürlich auch Danke an unseren Teilnehmer"
    gameshow "Vielen Dank und gute Nacht!"
    return

