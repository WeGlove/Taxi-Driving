define fall_guy = Character("Ein Mann in gesundheitlicher Gefahr")
define fall_fallschirm = Character("Ein Fallschirmspringer im Hintergrund")


label passenger_fall:
    $ a, b, c = False, False, False
    "Du willst dich grade etwas entspannen, da klingelt dein Telefon"
    menu:
        "Abheben":
            "Rauschen schallt aus dem Höhrer."
            fall_guy "Entschuldigung. Ich stecke hier etwas in einer Zwickmühle. Könntest du mir zufällig helfen?"
            menu:
                "Nein":
                    fall_guy "Was? Ich sschwebe, oder eher fliege hier grade in Lebensgefahr. Bitte helfen Sie mir."
                    menu:
                        "Ok, ich mach's ja":
                            fall_guy "Danke."
                            jump passenger_fall_start
                        "Nein":
                            fall_guy "Bitte, ich flehe Sie an!"
                            menu:
                                "Ja, ja ist ja gut.":
                                    fall_guy "Danke, wirklich... Danke!"
                                    jump passenger_fall_start
                                "Nein":
                                    "Nach einem ungesunden Schmatzgeräusch bricht der Anruf ab, manche Leute sind aber auch unhöflich."
                                    return
                "Ja":
                    jump passenger_fall_start
                "Was ist denn los?" if not a:
                    fall_guy "Nun ich fliege grade durh die Luft und muss irgendwie meinen Fall sichern sobald ich nach unten falle."
                    $ a = True
                "Wie kommt es dazu, dass du durch die Luft fliegst?" if a and not b:
                    fall_guy "Ich ach- ich bin auf ein Trampolin gefallen."
                    fall_guy "Ich hab keine Zeit viel zu reden. Bitte hilf mir!"
                    $ b = True
                "Mein Gott, ich ruf sofort die Feuerwehr" if b and not c:
                    fall_guy "Keine Zeit, sobald die hier sind bin ich schon Kartoffelstampf. Hilf mir bitte!"
                    $ c = True
                    
        "Nicht Abheben":
            "Manchmal braucht man auch einfach eine Pause."
            "Du hängst auf."
            return

