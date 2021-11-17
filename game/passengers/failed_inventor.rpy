define passenger_failed_inventor = Character("Daniel Altmotor")

label passenger_failed_inventor:
    $current_passenger.paying = 0
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
                        "Nein, ich bin an deinem Alllfak-dings-bums nicht interessiert.":
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
                        "Sie haben noch nichts oder?":
                            passenger_failed_inventor "Ja, ja... Wissen Sie es war nicht immer einfach. Ich habe in der Vergangenheit viele Fehler gemacht?"
                            menu:
                                "Tut mir leid das zu hören...":
                                    passenger_failed_inventor "Danke, ihr Mitgefühl wird mich sicher weiter bringen."
                                    "Er wirkt niedergeschlagen und seuftzt."
                                    passenger_failed_inventor "Naja, tut mir auch Leid. Ich habe auch eigentlich gar kein Geld um sie zu bezahlen..."
                                    menu:
                                        "Was!? Raus aus meinem Wagen!":
                                            passenger_failed_inventor "Ja, ok ok ich versteh schon. Keiner hat Zeit für den Daniel."
                                            "Du hältst und er verlässt den Wagen."
                                            return
                                        "Das ist schon in Ordnung. Wir gehen ja alle mal ne schwierige Zeit.":
                                            jump passenger_failed_inventor_success
                                "Was haben Sie denn für Fehler gemacht?":
                                    passenger_failed_inventor "Ich habe in meinem letzten Experiment den großen Zeh meines Teilnehmers mit einer Schnecke gekreutzt."
                                    passenger_failed_inventor "Vielleicht hätte mein erster Teilnehmer auch nicht gleich mein Arbetigeber sein sollen."
                                    passenger_failed_inventor "Davor stand ich schon auf der Kippe. Ich hatte eine Reihe von Versuchen mit Wespen unr Ratten durchgeführt."
                                    passenger_failed_inventor "Bevor wir die Stöcke von denen wieder aus der Kanalisation bekommen haben hat es Monate gedauert."
                                    passenger_failed_inventor "Dann hab ich noch ausversehen Cthulhu beschworen."
                                    passenger_failed_inventor "Zum Glück hat das noch keiner gemerkt."
                                    passenger_failed_inventor "Ähh. Bitte behalten sie das für sich."
                                    passenger_failed_inventor "Jetzt wo ich drücber nachdenke..."
                                    "Er reißt bei laufender Fahrt die Tür auf, springt heraus, tut sich leicht am Fuß weh, hustet, setzt seine Brille ab und rennt davon zum Patentamt."
                                    return
                                "Na dann wird ihr Allkraftdiskogerät ja bestimmt ihr großer Erfolg!":
                                    passenger_failed_inventor "Das Allfaktordiskriminahrungs- ähh, ich meine natürlich -diskriminierungsgerät."
                                    passenger_failed_inventor "Ja das hoff ich auch. Viele Optionen mehr bleiben mir auch nicht."
                                    jump passenger_failed_inventor_success
                        "Ich bin beeindruckt!":
                            passenger_failed_inventor "Ich bin auch von mir beeindruckt!"
                            you "Na dann wünsche ich ihnen noch viel Erfolg!"
                            jump passenger_failed_inventor_success
                        "Was ist denn Patent A?":
                            passenger_failed_inventor "Ja das Patent A patentiert meine letzte große Erfindung!"
                            you "Und was war die?"
                            passenger_failed_inventor "Ja meine letzte große Erfindung. Im Bereich... Wissen sie was ich muss mich vor ihnen nicht rechtfertigen. Fahren sie einfach ihr Taxi."
                            jump passenger_failed_inventor_flee
        "Sie sehen so aus als ob sie bei der Wissenschaft auf der Durststrecke waren?":
            passenger_failed_inventor "Was ich trinke doch täglich!"
            "Er nimmt seinen Flachmann aus der Tasche und nimmt einen tüchtigen Schluck."
            menu:
                "hey, hey, kein Alkohl in meinem Wagen":
                    passenger_failed_inventor "Ach sei mal keine Schnegge Takschi Fahrer."
                    passenger_failed_inventor "Isch will doch nur kurtsch zschum Patentamt."
                    "Offenbar enthielt sein Flachmann pures Ethanol."
                    jump passenger_failed_inventor_alcohol
                "Sagen sie können sie eigentlich bezahlen?":
                    "Ähm, ja natürlich. Für wen halten Sie mich denn?"
                    menu:
                        "Für jemanden der nicht bezahlen kann.":
                            passenger_failed_inventor "So was muss sich ein Mann meines geistischen Standes nicht gefallen laschen. Halten sie den Wagen an. Ich gehe!"
                            "Du hältst an und er verlässt den Wagen."
                            return
                        "Für einen Irren":
                            passenger_failed_inventor "So was muss sich ein Mann meines geistischen Standes nicht gefallen laschen. Halten sie den Wagen an. Ich gehe!"
                            "Du hältst an und er verlässt den Wagen."
                            return
                        "Entschuldigung":
                            passenger_failed_inventor "Rescht so."
                            "Nach einer Weile kommt ihr an und er verlässt den Wagen."
                            you "Hey sie müssen noch bezahlen!"
                            passenger_failed_inventor "Ach ja mein Beschter. Hier is dei Tringgeld."
                            $current_passenger.paying += game.base_fare / 1000
                            "Er gibt dir eine Münze aus seiner Jackentasche und zieht von Dannen."
                            return
                "Prost!":
                    passenger_failed_inventor "So lob isch mir das. Bischt ein gudder Takschifahrer."
                    "Offenbar enthielt sein Flachmann pures Ethanol."
                    jump passenger_failed_inventor_alcohol
                    

