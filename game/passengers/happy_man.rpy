define passenger_happy_man = Character("Der glücklichste Mensch der je in dein Taxi gestiegen ist.")

label passenger_happy_man:
    $current_passenger.status["cloths"] = False
    $current_passenger.paying = game.base_fare
    "Ein vor Freude strahlender Mann steigt in dein Taxi."
    "Er trägt ein T-Shirt auf dem ein Smiley abgedruckt ist."
    passenger_happy_man "Zum Friedhof bitte, guter Mann."
    menu:
        "Sie sehen sehr glücklich aus für jemanden der zum Friedhof will.":
            passenger_happy_man "Natürlich. Ich versuche immer fröhlich zu sein."
            passenger_happy_man "Es hilft einem durch's Leben weißt du?"
            menu: 
                "Ist ihnen denn was passiert?":
                    "Das Lächeln des Mannes wird intensiver."
                    passenger_happy_man "Ja, meine Frau ist gestorben!"
                    menu:
                        "Es tut mir Leid das ihnen das passiert ist. Mein Beileid.":
                            passenger_happy_man "Ach i wo! Ich lasse mir meine gute Laune nicht verderben."
                            jump passenger_happy_man_funeral
                        "Stimmt Sie das nicht traurig?":
                            passenger_happy_man "Ach i wo! Ich lasse mir meine gute Laune nicht verderben."
                            jump passenger_happy_man_funeral
                        "Deswegen wollen sie zum Friedhof?":
                            passenger_happy_man "Ja. Die Beerdiung fängt bald an."
                            jump passenger_happy_man_funeral
                        "... Welche Raiosender hören Sie so?":
                            passenger_happy_man "Ich höre gerne den Kinderserien im staatlich freigegebenem Rundfunk zu."
                            passenger_happy_man "Am Ende sind alle Charatere immer so glücklich."
                            
                "Ich kann mir schon vorstellen, das es Gelegenheiten gibt bei denen man traurig sein möchte.":
                    passenger_happy_man "Findest du? Welche denn zum Beispiel?"
                    menu:
                        "Bei einer Beerdigung":
                            "Ha, sie verstehen es zu spaßen, der hätte meiner verstorbenen Frau sicher auch gefallen!"
                            jump passenger_happy_man_funeral
                        "Wenn einem ein Passagier kein Trinkgeld gibt.":
                            "Na da brauchen Sie sich keine Sorgen machen!"
                            "Sie waren doch ein so anregender Gesprächspartner."
                            "Ich gebe gener etwas an andere ab wenn es sie glücklich macht!"
                            "Du kommst am Friedhof an."
                            passenger_happy_man "Vielen Dank für die Fahrt!"
                            "Er steigt aus deinem Taxi aus"
                            $current_passenger.paying = 2 * game.base_fare
                            return
                "Du hast recht. Immer eine positive Einstellung zu bewahren macht das Leben besser.":
                    passenger_happy_man "Ah du siehst es auch so wie ich, nicht wahr? Ein Lächeln macht jede Situation besser."
                    passenger_happy_man "Gut das sie auf der glücklichen Seite des Lebens stehen."
                    "Du hälst am Friedhof."
                    passenger_happy_man "Vielen Dank für die Fahrt!"
                    "Er verlässt den Wagen."
                    return
        "Alles klar.":
            jump passenger_happy_man_funeral
        "Ihr Arbeitsplatz?":
            "Das Lächeln des Mannes wird intensiver."
            "Nein ich besuche die Beerdigung meiner Frau!"
            jump passenger_happy_man_funeral
            

