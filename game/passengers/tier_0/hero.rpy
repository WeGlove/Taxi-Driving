define hero = Character("Actionman")


label hero:
    $attitude = 0
    "Ein Mann, der eine Unterhose über einem eng anliegenden Sportanzug trägt und sich ein Handtuch, das schlecht mit einem \"A\" bemalt wurde, umgebunden hat steigt in dein Taxi"
    hero "{i} DAS ACTIONSIGNAL WURDE GESENDET! ACTIONMAN MUSS SOFORT ZUM JUWELIER GLITZERKRÄHE!{/i}"
    menu:
        "Was für ein Signal? Und warum haben sie die Unterhose über der Hose an? Können Sie mich überhaupt bezahlen?":
            "Die Bezahlung ist dein Wissen etwas für die {i} Gerechtigkeit {/i} getan zu haben! Wer kann schon von sich sagen Actionman zum Tatort gefahren zu haben?"
            menu:
                "Immerhin eine gute Geschichte!":
                    "Du fährst los"
                    menu:
                        "Was ist denn das Verbrechen Actionman?":
                            hero "Das Actionsignal hat nur zum Juwelier gedeutet. Aber da es ein Juwelier ist wahrscheinlich ein Action-Raubüberfall!"
                        "Wie wirst du die Verbrecher dieses mal stellen Actionman?":
                            hero "Mit dem Action-Faustschlag natürlich! Die werden sich wundern!"
                            menu: 
                                "Oh ist der Action Faustschlag stärker als gewöhnliche Faustschläge?":
                                    hero "Nein aber ich schreie ganz laut \"Action\" dabei."
                                    you "Oh"
                                "Der Actionfaustschlag wird sie bestimmt vertreiben. Aber was wenn das nicht reicht?":
                                    "Er zeigt dir eine Pistole die er in seinem Gürtel versteckt hat"
                                    hero "Dann verwende ich die Action-Super-Gerechtigkeits-Freundschafts-Hyper-Pistole"
                                    menu:
                                        "Nicken und fahren":
                                            "Der Rest der Fahrt vergeht wie im Flug. Den jemand entführt hat."
                                        "Das wird sie ganz sicher umhauen Actionman":
                                            " Du lachst nervös "
                                            $attitude += 1
                                            hero "Die hat sie bis jetzt noch immer in die Flucht geschlagen. Ich freue mich, dass du das so verstehst!"


                            
                        "Sind die nicht über alle Berge bis wir da sind?":
                            hero "Ich bin mir sicher das Verbrechen flüchtet vor Actionman. Aber Actionman wird sie Action-verfolgen."


                "Gerechtigkeit bringt kein Brot auf den Tisch. Raus hier.":
                    "Er verlässt das Taxi und schreit"
                    hero "Action-Ausdauerlauf"
                    "Er beginnt in gewöhnlichem Tempo zu joggen"
                    $current_passenger.paying = 0 * game.base_fare
                    return
        "Ist da so eine Art Kostümfestival oder so? Ich habe selbst ein Kostüm und wollte bei sowas immer Mal mitmachen":
            hero "Oh ein rivalisierender Held! Nein, das hier ist Actionmans Fall! Halt du dich da raus!"
            menu:
                    "Aber ich bin gar kein Held nur ein Taxifahrer, der auch ein Kostüm besitzt.":
                        hero "Deine geheime Identität ist bei Actionman sicher. Darauf kannst du dich verlassen."
                        menu:
                            "Es ist keine geheime Identität. Ich verkleide mich nur gerne!":
                                hero "Ja sicher."
                                "Er zwinkert dir vielsagend zu"
                            "Ähm. Danke.":
                                hero "Auf {i}Actionman{/i} ist verlass!"

                    "Ah! Man darf natürlich nicht aus der Rolle fallen! Na dann Actionman lass uns das Verbrechen bekämpfen":
                        hero "Du bringst mich nur hin. Wie gesagt dieser Fall gehört {i}Actionman{/i}"
    "Nach einer Weile kommt ihr vor dem erstaunlich ruhigen Juwelierladen an."
    if not attitude == 1:
        hero"Actionman wird nachsehen gehen, fahr unbescholtener Mitbürger"
        "Er lässt dich ohne zu bezahlen zurück. Nach einer kurzen Weile hörst du Sirenen. Du beschließt dich jetzt besser auf den Weg zu machen."
        $current_passenger.paying = 0 * game.base_fare
        return
    else:
        hero "Du hast Actionman wirklich beeindruckt. Ein Superheld verdient nicht viel aber wenigstens kann ich dir das hier geben"
        "Er reicht dir eine Taschenlampe, über die eine Folie mit einem A gelegt wurde"
        hero "Falls du den Actionman je wieder brauchen solltest "
        $current_passenger.paying = 0 * game.base_fare
        "Nach einer kurzen Weile hörst du Sirenen. Du beschließt dich jetzt besser auf den Weg zu machen."
        return
            

    