label passenger_failed_inventor_flee:
    you "So hier wären wir."
    passenger_failed_inventor "Danke."
    "Er schaut dich noch einmal mistrauisch an und steigt aus."
    you "Hey, sie müssen noch bezahlen!"
    "Der Mann rennt so schnell er kann Richtung Patentamt."
    return
    
label passenger_failed_inventor_success:
    "Er schweigt für einen Moment."
    passenger_failed_inventor "Wissen Sie, sie waren sehr nett zu mir. Warum nehmen sie nicht den Prototypen von meinem Allfaktordiskriminierungsgerät?"
    passenger_failed_inventor "Das wäre zumindest etwas Bezahlung"
    menu:
        "Nein Danke. Ich kann solchen Plunder nicht in meinem Taxi brauchen":
            "Er wirkt verletzt"
            passenger_failed_inventor "Na gut. Dann geh ich Mal zum Patentamt. Tschüss, schätz ich Mal."
            "Du hältst und er verlässt den Wagen."
            return
        "Ja wenn sie sich da sicher sind.":
            passenger_failed_inventor "Gerne doch!"
            "Du hältst und er verlässt den Wagen. Er hinterlässt dir sein Allfaktordiskriminierungsgerät."
            return
        "Das kann ich nicht annehmen. Bezahlen sie doch einfach beim nächsten Mal!":
            passenger_failed_inventor "Ah daran können sie glauben. Mit dem Patent für dieses Gerär werde ich Sie dreifach zurückbezahlen können!"
            you "Ich werde drauf warten!"
            passenger_failed_inventor "Vielen Dank für die Güte."
            "Du hältst und er verlässt den Wagen."
            return 

label passenger_failed_inventor_alcohol:
    menu:
        "Jetzt reicht's mir aber. Raus!":
            "Du schmeißt den Gast aus dem Taxi."
            passenger_failed_inventor "Warte. Mein Allfagtorrkreditgerät..."
            "Du schmeißt es ihm hinterher."
            return
        "Ok, ich fahr Sie noch bis dahin, ist ja gleich um die Ecke.":
            passenger_failed_inventor "Dange Schatz. Bischt'n gudder Takschifahrer."
            "Nach einer Weile kommt ihr an und er verlässt den Wagen."
            you "Hey sie müssen noch bezahlen!"
            passenger_failed_inventor "Ach ja mein Beschter. Hier is dei Tringgeld."
            $current_passenger.paying += game.base_fare / 1000
            "Er gibt dir eine Münze aus seiner Jackentasche und zieht von Dannen."
            return