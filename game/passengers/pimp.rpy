define faustings = Character("Max Faustings")


label passenger_faustings_neutral_start:
    "Der Mann brummt als Einveständnis"
    fausings "Sagen Sie, ist Taxi fahren ein guter Job"
        menu:
            "Komisch. Ich hatte neulich einen Clown mitgenommen der mich das auch gefragt hat." if has_clowned:
            "Ich kann mich nicht beklagen"

label passenger_faustings_clown:
    faustings "Er war nicht zufällig ein Clown oder?"
    menu:
        "Ja war er!":
            faustings "Ah"
            faustings "Das war mein Bruder."
            jump passenger_faustings_brother
        "Sie kennen ihn?":
            "Er wirkt etwas angespannter als vorher."
            faustings "Ja, er ist mein Bruder."
            jump passenger_faustings_brother
        "Nein, er war kein Clown":
            faustings "Oh"
            "Er wirkt plötzlich etwas niedergeschlagen."
            faustings "Hätte ja sein können."
            menu:
                "Kennen Sie einen Clown?":
                    faustings "Ah nicht eirklich er ist nur ein Bekannter."
                    jump passenger_faustings_annoy_him
                    
                "Sie sind also der Geschäftsfüher vom Strpclub Soleil.":
                    jump passenger_faustings_boss
                

label passenger_faustings_annoy_him:
    menu:
        "Sind Sie sich sicher? Es hat sich so angehört als ob sie einen Clown kennen."
            faustings "Nein, nein, nicht wirklich, geht auch nur uns wirklich was an."
                menu:
                    "Ah, der Clown den Sie nicht kennen, der aber auch nur Sie etwas angeht, natrürlich.":
                        faustings "Suchst du nach Ärger?"
                            menu:
                                "Suchst du nach einem Clow-":
                                    "Die Verartzung deines Auges hat eine Weile gedauert. Du scheinst deinen nächsten Kunde dadurch verpasst zu haben."
                                    return
                                "Nein, nein, es tut mir Leid. Vergessen wir das.":
                                    # TODO
                                
                    "Ist auch nicht so wichtig.":
                        # TODO
        "Ist auch nicht so wichitg":
            #TODO
                
label passenger_faustings_brother:
    menu:
        "Wissen Sie, dass ihr Bruder depressiv ist?":
            faustings "Ha, es ist wohl kaum zu übersehen oder?"
            faustings "Es tut mir wirklich Leid um ihn und ich glaube ich bin etwas mit Schuld an seinem Zustand."
        "Sie lassen ihn in ihre Stripclubs?":
            faustings "Ich habe mehrere Geschäfte im Rotlichtviertel. Ich kann wohl kaum an jeder Ecke gleichzeitig stehen."
            
        "Haben Sie ein gutes Verhältnis zu ihrem Bruder?":
        "Das tut mir Leid":
            # TODO
        "Sie scheinen erfolgreicher zu sein als ihr Bruder":
        
label passenger_faustings_unfriendly:
    "Er wirkt belustigt."
    faustings "Leute meiner Sorte sorgen dafür, dass Leute ihrer Sorte im Geschäft bleiben."
    faustings "Denken Sie, Sie fahren die Leute nur zum Bäcker?"
    faustings "Vergraulen Sie sich nicht ihre gute Kundschaft mein Lieber."
    menu:
        "Nein mit Ausbeutern mache ich keine Geschäfte":
            faustings "Ausbeuter?"
            faustings "Wie viel von ihren Einnahmen gehen denn an ihre Arbeitnehmer?"
        "Na gut... Sie haben ja Recht.":
            "Er brummt."
            faustings "Na also"

label passenger_faustings_boss:
    faustings "Allerdings. Nicht nur den Stripclub, ich habe einige Unternehmen im Rotlichtbereich wissen Sie?"
    menu: 
        "Kann man in ihrem Geschäft einsteigen?":
            faustings "Sie brauchen Geld?"
        "Ich glaube ich könnte nicht im Rotlicht arbeiten":
            faustings "Natürlich, dazu fehlt ihnen der Bizeps oder die Brüste."
            "Er lacht herzlich"
            faustings ""
        "Interessant. Wie ist das Leben denn so als Pimp?"
        "Hm":
            faustings "Das stört sie oder?"
            menu:
                "Nein eigentlich nicht.":
                    fausings "Vielleich stört es mich auch nur selber."
                    menu:
                        ""
                "Mit dem Zuhälter Beruf assoziert man nicht grade ein positives Arbeitsumfeld."
                
label passenger_faustings_money:
    menu:
        "Ja, deshalb auch die Frage":
            fa
        "Nein, es geht mir um den _FAME_":
            "Er zieht die Augenbrauen zusammen."
            fausings "Den _FAME_?"
            menu:
                "Ich will etwas coolers sein als nur so ein blöder Taxifahrer.":
                    "Er schaut dich bemitleidend an."
                    faustings "Ich glaube ihr Beruf ist genau der richtige für Sie."
                    faustings "Glauben Sie mir die Zuhälterschaft bringt weniger Prestige mit sich als man glaubt."
                    faustings "Ah, da sind wir ja auch schon. Vielen Dank für die Fahrt."
                "Ich will das mich Leute respektiern wie Sie"
                ""
    
label passenger_faustings:
    $ has_clowned = game.get_passenger("clown").has_driven

    "Ein bulliger Mann mit Tattoos und einer Sonnenbrille steigt in deinen Wagen."
    faustings "Hallo. Bitte bringen Sie mich zu meinem Etablissment. Dem Stripclub Soleil."
    menu:
        "Alles klar":
            jump passenger_faustings_neutral_start
        "Sie sind der Geschäftsführer vom Soleil?":
            jump passenger_faustings_boss
        "Ich hatte neulich einen Gast den ich dort hinbringen sollte" if has_clowned:
            jump passenger_faustings_clown
        "Ich fahre keine Leute ihrer Sorte":
            jump passenger_faustings_unfriendly
    