label passenger_fall_start:
    $ items = [False, False, False, False, False, False, False, False]
    $ items_success = [False, False, False, False, False, False, False, False]
    $ item_count = 0
    fall_guy "Ok also zusammenfassend:"
    fall_guy "Ich fliege grade in einer ungesunden Geschwindigkeit nach oben."
    fall_guy "Ich habe 8 Objekte um mich die mir beim Überleben helfen könnten."
    label passenger_fall_item:
    if item_count >=8:
        jump passenger_fall_fail
    $ item_count +=1
    fall_guy "Welches denkst du sollte ich benutzen:"
    menu:
        "Den Scherkraftbeschleuniger" if not items[0]:
            $items[0] = True
            if items_success[1] and items_success[4]:
                jump passenger_win
            if items_success[1]:
                fall_guy "Der hochenergetische Kern des Scherkraftbeschleunigers ist ausgebrannt. Ich muss einen Ersatz finden!"
                jump passenger_fall_item
            if items_success[5]:
                fall_guy "Hey, die Batterien an dem Ding sind alle. Scheiße, wenn man einmal welche gebraucht hätte."
                jump passenger_fall_item
            fall_guy "Hm, es scheint so als wären die Batterien alle. Außerdem ist der hochenergetische Kern des Beschleunigers ausgebrannt."
            fall_guy "Ich brauche Ersatz!"
            jump passenger_fall_item
                
        "Die paar Batterien" if not items[1]:
            $items[1] = True
            if items_success[4]:
                $items_success[1] = True
                fall_guy "Dank des Vogels sind Sie jetzt na genug an mir."
                jump passenger_fall_item
            fall_guy "Sie sind zu weit weg ich kann Sie nicht erreichen!"
            jump passenger_fall_item
        "Das Feuerzeug" if not items[2]:
            $items[2] = True
            fall_guy "Ok ich hab es angemacht."
        "Den vorbei fliegenden Vogel" if not items[3]:
            $items[3] = True
            if items[2]:
                fall_guy "Gute Idee. Hier schau du blöder Vogel."
                "Vogelgeschrei ertönt im Hintergrund"
                fall_guy "Gut, gut, er hat mich zerkratzt, aber immerhin sind die Batterien jetzt näher an mir dran"
                jump passenger_fall_item
            fall_guy "Er starrt mich unbeieindruckt an. Er hockt quasi auf den Batterien!"
            jump passenger_fall_item
            
        "Den Komet" if not items[4]:
            if items_success[5]:
                $items_success[4] = True
                fall_guy "Danke der Komethandschuhe hab ich kein Problem ihn aufzusammeln!"
                jump passenger_fall_item
            fall_guy "Mit meinen bloßen Händen fass ich das garantiert nicht an."
            fall_guy "Man könnte es aber vielleicht als Ersatz für den Kern des Schwerkraftbeschleumigers verwenden."
            jump passenger_fall_item
            $items[4] = True
        "Den Fallschirmspringer" if not items[5]:
            $items[5] = True
            if items_success[7]:
                $items_success[5] = True
                fall_fallschirm "Ah meine Mitgift. Besten Dank! Hier meine Komet Handschuhe sollten dir helfen können. Ich flieg dann mal weiter nach unten."
                jump passenger_fall_item
            fall_guy "Hey, könntest du mir deinen Fallschirm leihen?"
            fall_fallschirm "Nein, ich hab den letzten schon weggeworfen weil er Löcher hatte. Den hier brauch ich leider."
            fall_guy "Schade..."
            fall_fallschirm "Ich könnte dir aber meine patentierten Komethandschue geben. Dafür brauche ich aber etwas Hilfe"
            fall_guy "Ok, dass ist etwas besser als gar nichts."
            fall_fallschirm "Ich komme grade aus diesem abstpzenden Flugzeug und meine Mitgift liegt noch in meinem Gepäck."
            fall_fallschirm "Könntest du sie mir irgendwie besorgen?"
            fall_guy "Ich werde es versuchen"
            fall_fallschirm "Es würde mir vie bedeuten."
            jump passenger_fall_item
        "Den Flyer der nächsten Pizzeria" if not items[6]:
            $items[6] = True
            fall_guy "Ich habe ihn in ein Papierflugzeug gefaltet."
            jump passenger_fall_item     
        "Das abstürzende Flugzeug" if not items[7]:
            $items[7] = True
            if items[6]:
                $ items_success[7] = True
                fall_guy "Sehr clever. Ich kann den Flyer in das brennende Flugzeug werfen um die Mitgift des Fallschirmspringers zu holen. Ist ja logisch!"
                jump passenger_fall_item
            fall_guy "Hah, die Nase ist aber ungeöhnlich weit unten für ein Föugzeug. Fast so als ob irgendetwas es angezogen hätte."
            jump passenger_fall_item
    label passenger_fall_fail:
        fall_guy "Woops. Das scheint der höhepunkt des Fluges gewesen zu sein."
        fall_guy "Hat wohl doch nicht so gut geklappt wie ich mir das erhofft hab."
        fall_guy "Naja sei's drum trotzdem danke!"
        "Er legt auf."
        return
    label passenger_fall_win:
        fall_guy "Sehr gut, mit dem Komet als Kern und den Batterien für die Kontrolle ist der Schwerkraftbeschleumiger wieder einsatzfähig."
        fall_guy "Danke du hast mir echt das Leben gerettet."
        fall_guy "Bleibt nur noch meinen Fall nach oben abzubremsen."
        "Sobald der Mann auf der anderen Seite sein Gerär aktiviert hast du das Gefühl, dass sich die Erde einige Meter aus ihrer Umlaufbahn entfernt hat."
        fall_guy "Ah, scheint als wäre der Komet doch kein kompatibler Kern. Was will man machen..."
        "Er hat afugelegt."
        "Kurz darauf erhökst du eine Nachricht, Dir wurde X CRP übermittelt!"
        return
        
    