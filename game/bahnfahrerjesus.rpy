define bfj = Character("Bahnfahrerjesus")

label bfj: 
    "Ein alter Mann in zerschlissenem Anzug und einem klobigen Koffer steigt ins Taxi ein"
    bfj "Schönen guten Abend. Ich würde gerne in die nächste Stadt wenn's Recht ist."
    menu:
        "Sie sehen aus, wie ein Penner, können Sie mich überhaupt bezahlen?":
            bfj "Bitte, ein Mann meines Berufes kann sich so etwas noch leisten. Sie müssen wissen, ich war mal Professor."
        "Guten Abend! Das mache ich gerne, steigen Sie ein!":
            bfj "So freundliche Menschen findet man heutzutage wirklich selten"
        "Grummeln und Nicken":
            bfj "Er steigt ein und beginnt dir seine Geschichte zu erzählen"

    bfj  "Wissen Sie, ich war mal Professor der Philosophie, da hab ich viel gemacht mit meiner Schreibmaschine"
    menu:
        "Mhm.":
            bfj "Ich habe seinerzeit viele Forschungasrbeiten veröffentlicht, haben sie schonmal gehört von..."
            "Du drehst die Musik lauter"
        "Der {i}Philosophie{/i}? Das erklärt wenigstens Ihren Aufzug!":
            "Was ist denn an meiner Kleidung auszusetzen? Ihre Generation hat ja wirklich jeden Respekt verloren!"
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
        "Ja, es gibt schon echt viele Leute heutzutage.":
            bfj"Vor allem faule, aber zum Glück gehören Sie ja nicht dazu!"


    