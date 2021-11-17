define zeuge = Character("Chantelle")

label zeuge:
    $current_passenger.paying = game.base_fare
    $current_passenger.status["conversion"] = False
    "Eine junge Frau steigt in dein Taxi. Sie streicht sich die Haare aus dem Gesicht und möchte zum örtlichen Tempel gebracht werden"
    zeuge "Ein wunderschöner Tag zum Beten finden Sie nicht?"
    menu:
         "Ich bin nicht religiös. Der Tag ist aber trotzdem schön.":
            zeuge "Aber jeder Tag wird doch durch Religion schöner!"
         "Ja, preiset den mächtigen Erlöser! Er und seine Erdbeeren werden uns befreien!":
            "Sie rümpft die Nase, fasst sich dann aber schnell wieder."
            zeuge "Erdbeerianismus ist von gestern."
         "Bleib mir bloß mit Religion weg":
            zeuge "Gerade Leute wie Sie könnten Religion gut gebrauchen!"
            $current_passenger_stats.paying -= 0.1 * game.base_fare
    zeuge "Möchten Sie nicht von meiner Religion hören?"
    menu:
         "Nein, danke!":
            "Sie ignoriert dich und fährt unbeirrt fort." 
            $not_strawberry = True
         "Ja warum nicht!":
            "Ihre Augen leuchten auf und sie beginnt begeistert zu reden"
            $not_strawberry = True
            $current_passenger.paying += 0.25 * game.base_fare
         "Beleidige nicht mich und mein unbändiges Vertrauen in die Erdbeeren, Versucherin!":
            "Sie spuckt auf der Stelle aus." 
            $current_passenger.paying += -0.75 * game.base_fare
            $not_strawberry = False
    if not_strawberry:
        "Also, ich bin von den Whiskasianeren und wir glauben, dass die Katzen uns irgendwann erretten werden!"
        menu:
             "Ist das nicht so ein komischer Furry-Sex-Kult?":
                "Nein, das ist nur Nebensache. Der Sex ist trotzdem gut!" 
                menu:
                     "Na gut ich komme mit, wo kann ich mich anmelden?":
                        zeuge "Kommen Sie doch mit in den Tempel, ich zeige Ihnen da {i}ALLES{/i}"
                        $current_passenger.paying += game.base_fare
                        $current_passenger.status["conversion"] = True
                     "Nein, danke kein Interesse":
                        "Sie schaut enttäuscht und sagt den Rest der Fahrt beleidigt kein Wort mehr"

             "Das klingt interessant. Ich mag Katzen, wo kann ich mich anmelden?":
                "Ihre Augen leuchten und lächelnd antwortet sie:" 
                zeuge "Kommen Sie doch mit in den Tempel"
                $current_passenger.paying +=  game.base_fare
                $current_passenger.status["conversion"] = True
             "Bloß nicht! Da geh ich ja lieber zum Kult der Großen AI!":
                "Sie schaut enttäuscht und sagt den Rest der Fahrt beleidigt kein Wort mehr"
    else:
        zeuge "Ich eine Versucherin? Du solltest dich mal ansehen mit deinen Erdbeeren!"
        menu:
            "Der Erdbeerianismus ist deinem Was-auch-immer völlig überlegen!":
                zeuge"Jeder vom Erdbeerianismus hat doch nur noch Früchte im Hirn. Du könntest mich nicht mal versuchen, wenn ich es wollte!"
                menu:
                    "Sie küssen":
                        "Nachdem du dich einige Zeit später von ihrem Schlag erholt hast, fragst du dich, warum du dachtest, dass das eine gute Idee wäre."
                    "Anhalten und sie rauswerfen":
                        zeuge "Klar ich wollte eh nicht in deinem dreckigen Erdbeertaxi fahren!"
                        $current_passenger_stats.paying = 0
                    "Stoisch nach vorne auf die Straße schauen und sie ab jetzt ignorieren":
                        "Sie versucht dich weiter anzustacheln, gibt aber nach einer Weile schmollend Ruhe"
            "Wie bitte? Bin ich etwa in dein Taxi eingestiegen und habe angefangen von Religion zu faseln?":
                "Sie versucht etwas zu erwiedern, stoppt dann aber. Sie schmollt für den Rest der Fahrt auf der Rückbank"
    
            



    

