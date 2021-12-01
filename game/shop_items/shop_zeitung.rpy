


label shop_zeitungen:
    $item_base_cost = game.base_fare * 2

    $item_ID ="Zeitungen"
    you "Was ist denn mit den Zeitungen?"
    shopkeep "Du weißt wie deine Mitmenschen immer mit dir reden obwohl du dich eigentlich auf die Straße konzenteren sollst?"
    shopkeep "Naja die Zeitungen helfen da auch nicht, aber immerhin hast du nach deiner Schicht was zum lesen."
    menu: 
        "Ich bin nicht daran interessiert. Zeig mir etwas anderes.":
            return
        "Hört sich gut an. Was kosten die denn?":
            $text_price = game.price[item_ID]
            shopkeep "[text_price] CRP"
            
            
            menu:
                "Versuchen mit ihm zu feilschen" if game.haggling[item_ID] < 2:
                    jump haggle_loop_zeitung
                "Es nehmen":
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                    return
                "Ablehnen":
                    return
            label haggle_loop_zeitung:
                menu:
                    "Aber die sind doch schon Jahre alt!" if not game.options[item_ID][0]:
                        shopkeep "Na, eben. Es waren die Nachrichten, jetzt sind es Geschichtsbücher!"
                        $game.options[0] = True
                        $game.price[item_ID] -= game.base_fare
                    "Da sind ja Kaffeeflecken drauf!" if not game.options[item_ID][1]:
                        shopkeep "Ja, stimmt schon."
                        $game.options[item_ID][1] = True
                        $game.price[item_ID] -= game.base_fare
                    "Die würd ich morgens in jedem Papiermüll umsonst bekommen." if not options[item_ID][2]:
                        shopkeep "Du siehst auch wie jemand aus der morgens im Müll wühlt."
                        $game.options[item_ID][2] = True
                        $game.price[item_ID] += game.base_fare
                    "Darfst du die überhaupt verkaufen?" if not game.options[item_ID][3]:
                        shopkeep "Natürlich. Ich stehe über dem Gesetz."
                        $game.options[item_ID][3] = True
                    "Liest du gerne Zeitung?" if not game.options[item_ID][4]:
                        shopkeep "Klar. Aber nicht dieses Käseblatt"
                        $game.options[item_ID][4] = True
                        $game.price[item_ID] += game.base_fare * 2
                $game.haggling[item_ID] += 1
                if (game.haggling[item_ID] < 2):
                    jump haggle_loop_zeitung
                
            if game.money >= game.price[item_ID]:
                $text_price = game.price[item_ID]
                shopkeep "Gut, ich verkauf es dir für [text_price] CRP"
                menu:
                    "Ich nehm's":
                        $game.money -= game.price[item_ID]
                        $game.upgrades[item_ID] = True
                    "Ich lass es":
                        return
                "Du hast einen Haufen alter Zeitungen gekauft."
                "War es das Wert?"
            else:
                "Du hast nicht gnug Geld für die Zeitungen."
                "Ist vielleicht auch besser so."
            return