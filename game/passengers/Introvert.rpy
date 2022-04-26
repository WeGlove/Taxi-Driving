define introvert = Character("Ein wichtig aussehender Mann")

label introvert:
    "Ein Mann in einem sehr gepflegten Nadelstreifenanzug steigt in dein Taxi."
    introvert "Zum Rathaus bitte, und beeilen Sie sich bitte, wenn Sie nichts dagegen haben."
    "Du nickst bestätigend und versuchst ein Gespräch zu initiieren"
    introvert "Bitte, versuchen Sie, wenn möglich, nicht mit mir zu reden, ich mag das nicht."
    if game.upgrades["Zeitungen"]:
        "Der Mann nimmt eine Zeitung auf und liest sie."
        $current_passenger.paying += 0.25 * game.base_fare
    else:
        "Der Mann nimmt ein Buch aus einer Tasche und beginnt zu lesen"
    if game.get_passenger("mime").has_driven:
        if game.get_passenger("mime").Status["Nice_Mime"]:
            "Die Mime, mit der du kurzem gefahren bist erkennt dein Taxi und beginnt an einer roten Ampel eine kleine Aufführung zu deiner Belustigung"
            menu:
                "Den Passagier darauf aufmerksam machen":
                    "Der Mann atmet genervt aus und widmet sich schnell wieder dem,  was er vorher gemacht hat."
                    $current_passenger.paying -= 0.25 * game.base_fare
                "Nichts sagen":
                    $current_passenger.paying += 0.25 * game.base_fare
    "Ein Auto kommt aus einer Seitenstraße geschossen, aller Voraussicht nach, musst du eine Vollbremsung machen."
    menu:
            "Vorsicht!":
                "Der Mann schaut auf, sieht sich verwirrt um bemerkt das Auto nicht sofort und knallt mit dem Kopf auf das Amaturenbrett."
                introvert "Das hätten Sie mir aber schon früher sagen können"
                $current_passenger.paying -= 0.25 * game.base_fare
                menu:
                    "Die Antwort, die dir auf der Zunge liegt, schlucken":
                        "Der Passagier widmet sich wieder dem, was er vorher getan hat"
                    "Aber Sie haben doch gesagt ich soll nicht mit Ihnen reden!":
                        introvert   "Das gilt doch offensichtlich nicht für Notfälle und jetzt hören Sie bitte auf mit mir zu diskutieren."
                        introvert   "Davon bekomme ich Kopfschmerzen!"
                        $current_passenger.paying -= 0.25 * game.base_fare
                        menu:
                            "Aufhören zu diskutieren":
                                "Der Passagier widmet sich wieder dem, was er vorher getan hat"
                            "Ich habe Ihnen rechtzeitig bescheid gesagt, so lasse ich nicht mit mir reden!":
                                introvert "Das sehe ich anders, diese Unverschämtheit ziehe ich von Ihrer Rechnung ab!"
                                $current_passenger.paying -= 2* game.base_fare
            "Nichts sagen":
                "Der Mann knallt mit dem Kopf auf das Amaturenbrett und hinterlässt einen kleinen Blutfleck"
                introvert "Hmm, da hätte ich besser aufpassen sollen. Tut mir leid Ihnen Umstände zu machen"
                $current_passenger.paying += 0.25 * game.base_fare
    "Eine Frau hängt ein Banner mit einem Bild von ihr und unzweifelhaft deinem beschäftigten Mitfahrer auf eine Brücke"
    "Darauf steht: Mannfred, willst du mich heiraten?"
    menu:
            "Ihn darauf aufmerksam machen": 
                introvert "Halten Sie an!"
                menu:
                    "Anhalten":
                        "Er steigt aus dem Auto."
                        if game.upgrades["Zeitungen"]:
                            $text_price = game.newspaper_monies
                            "Er lässt dir gerade mal {textprice} CRP"
                            $current_passenger.paying = game.newspaper_monies
                            return
                        else:
                            "Er verlässt eilig den Wagen und vergisst dabei zu zahlen."
                            $current_passenger.paying = 0
                            return

                    "Nicht Anhalten":
                            "Er läuft rot an."
                            introvert "WAS DENKEN SIE SICH DENN! HALTEN SIE AN, MANN! SONST SEHEN SIE KEINEN CRP VON MIR!"  
                            "Widerstrebend fährst du rechts ran."
                            introvert "Und das ist eigentlich noch zu viel!"
                            $current_passenger.paying = 0.25 * game.base_fare
                            return
                    "Ihn erst um die Fahrtkosten bitten":
                        introvert "Denken Sie ich würder die Zeche prellen? Für diese Unverschämtheit gibt es kein Trinkgeld!"
                        if current_passenger.paying > game.base_fare:
                            $current_passenger.paying = game.base_fare
                        "Er steigt aus dem Taxi"
                        return
            "Ihn nicht darauf aufmerksam machen":
                "Dein Passagier sieht nicht von seiner Tätigkeit hoch und verpasst den Heiratsantrag."
    "Ihr kommt an eurem Zielort an."
    menu:
            "Ihn darauf aufmerksam machen":
                introvert "Vielen Dank."
                return
            "Ihn nicht darauf aufmerksam machen":
                "Es vergeht einige Zeit, bis er bemerkt, dass ihr angekommen seid, sodass du deinen nächsten Kunden verpasst"
                $game.skip_a_character()
                introvert "Oh, ich hab gar nicht bemerkt, dass wir schon da sind! Das tut mir leid. Hier, fürs warten"
                $current.passenger.paying += 5 * base_fare



