label shop_staubsauger:
    $item_base_cost = game.base_fare * 2
  
    $item_ID = "Staubsauger"
    
    you "Was ist denn mit dem Handstaubsauger?"
    shopkeep "Du weißt wie deine Mitfharer immer ihre ekligen Krümel hinterlassen?"
    shopkeep "Damit bekommst du sie weg."
    shopkeep "Es macht es leicht angenehmer in deiner Müllhalde mitzufahren."
     
    menu: 
        
        "Ich bin nicht daran interessiert. Zeig mir etwas anderes.":
            return
        "Hört sich gut an. Was kostet das Ding denn?":
            $text_price = game.price[item_ID]
            shopkeep "[text_price] CRP"
            menu:
                "Versuchen mit ihm zu feilschen" if game.haggling[item_ID] < 2:
                    jump haggle_loop
                "Es nehmen":
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                    "Du hast einen Staubsauger gekauft"
                    if game.upgrades["Putzlappen"]:
                                jump awesome_kombo
                    return
                "Ablehnen":
                    return
            
            label haggle_loop:
                menu:
                    "Aber schau mal auf das Preischild!" if not game.options[item_ID][0]:
                        shopkeep "Na gut, hab es eben etwas billiger bekommen"
                        $game.options[item_ID][0] = True
                        $game.price[item_ID] -= game.base_fare
                    "Dreh mal um, dass hat doch bestimmt Kratzer" if not game.options[item_ID][1]:
                        shopkeep "Ja, ja, ok ist secon hand, der geht an dich."
                        $game.options[item_ID][1] = True
                        $game.price[item_ID] -= game.base_fare
                    "Schau mal auf das Baujahr, das sieht ja schon ewig alt aus." if not game.options[item_ID][2]:
                        shopkeep "Genau, das macht es antik, und damit eigentlich teurer."
                        $game.options[item_ID][2] = True
                        $game.price[item_ID] += game.base_fare
                    "Das Ding hab ich doch schon im Supermarkt billiger gesehen." if not game.options[item_ID][3]:
                        shopkeep "Na dann geh doch in den Supermarkt"
                        $game.options[item_ID][3] = True
                    "Bitte, bitte" if not game.options[item_ID][4]:
                        shopkeep "{i}nein.{/i}"
                        shopkeep "Mir ist grade auch wieder eingefallen, das hier ist ein Erbstück des späten Künstlers Hanswurst."
                        shopkeep "Es ist eigentlich noch sehr viel mehr wert."
                        $game.options[item_ID][4] = True
                        $game.price[item_ID] += game.base_fare * 2
                    "Es nehmen" if game.haggling[item_ID] == 1:
                        if game.money >= game.item_cost:
                            $game.money -= game.price[item_ID]
                            $game.upgrades[item_ID] = True
                            $game.friendliness += 2
                            "Du hast einen Staubsauger gekauft"
                            if game.upgrades["Putzlappen"]:
                                jump awesome_kombo
                            return
                        else:
                            "Du hast nicht genug Geld für einen Handstaubsauger."
                            return
                $game.haggling[item_ID] += 1
                if (game.haggling[item_ID] < 2):
                    jump haggle_loop
                
            if game.money >= game.price[item_ID]:
                $text_price = game.price[item_ID]
                shopkeep "Gut, ich verkauf es dir für [text_price] CRP"
                menu:
                    "Ich nehm's":
                        $game.money -= game.price[item_ID]
                        $game.upgrades[item_ID] = True
                        $game.friendliness += 2
                        "Du hast einen Staubsauger gekauft"
                        if game.upgrades["Putzlappen"]:
                                jump awesome_kombo
                    "Ich lass es":
                        return
                
            else:
                "Du hast nicht genug Geld für den Handststaubsauger"
            return

    label awesome_kombo:
            "{b} KOMBOBONUS {\b}"
            "{b} KOMBOBONUS! {\b}"
            "{b} KOMBOBONUS!! {\b}"
            "{b} KOMBOBONUS!!! {\b}"
            "Zusammen mit dem Lappen der Renigung entfaltet der legendäre Staubsauger von Peter Maffay seine wahre Kraft!"
            "Die Menschen nehmen dein Taxi jetzt als blitzblank war!"
            $game.friendliness += 1
            return 
