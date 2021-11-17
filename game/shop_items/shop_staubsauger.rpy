label shop_staubsauger:
    $item_base_cost = base_fare * 2
  
    $item_ID = "Staubsauger"
    
    you "Was ist denn mit dem Handstaubsauger?"
    shopkeep "Du weißt wie deine Mitfharer immer ihre ekligen Krümel hinterlassen?"
    shopkeep "Damit bekommst du sie weg."
    shopkeep "Es macht es leicht angenehmer in deiner Müllhalde mitzufahren."
     
    menu: 
        
        "Ich bin nicht daran interessiert. Zeig mir etwas anderes.":
            return
        "Hört sich gut an. Was kostet das Ding denn?":
            $text_price = price[item_ID]
            shopkeep "[text_price] CRP"
            menu:
                "Versuchen mit ihm zu feilschen" if haggling[item_ID] < 2:
                    jump haggle_loop
                "Es nehmen":
                    $money -= price[item_ID]
                    $upgrades[item_ID] = True
                    return
                "Ablehnen":
                    return
            
            label haggle_loop:
                menu:
                    "Aber schau mal auf das Preischild!" if not options[item_ID][0]:
                        shopkeep "Na gut, hab es eben etwas billiger bekommen"
                        $options[item_ID][0] = True
                        $price[item_ID] -= base_fare
                    "Dreh mal um, dass hat doch bestimmt Kratzer" if not options[item_ID][1]:
                        shopkeep "Ja, ja, ok ist secon hand, der geht an dich."
                        $options[item_ID][1] = True
                        $price[item_ID] -= base_fare
                    "Schau mal auf das Baujahr, das sieht ja schon ewig alt aus." if not options[item_ID][2]:
                        shopkeep "Genau, das macht es antik, und damit eigentlich teurer."
                        $options[item_ID][2] = True
                        $price[item_ID] += base_fare
                    "Das Ding hab ich doch schon im Supermarkt billiger gesehen." if not options[item_ID][3]:
                        shopkeep "Na dann geh doch in den Supermarkt"
                        $options[item_ID][3] = True
                    "Bitte, bitte" if not options[item_ID][4]:
                        shopkeep "{i}nein.{/i}"
                        shopkeep "Mir ist grade auch wieder eingefallen, das hier ist ein Erbstück des späten Künstlers Hanswurst."
                        shopkeep "Es ist eigentlich noch sehr viel mehr wert."
                        $options[item_ID][4] = True
                        $price[item_ID] += base_fare * 2
                $haggling[item_ID] += 1
                if (haggling[item_ID] < 2):
                    jump haggle_loop
                
            if money >= price[item_ID]:
                $text_price = price[item_ID]
                shopkeep "Gut, ich verkauf es dir für [text_price] CRP"
                menu:
                    "Ich nehm's":
                        $money -= price[item_ID]
                        $upgrades[item_ID] = True
                    "Ich lass es":
                        return
                "Du hast einen Staubsauger gekauft"
            else:
                "Du hast nicht genug Geld für den Handststaubsauger"
            return