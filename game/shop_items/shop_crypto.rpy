label shop_crypto:
    $item_base_cost = game.base_fare * 2
   
    $item_ID = "Crypto Mining"
    $text_price = game.price[item_ID]
   
    you "Ich suche da noch sowas was ich auf der Seite machen kann..."
    shopkeep "Ah, da kann ich helfen. Ich habe hier noch diesen Crypto Miner. Aber ich muss dich warnen. Keiner mag Leute die Crypto Mining machen. Die sind immer so unausstehlich..."
   
    menu:
        "On second thought ":
            return
        "Ich weigere mich zu glauben, dass man von einer Tätigkeit auf Leute schließen kann!":
            shopkeep "Dann sind Pädophile nicht im Großen und Ganzen pervers?"
            shopkeep "Aber mach was du denkst ich werde dich nicht aufhalten. "
    you "Wie viel kostet das Ding denn?"
    shopkeep "[text_price] CRP"
    menu:
        "Versuchen mit ihm zu feilschen" if game.haggling[item_ID] < 2:
            jump haggle_loop_crypto
        "Es nehmen":
            $game.money -= game.price[item_ID]
            $game.upgrades[item_ID] = True
            return
        "Ablehnen":
           return
    
    
    label haggle_loop_crypto:
        menu:
            "Ist das nicht ein bisschen viel?" if not game.options[item_ID][2]:
                shopkeep "Nein."
                $ game.options[item_ID][2] = True
            "Wirklich? Ich finde das viel zu teuer!" if game.options[item_ID][2]:
                shopkeep "Dann kauf's woanders."

            "Wenn du das Ding hast. Bist letztendlich dann nicht du unausstehlich?" if not game.options[item_ID][0]:
                $game.options[item_ID][0] = True
                $game.price[item_ID] -= item_base_cost *0.5
                $text_price = game.price[item_ID]
                shopkeep "Wenn du es so sagst, will ich es eigentlich gar nicht mehr. Ich überlass es dir für  [text_price]"
                $game.options[item_ID][0] = True
                
            "Ne. Ich glaub ich lass es dir. Unaustehlicher." if game.options[item_ID][0]:
                            
                $game.price[item_ID] -= item_base_cost *0.25
                $text_price = game.price[item_ID]
                shopkeep "Bitte, ich geb es dir für [text_price] "
            "Kein Problem! Das Geld hab' ich dann mit meinem Crypto Investment gleich wieder drin!" if not game.options[item_ID][1]:
                $game.price[item_ID] += item_base_cost * 0.5
                $game.options[item_ID][1]  = True
                shopkeep "Sag ich doch. {i}Unausstehlich.{/i} Nah, wenn du sooo viel damit verdienst macht's dir doch bestimmt nichts aus, noch was draufzulegen?"
            "Selbst das hab ich in ein paar Tagen mit dem Ding wieder drin!" if game.options[item_ID][1]:
                $game.price[item_ID]+= item_base_cost *0.5
                shopkeep "Unausstehlich {b}und{/b} lernresistent. Immerhin kannst du das Ding dann ja auch gerne noch teurer haben wenn's so wertvoll ist."
            "Kein Problem! Das zahlt sich dann ja... Bäh. Das macht einen ja wirklich unausstehlich ":
                shopkeep "Sag ich doch"
                return  
            "Es nehmen" if game.haggling == 1:
                if game.money >= game.price[item_ID]:
                    $text_price = game.price[item_ID]
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                    $game.friendliness -= 1
                    "Du hast einen Cryptominer gekauft gekauft"
                    return
                else:
                    "Du hast nicht genug Geld für den Cryptominer. Vielleicht auch besser so..."
                    return
        $game.haggling[item_ID] += 1
        if (game.haggling[item_ID] < 2):
                    jump haggle_loop_crypto      
    if game.money >= game.price[item_ID]:
            $text_price = game.price[item_ID]
            shopkeep "Gut, ich verkauf es dir für [text_price] CRP"
            menu:
                "Ich nehm's":
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                    $game.friendliness -= 1
                "Ich lass es":
                    return
            "Du hast einen Cryptominer gekauft gekauft"
    else:
            "Du hast nicht genug Geld für den Cryptominer. Vielleicht auch besser so..."
            return