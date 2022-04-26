


define Unicorn = Character("Einhorn")

label Unicorn:
    #Einhorn Symbol für Sucht <-- wird immer mehr demonic bei Ablehnung von Dings
    # Am Ende  Einhorn verschwundne. Du findest dich alleine in deinem Taxi wieder. Du hast Lust auf Drogen.
    "Ein Einhorn mit Sonnenbrille steigt in deinen Wagen."
    Unicorn "Yo."
    menu:
        "Alter, ich muss mit diesen Drogen aufhören.":
            Unicorn "Wäre vielleicht besser. Aber bis dahin..."
            Unicorn "Bock einen durchzuziehen?"
            menu:
                "Immerdoch":
                    "Glücklich nimmst du die Tüte des Einhorns entgegen und ziehst genüsslich einmal daran."
                    "Dir entgeht die Ironie an der Situation irgendwie"
                    Unicorn "So ist's richtig!"
                "Ich weiß nicht...":
                    "Das Einhorn zuckt mit den Ohren"
                    Unicorn "Sicher? Noch eine letzte Tüte... Was soll sie denn noch schaden? Wäre doch uncool, mich hier alleine rauchen zu lassen."
                    "Dir kommt es vor als seien die Zähne des Einhorns etwas spitzer geworden"
                    menu:
                        "Ja wäre schon ziemlich uncool":
                            "Du nimmst einen Zug von der Tüte"
                            "Das Einhorn lächelt dich an"
                            jmp smoked_one
                            
                        "Ich weiß wirklich nicht":
                            Unicorn "Ach komm schon nur eine"
                            "Es zieht die Sonnenbrille etwas runter und hält dir den Joint unter die Nase, sodass dir der Geruch in die Nase steigt."
                            "Du fragst dich ob alle Pferde senkrechte Schlitze als Pupillen haben oder nur dieses."
                            menu:
                                "Ach, was soll's?":
                                    "Du nimmst einen Zug vom Joint"
                                    jmp smoked_one
                                "Nein, ich glaube das sollte ich nicht":
                                    
                                    Unicorn "Du hälst dich wohl für was besseres, was?"
                                    "Seit wann hat dieses Untier eigentlich ledrige Flügel am Rücken?"
                                    Unicorn "Hör zu, du nimmst diesen Joint jetzt in den Mund und ziehst daran sonst werde ich richtig ungemütlich!"
                                    menu:
                                        "Na gut":
                                            jmp smoked_one
                                        "Nein.":
                                            "Es bläst heißen Dampf aus seinen Nüstern und auf seinem Kopf bemerkst du ein zweites Horn. Waren die eigentlich die ganze Zeit schon so gekrümmt?"
                                            Unicorn "Du"
                                            Unicorn "nimmst"
                                            Unicorn "jetzt"
                                            Unicorn "den"
                                            Unicorn "Joint"
                                            menu:
                                                "Ähm, ich glaube ich hab grade richtig Lust auf Drogen":
                                                    Unicorn "Schon besser"
                                                    "Es nimmt wieder seine alte deinen Nerven besser bekommende Gestalt an"
                                                    jmp smoked_one
                                                "Nein":
                                                    "Dein Gegenüber hat mittlerweile sein ganzes Fell verloren. Darunter ist feuerrote Haut zum Vorscheingekommen."
                                                    "Es scheint mehr Raum einzunehmen als eigentlich in deinem Taxi sein sollte."
                                                    Unicorn "Verflucht seist du, Mensch, der es wagt sich mir zu widersetzen. Brennen sollst du, aber auch auf Erden sollst du leiden!"
                                                    Unicorn "Du sollst die Stoffe begehren, die du heute verweigert hast und dennoch bei dem Versuch sie zu erhalten verzagen!"
                                                    Unicorn "So lautet mein Spruch!"
                                                    "Dann verschwindet es."
                                                    "Dein Taxi riecht nach Schwefel."

                        
                
                              

        "Yo.":
        "Hallo, wo kann ich Sie hinbringen":

    label smoked_one:
        Unicorn "So lob ich's mir, das ist {i}cool{\i}."
                    "Die Worte des Einhorns füllen deinen Bauch mit wohliger Wärme"
                    Unicorn "Aber bei einer muss es doch nicht bleiben oder? Wenn du bald aufhören willst, kannst du doch heute richtig am Rad drehen!"
                    #TODO
    
