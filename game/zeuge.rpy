define zeuge = Character("Chantelle")

label zeuge:
    "Eine junge Frau steigt in dein Taxi. Sie streicht sich die Haare aus dem Gesicht und möchte zum örtlichen Tempel gebracht werden"
    zeuge "Ein wunderschöner Tag zum Beten finden Sie nicht?"
    menu:
         "Ich bin nicht religiös. Der Tag ist aber trotzdem schön.":
            zeuge "Aber jeder Tag wird doch durch Religion schöner!"
         "Ja, preiset den mächtigen Erlöser! Er und seine Erdbeeren werden uns befreien!":
            "Sie rümpft die Nase, fasst sich dann aber schnell wieder."zeuge "Erdbeerianismus ist von gestern."
         "Bleib mir bloß mit Religion weg":
            zeuge "Gerade Leute wie Sie könnten Religion gut gebrauchen!"
    zeuge "Möchten Sie nicht von meiner Religion hören?"
    menu:
         "Nein, danke!":
            "Sie ignoriert dich und fährt unbeirrt fort." 
            $not_strawberry = True
         "Ja warum nicht!":
            "Ihre Augen leuchten auf und sie beginnt begeistert zu reden"
            $not_strawberry = True
         "Beleidige nicht mich und mein unbändiges Vertrauen in die Erdbeeren, Versucherin!":
            "Sie spuckt auf der Stelle aus." 
            $not_strawberry = False
    if not_strawberry:
        "Also, ich bin von den Whiskasianeren und wir glauben, dass die Katzen uns irgendwann erretten werden!"
        menu:
             "Ist das nicht so ein komischer Furry-Sex-Kult?":
                "Nein, das ist nur Nebensache. Der Sex ist trotzdem gut!" 
                menu:
                     "Na gut ich komme mit, wo kann ich mich anmelden?":
                        zeuge "Kommen Sie doch mit in den Tempel, ich zeige Ihnen da {i}ALLES{/i}"
                     "Nein, danke kein Interesse":
                        "Sie schaut enttäuscht und sagt den Rest der Fahrt beleidigt kein Wort mehr"

             "Das klingt interessant. Ich mag Katzen, wo kann ich mich anmelden?":
                "Ihre Augen leuchten und lächelnd antwortet sie:" zeuge "Kommen Sie doch mit in den Tempel"
             "Bloß nicht! Da geh ich ja lieber zum Kult der Großen AI!":
                "Sie schaut enttäuscht und sagt den Rest der Fahrt beleidigt kein Wort mehr"



    