label passenger_happy_man_funeral:
    menu:
        "Denken Sie nicht, dass sie falsch angezogen sind für eine Beerdigung?" if not current_passenger_stats["status"]["cloths"]:
            passenger_happy_man "Meine Frau hätte das nicht sonderlich interssiert."
            passenger_happy_man "Sie mochte mich als der, der ich bin."
            $current_passenger.status["cloths"] = True
            jump passenger_happy_man_funeral
        "Denken Sie nicht ihre Frau wäre traurig, dass Sie an ihrer Beerdigung so glücklich sind?":
            passenger_happy_man "Ich glaube nicht das meine Frau so selbst verliebt war, dass sie gewünscht hätte, dass ich an ihrer Beerdigung traurig sein muss."
            menu:
                "Aber hat sie ihnen denn nichts bedeutet?":
                    passenger_happy_man "Natürlich hat sie das. Ich bin doch bei ihrer Beerdigung oder?"
                    menu:
                        "Aber sind sie traurig?":
                            passenger_happy_man "Nein, warum sollte ich es auch sein?"
                            menu:
                                "Können sie wirklich sagen das sie sie vermissen wenn sie nicht traurig sind, weil sie Tod ist?":
                                    passenger_happy_man "..."
                                    "Er wirkt etwas kühler."
                                    passenger_happy_man "Halten sie bitte an."
                                    "Du hälst am Straßenrand."
                                    "Er verlässt den Wagen."
                                    you "Hey, sie müssen noch bezahlen."
                                    passenger_happy_man "Es macht mich glücklich nicht zu zahlen."
                                    "Er geht."
                                    $current_passenger.paying = 0
                        "Das ist ein Argument...":
                            passenger_happy_man "Siehst du du siehst es doch auch wie ich."
                            "Nach einer Weile kommt ihr am Friedhof an."
                            passenger_happy_man "Danke für Die Fahrt."
                            "Er steigt aus."
                            return
                "Sie sind schrecklich":
                    passenger_happy_man "Ich? aber warum denn? Ich will doch nur das jeder glücklich ist!"
                    menu:
                        "Aber nicht jeder will glücklich sein!":
                            passenger_happy_man "... Was meinen sie damit?"
                            you "Jedem ständig aufzwingen zu wollen glücklich zu sein ist doch respektlos gegenüber den Leuten."
                            you "Sie können ihre eigene Entscheidungen treffen."
                            passenger_happy_man "Ich glaube ich verstehe was du meinst."
                            "Du kommst am Friedhof an."
                            passenger_happy_man "Vielen Dank für das interssante Gespräch während der Fahrt."
                            passenger_happy_man "Hier ist ihr Geld."
                            "Er gibt dir die Hälfte des Fahrpreises."
                            you "Hey das ist nicht genug!"
                            passenger_happy_man "Ich weiß."
                            "Er lächelt breiter und verlässt den Wagen"
                            $current_passenger.paying = game.base_fare / 2
                            return
                        "Es gibt aber Situationen in denen es einem besser geht wenn man traurig ist!":
                            passenger_happy_man "Wie meinst du das?"
                            you "Wenn sie nicht traurig sind dann muss das ja bedeutet haben das ihnen nicht viel an der Person gelegen hat."
                            you "Wie können Sie sich sicher sein Sie geliebt zu haben wenn ihr Tod keinen negativen Einfluss auf sie hat."
                            passenger_happy_man "..."
                            "Er wirkt etwas kühler."
                            passenger_happy_man "Halten sie bitte an."
                            "Du hälst am Straßenrand."
                            "Er verlässt den Wagen."
                            you "Hey, sie müssen noch bezahlen."
                            passenger_happy_man "Es macht mich glücklich nicht zu zahlen."
                            "Er geht."
                            $current_passenger.paying = 0
                            return
                "Wenn sie meinen.":
                    passenger_happy_man "Das tue ich."
                    "Nach einer Weile kommt ihr am Friedhof an."
                    passenger_happy_man "Danke für Die Fahrt."
                    "Er steigt aus."
                    return
                "Sie haben recht.":
                    passenger_happy_man "Ah du siehst es auch so wie ich, nicht wahr? Ein Lächeln macht jede Situation besser."
                    passenger_happy_man "Gut das sie auf der glücklichen Seite des Lebens stehen."
                    "Du hälst am Friedhof."
                    passenger_happy_man "Vielen Dank für die Fahrt!"
                    "Er verlässt den Wagen."
                    return
