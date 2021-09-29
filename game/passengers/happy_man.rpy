define passenger_happy_man = Character("Der glücklichste Mensch der je in dein Taxi gestiegen ist.")
$current_passenger_stats["paid"] = base_fare
label passenger_happy_man:
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
                            ""
                        "Wenn einem ein Passagier kein Trinkgeld gibt.":
                            "Na da brauchen Sie sich keine Sorgen machen!"
                            "Sie waren doch ein so anregender Gesprächspartner."
                            "Ich gebe gener etwas an andere ab wenn es sie glücklich macht!"
                            "Du kommst am Friedhof an"
                            passenger_happy_man "Vielen Dank für die Fahrt!"
                            $current_passenger_stats["paid"] = 2 * base_fare
                "Du hast recht. Immer eine positive Einstellung zu bewahren macht das Leben besser.":
                    passenger_happy_man "Sie sind ein Mann der es zu Leben versteht!"
        "Alles klar.":
            "Sie sind ein "
        "Ihr Arbeitsplatz?":
            "Das Lächeln des Mannes wird intensiver."
            "Nein ich besuche die Beerdigung meiner Frau!"
            jump passenger_happy_man_funeral
            
label passenger_happy_man_funeral:
    menu:
        "Denken Sie nicht, dass sie falsch angezogen sind für eine Beerdigung?":
            passenger_happy_man "Meine Frau hätte das nicht sonderlich interssiert."
            passenger_happy_man "Sie mochte mich als der, der ich bin."
        "Denken Sie nicht ihre Frau wäre traurig, dass Sie an ihrer Beerdigung so glücklich sind?":
            passenger_happy_man "Ich glaube nicht das meine Frau so selbst verliebt war, dass sie gewünscht hätte, dass ich an ihrer Beerdigung traurig sein muss."
     
    

