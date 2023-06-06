define support = Character("Die Taxi Support HotlineTM")
define support_psych = Character("Eine beruhigende Stimme")
define support_diss = Character("Eine strenge Stimme")
define support_actual = Character("Eine gelangweilte Stimme.")

label support:

"Dein Taximeter funktioniert nicht mehr richtig."
"Du rufst die Taxisupport Hotline."

label Wiederwahl:

support "Willkommen, bei der Taxi Support HotlineTM."
support "Wenn sie einen Schaden an ihrem Taxi melden wollen, drücken sie die 1."
support "Wenn sie einen Dissidenten melden wollen, drücken sie die 2."
support "Wenn sie psychologische Hilfe für ihren stressigen Beruf benötigen drücken sie die 3."

menu: 
    "1":
        support "Die Taxi-Support-HotlineTM ist immer für ihre Anliegen zur Stelle."
        support "Ihre Individuelle Hilfe, bei der Taxi-Support-HotlineTM."
        support "Schnell und zuverlässig die Taxi-Support-HotlineTM."
        support "Bitte warten sie während sie zu einem Taxi-Support-Hotline-Operator(C) von der Taxi-Support-HotlineTM verbunden werden..."
        "Warteschlangen Musik beginnt zu spielen."
        menu:
            "Weiter Warten":
                support "Die Taxi-Support-HotlineTM stellt Hunderten von Taxi-Vehicle-Operatives(C), Taxi-Support-Hotline-Operators(C) und Taxi-Support-Hotline-Operator-Deupties(TM) zur Verfügung."
                support "Von unseren vielen Taxi-Support-Hotline-Operation-Towers(C), gehen viele Taxi-Support-Hotline-Transmission-Information-Rays aus, ..."
                support "die in den Taxi-Vehicle-Buisness- bis Economy-Class-Autos, von den Taxi-Support-Information-Collecting-Rods(C) gefangen werden."
                support "Die Taxi-Support-Hotline-Families(C), sind das Grundgestein jedes Taxi-Support-Hotline-Operators."
                support "Taxi-Support-Hotline-Enforcers, sorgen für unsere bekannte Taxi-Support-Hotline-Justice, die Taxi-Support-Hotline-Families vor Taxi-Support-Hotline-Operators und Taxi-Support-Hotline-Deputies schützt, die ihre Arbeit nicht mehr korret ausführen können."
                support "Bitte warten sie während sie zu einem Taxi-Support-Hotline-Operator(C) von der Taxi-Support-HotlineTM verbunden werden..."
                menu:
                    "Weiter warten":
                        support "Die Taxi-Support-HotlineTM beschäftigt hunderte Taxi-Support-Business-Analysists(C), die zusamen mit den Taxi-Support-Hotline-Enforcers die Konkurenz unten und unsere Aktien hoch halten."
                        support "Die freundliche Taxi-Support-Executive-Lobby-GroupTM hält Taxi-Vehicle-Operatives(C) auf den Straßen und andere nicht mit der Taxi-Support-HotlineTM verbundene Verkehrsmittel von den Straßen fern."
                        support "Taxi-Support-Tax- und Finance-Officers(C) sind der primäre Antrieb hinter fem Erfolg der Taxi-Support-HotlineTM-Services."
                        support "Ohne unser breites Netzwerk an Taxi-Support-Executive-Lobby-Group-membersTM, Taxi-Support-Tax-and-Finance-Officers und Taxi-Support-Hotline-Enforcers, ..."
                        support "würde die Taxi-Support-HotlineTM nie die totrale Informations- und Exekutionsgewalt die nötig ist um die Taxi-Support-Hotline-TM zu dem Monopol zu machen, dass es verdient hat zu sein."
                        support "Vergessen sie nicht. Der Erfolg der Taxi-Support-HotlineTM startet mit ihnen, ob sie das wollen oder nicht."
                        menu:
                            "Weiter Warten":
                                support_actual "Ja... was? ..."
                                menu:
                                    "Mein Taximeter ist kaputt":
                                        support_actual "Ich kann sie nicht hören."
                                    "Hallo":
                                        support_actual "Ich kann sie nicht hören."
                                    "Sind sie der Support":
                                        support_actual "Ich kann sie nicht hören."
                                    "...":
                                        support_actual "Ich kann sie nicht hören."
                                support_actual "Warten sie ihr Taximeter ist kaputt, das blockiert die Leitung."
                                support_actual "Ich reparier das..."
                                "Die andere Seite hat aufgelegt"
                                "Nach etwas warten scheint das Taximeter wieder zu funktionieren."
                                "Du fährst weiter."
                                $current_passenger.paying = 0
                                return 
                            "Es Aufgeben":
                                jump Aufgabe
                    "Es Aufgeben":
                        jump Aufgabe
            "Es Aufgeben":
                jump Aufgabe

    "2":
        support_diss "Guten Abend. Sie möchten einen Dissidenten melden?"
        menu: 
            "Ja mein Nachbar Manfred, der ist ein echtes Arschloch":
                support_diss "Notiert. Vielen Dank für ihre Mithilfe."
                support_diss "Sobald wir mehr über ihren Nachbarn erfahren haben werden wir sie wieder kontaktieren."
                return
            "Nein, ich habe mich verdrückt":
                support_diss "Für dieses Vergehen werden sie bestraft!"
                $current_passenger.paying = -game.get_base_fare()
                return 

    "3":
        support "Sie werden jetzt von einem Taxi Hotline Psychology Helper unterstützt"
        support_psych "Alles ist im Einklang"
        support_psych "Um Sie herum ist Natur"
        support_psych "die Vögel zwitschern"
        support_psych "die Gratis Nutzung dieses Services ist abgelaufen."
        support_psych "Vielen Dank für ihr Interesse."
        jump Aufgabe

    "Einen anderen Knopf drücken":
        support "Sie haben den falschen Knopf gedrückt, bitte versuchen sie es erneut."
        jump Wiederwahl

label Aufgabe:
    "Du legst auf."
    "Dein Taximeter scheint noch zu halten, hat dir aber für die letzte Fahrt falsch berechnet."
    $current_passenger.paying = -game.get_base_fare()/2
        

return