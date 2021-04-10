define baby = Character("Baby")

label baby:
    "Ein erwachsener Mann mit einer Windel und Rassel steigt in deinen Wagen."
    baby "Will Spielplatz."
    menu:
        "Nur Erwachsene dürfen fahren, raus hier!":
            "Der Mann beginnt infernalisch zu heulen und sich auf die Sitze zu werfen."
            menu:
                "Ok, ok, du kannst ja schon mit fahren, aber sei leise":
                    "Der Mann grinst zurfrieden."
                "Jetzt auch noch das, NEIN, RAUS HIER!!":
                    "Der Mann verstärkt sein Geheule und beginnt gegen deinen Sitz zu treten."
                    menu:
                        "Jetzt reichts mir aber...":
                            "Du steigst aus dem Wagen auf und öffnest die Tür zu dem Mann."
                            "Dein Sitzleder zerkratzend schleifst du ihn aus deinem Wagen"
                            you "Und komm ja nicht wieder!"
                            "Du fährst ohne ihn weiter, sein Gehuele hörst du aber noch am nächsten Block."
                            return
                        "Bei allem was heilig ist, hör bitte auf ich fahr dich ja schon":
                            "Der Mann grinst zurfrieden."
        "Ok, das Kind will zum Spielplatz, lass uns fahren.":
            "Der Mann grinst zufrieden."
    baby "Papa?"
    menu:
        "Nein, ich bin nicht dein Papa":
            baby "Wo, Papa? Warum Papa gegangen?"
            menu:
                "Wo hast du ihn denn das letzte mal gesehen?":
                    baby "10 Jahre. Papa holen Ziga-...Ziga-"
                    "Er bricht in Tränen aus"
                    baby "{i}Wo, Papa!?!{\i}"
                    menu: 
                        "Hey, hey, es wird alles gut, du bist doch schon groß und stark!":
                            "Er hört auf zu weinen und fragt schluchzent:"
                            baby "Wirklich?"
                            you "Ja schau dich doch an, du bist doch schon groß un kräftig und brauchst keinen mehr, der auf dich aufpasst."
                            "Ihr seid inzwischen am Spielplatz angekommen"
                            baby "Danke."
                            "Er gibt dir das Geld und zwei Schokotaler bevor er aussteigt."
                        "Ich weiß, ich weiß, ich kenn das Gefühl":
                            "Der Mann beginnt noch mehr zu weinen!"
                            baby "{i}Wo, unsere Papa!?!{\i}"
                            "Ihr seid inzwischen am Spielplatz angekommen"
                            "Noch immer schluchzend steigt der Mann aus dem Wagen aus."
                "Hier warum spielst du nicht mit meinem Jojo?":
                    baby "Yay!"
                    "Der Mann beginnt mit dem Jojo zu spielen. Er ist so vertieft darin das die Fahrt ohne weitere Umstände verläuft."
                    you "Da wären wir, der Spielplatz."
                    baby "Danke."
                    "Der Mann gibt dir zusätzlich zum Geld einen Schokotaler nimmt aber das Jojo mit."
        "Ja der bin ich. Ich bin dein Papa":
            baby "Papa!"
            "Er grinst dich an"
            baby "Will Lolli"
            menu:
                "Tut mir leid ich hab keinen Süßkram":
                    "Der Mann bricht in Geheul aus."
                    baby "Aber, ich will Lolli!"
                    "Für den Rest der fahrt belästigt dich der Mann und fordert seinen Lolli ein, den du ihm nicht geben kannst"
                    baby "Du, gar nicht Papa!"
                    "Sind seine letzen Worte bevor er wütend dein Auto verlässt."
                "Ok, ok lass uns kurz anhalten, ich kauf dir einen Lolli":
                    baby "Ja, Lollis!"
                    "Du gehst und kaufst ein paar Lollis für den Mann."
                    "Als du sie ihm gibst scheint er überglücklich zu sein und ist für den Rest der Fahrt zu frieden."
                    "Als er austeigt gibt er dir dein Geld und einen Schokotaler."
    return

