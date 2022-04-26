define passenger_debts = Character("Der Praktikant")

label passenger_debts_who:
    passenger_debts "ja ähh, ihr vertrautes Finanzinstitut schickt mich."
    $game.debt_collector.status["who"] = True
    return
    
label passenger_debts_engage:
    menu:
        "Ich hab keine Lust mich mit bürokratischem Mist rumzuschlagen":
            passenger_debts "Äh ja, ähh, also, wissen Sie, das ist ja so ne Sache mit der Verwaltung."
            passenger_debts "Es ginge hier dann um ein ... ähm, vertragsrechtliches... Problem. Verstehen Sie?"
            label passenger_debts_who_ret_1:
            menu:
                "Was will Robby denn jetzt schon wieder?":
                    passenger_debts "Also, ich ähh, hm, also ... ähhhh"
                    passenger_debts "..."
                    "..."
                    you "..."
                    passenger_debts "Also,ja, ähh, gut das Sie das anscheinend schon bei dem Herren auf dem Schirm haben"
                    passenger_debts "Ich... ähh, werde dann bescheid geben das der Herr Robby sich darum kümmert."
                    "Er verlässt deinen Wagen, sichtlich erleichtert."
                    return
                "Wer schickt Sie denn?" if not game.debt_collector.status["who"]:
                    call passenger_debts_who
                    jump passenger_debts_who_ret_1
                "Ich hab jetzt keine Zeit für sowas. Können wir das nicht auf einen anderen Termin verschieben":
                    passenger_debts "Ja ähh, also, öhm, das war so jetzt auch eigentlich nicht geplant... aber äh, wann würde es denn gehen."
                    you "Wie wäre es mit nächster Woche?"
                    passenger_debts "Gut ähh, ich werde Sie dann, ähmm, dementsprechend nocheinmal k-kontaktieren."
                    "Er verlässt deinen Wagen, sichtlich erleichtert."
                    return
        "Etwas 'Verwaltungstechnisches'?":
            passenger_debts "Ja, Sie müssen sehen, Sie haben bei meiner Firma, ein leichtes ähh, Problem, in der Finanzverwaltung..."
            passenger_debts "Sie... haben Schulden..."
            menu:
                "Was interessiert mich das?":
                    passenger_debts "Ähhm, ja, äh, tja, also wenn Sie äh, wenn Sie nicht zahlen, wird die Bank irgendwann äh.. zu Pfändungen übergehen."
                    "Nachdem er dich informiert hat. tritt der Mann aus deinem Wagen. Er ist sichtlich erleichtert."
                "Sie sind doch ein gut aussehender Mann. Wir finden hier doch sicher eine Lösung die uns beiden gefällt.":
                    passenger_debts "Ähh, ähhm, ja, also, was, äh, ja, hm,..., ähh, ..., .... ,......, wie bitte?"
                    "Der Mann fällt in Ohnmacht"
                    menu:
                        "Ihn auf den Bürgersteig legen":
                            "Er liegt auf dem Bürgersteig."
                            "Er wirkt viel entspannter als vorher."
                            "Du fährst weg."
                            return
                        "Bei ihm bleiben bis es ihm wieder besser geht.":
                            "Nach einer Weile, wacht er wieder auf."
                            passenger_debts "Hmm? Was, wie, Gummibärchen? Was war nochma-"
                            "Er sieht dich an. Seine Augen weiten sich."
                            passenger_debts "Ja, äh, e-entschuldigung, f-für die Unanehmlichk-keiten. Ich w-werde dann erst mal wieder gehen."
                            passenger_debts "D-Danke, äh für die Hilfe."
                            "Er geht"
                            return
                "Können Sie das beweisen?":
                    "Plötzlich weandelt sich der Gesichtsausdruck des Mannes von Nervosität zu bitterer Entschlossenheit."
                    passenger_debts "Sie haben genau [game.money] CRP auf ihrem Konto bei unserer Bank."
                    passenger_debts "Dies geht aus ihrer Transaktionsgeschichte hervor, die sich hier, hier und hier anschauen können."
                    "Er legt dir ein paar Dokumente vor."
                    passenger_debts "Wenn Sie nicht in der Lage sind zu zahlen wird ihre Bank ihnen gerne dabei behilflich sein, ihre bisher gekauften Güter zu pfänden."
                    passenger_debts "Außerderm wurde ein permamnenter Eintrag ihrer Überziehung in ihre Akte eingetragen."
                    passenger_debts "Wenn Sie nicht pfänden wollen wird die Bank einen Schuldeneintreiber schicken der sich ihrer Güter für Sie entledigt."
                    passenger_debts "Wenn Sie noch weitere Fragen haben melden Sie sich bei mir."
                    passenger_debts  "Hier ist meine Karte."
                    "Er gibt dir seine Karte."
                    "'Pit Neuer, Praktikant bei der Bank'"
                    passenger_debts "Wenn Sie mich jetzt entschuldigen würden."
                    "Er öffnet die Tür des Autos und geht hinaus."
                    return
                "Ok, ja das stimmt, ich bin im Minus.":
                    passenger_debts "A-Also, wenn sie ähh, wenn sie wollen, kann ich vielleicht ein paar ihrer Sachen pfänden, wenn Sie äh, das möchten."
                    menu:
                        "Ich will nichts pfänden":
                            passenger_debts "A - äh- ja na gut. Dann m-muss ich ihnen leider mitteilen, d-dass die Bank i-ihnen einen Eintrag in ihrer Akte verzeichnet."
                            passenger_debts "W-wenn, s-sie mich dann entschuldigen würden."
                            "Er verlässt deinen Wagen."
                            return.
        "Wer schickt Sie denn?" if not game.debt_collector.status["who"]:
            call passenger_debts_who
            jump passenger_debts_who_ret_2

label passenger_debts:
    $game.debt_collector.status["who"] = False
    "Was für ein schönes Gefühl." 
    "Du bist mit der Arbeit für heute fertig"
    "..."
    "Es klopft an deine Wagentür."
    "Ein Mann im Anzug hält nervös ein Klemmbrett unterm Arm und versucht deine Aufmerksamkeit zu bekommen."
    menu:
        "Wegfahren":
            "Du fährst weg."
            "Er starrt dir nach und weiß nicht was er tun soll."
        "Ihm die Tür öffnen":
            passenger_debts "E-Entschuldigung, ja, äh, hmhmm, guten Tag..."
        
            menu:
                "Ich bin schon fertig für heute!":
                    passenger_debts "E-Es geht auch nicht ums Fahren, sondern eher um etwas... ähh... Verwaltungstechnisches?"
                    jump passenger_debts_engage
                "Was gibt's denn?":
                    passenger_debts "Nu- ähem- nun es äh, es geht um etwas verwaltungstechnisches."
                    jump passenger_debts_engage
                "Fahrten nach den Öffnungszeiten kosten extra.":
                    passenger_debts "E-Es geht auch nicht ums Fahren, sondern eher um etwas... ähh... Verwaltungstechnisches?"
                    jump passenger_debts_engage
                "Ich bin eigentlich schon fertig für heute aber für Sie mach ich eine Ausnahme.":
                    "E-Es geht auch nicht ums Fahren, sondern eher um etwas... ähh... Verwaltungstechnisches?"
                    jump passenger_debts_engage
    

