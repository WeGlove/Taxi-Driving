define passenger_failed_inventor = Character("Daniel Altmotor")
$current_passenger_stats["paid"] = base_fare
label passenger_failed_inventor:
    "Ein in einen verschlissenen Laborkittel gekleideter Mann steigt in dein Taxi."
    passenger_failed_inventor "Heureka! Zum Patentamt Kutscher!"
    menu:
        "Klar. Haben sie etwas bedeutendes entdeckt?":
            passenger_failed_inventor "Natürlich hab ich das. Es ist das Allfaktordiskriminierungsgerät."
            menu:
                "Was tut es?":
                    "Er mustert dich mit zusammengekniffenen Augen."
                    passenger_failed_inventor "Sie werden mir doch wohl nicht meine Patent stehlen wollen?"
                    menu:
                        "Ja, Hände hoch!":
                            you "Rück deinen Allquantordiskreditier-"
                            passenger_failed_inventor "-Allfaktordiskriminierungsgerät"
                            you "Genau, das Ding. Rück es raus!"
                            passenger_failed_inventor "Niemals! Nach 25 Jahren geb ich nicht meinen einzigen wissenschaftlichen Erfolg auf!"
                            "Er flüchtet aus deinem Wagen."
                            return
                        "Nein, ich bin an deinem Alllfak-dings-bums nicht interessiert."
                            passenger_failed_inventor "Das Allfaktordiskriminierungsgerät"
                            passenger_failed_inventor "Sie sind aber ganz schön neugiereig für jemanden der meine Patente nicht stehelen will."
                            "Für den Rest der Fahrt, weicht er der Konversation mit dir aus."
                            jump passenger_failed_inventor_flee
                        "*Nervöses Lachen*":
                            passenger_failed_inventor "Jetzt lachst du auch schon wie ein Dieb!"
                            "Er umklammert seine \"Erfindung\""
                            passenger_failed_inventor "Nicht mit mir hörst du! Nicht mit mir!"
                            "Bei laufender Fahrt reißt er die Tür deines Taxis auf und springt heraus."
                            return
                "Haben sie denn schon irgendwelche Patente?":
                    passenger_failed_inventor "Patente A, B, C und die 6!"
                    menu: 
                        "Sie haben noch nichts oder?"
        "Sie sehen so aus als ob sie bei der Wissenschaft auf der Durststrecke waren?":
            ""
label passenger_failed_inventor_flee:
    you "So hier wären wir."
    passenger_failed_inventor "Danke."
    "Er schaut dich noch einmal mistrauisch an und steigt aus."
    you "Hey, sie müssen noch bezahlen!"
    "Der Mann rennt so schnell er kann Richtung Patentamt."
    return