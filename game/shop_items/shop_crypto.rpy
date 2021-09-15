label crypto:
    $item_base_cost = base_fare * 2
    $item_cost = item_base_cost
    you "Ich suche da noch sowas was ich auf der Seite machen kann..."
    shopkeep "Ah, da kann ich helfen. Ich habe hier noch diesen Crypto Miner. Aber ich muss dich warnen. Keiner mag Leute die Crypto Mining machen. Die sind immer so unausstehlich..."
    menu:
        "On second thought ":
            return
        "Ich weigere mich zu glauben, dass man von einer Tätigkeit auf Leute schließen kann!":
            shopkeep "Dann sind Pädophile nicht im Großen und Ganzen pervers?"
            shopkeep "Aber mach was du denkst ich werde dich nicht aufhalten. "
    you "Wie viel kostet das Ding denn?"
    shopkeep "[item_base_cost] CRP"
    $number_of_haggles = 0
    $options = [False, False, False, False, False]
    label haggle_loop_crypto:
        menu:
            "Ist das nicht ein bisschen viel?" if not options[2]:
                shopkeep "Nein."
                $ options[2] = True
            "Wirklich? Ich finde das viel zu teuer!" if options[2]:
                shopkeep "Dann kauf's woanders."

            "Wenn du das Ding hast. Bist letztendlich dann nicht du unausstehlich?" if not options[0]:
                $options[0] = True
                $item_cost -= base_fare
                shopkeep "Wenn du es so sagst, will ich es eigentlich gar nicht mehr. Ich überlass es dir für [item_cost] "
                $options[0] = True
                $item_cost -= base_far
            "Ne. Ich glaub ich lass es dir. Unaustehlicher." if options[0]:
                            
                $item_cost -= base_fare
                shopkeep "Bitte, ich geb es dir für [item_cost] "
            "Kein Problem! Das Geld hab' ich dann mit meinem Crypto Investment gleich wieder drin!" if not options[1]:
                $item_cost += base_fare
                $options[1]  = True
                shopkeep "Sag ich doch. {i}Unausstehlich.{/i} Nah, wenn du sooo viel damit verdienst macht's dir doch bestimmt nichts aus, noch was draufzulegen?"
            "Selbst das hab ich in ein paar Tagen mit dem Ding wieder drin!" if options[1]:
                $item_cost += base_fate
                shopkeep "Unausstehlich {b}und{/b} lernresistent. Immerhin kannst du das Ding dann ja auch gerne noch teurer haben wenn's so wertvoll ist."
            "Kein Problem! Das zahlt sich dann ja.. Bäh. Das macht einen ja wirklich unausstehlich ":
                shopkeep "Sag ich doch"
                return  
        $number_of_haggles += 1
        if (number_of_haggles < 2):
                    jump haggle_loop_crypto      
    if money >= item_cost:
            shopkeep "Gut, ich verkauf es dir für [item_cost] CRP"
            menu:
                "Ich nehm's":
                    $money -= item_cost
                    $upgrades["crypto"] = True
                "Ich lass es":
                    return
            "Du hast einen Cryptominer gekauft gekauft"
    else:
            "Du hast nicht genug Geld für den Cryptominer. Vielleicht auch besser so..."
            return