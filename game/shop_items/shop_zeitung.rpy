


label shop_zeitungen:
    $item_base_cost = base_fare * 2

    $item_ID ="Zeitungen"
    you "Was ist denn mit den Zeitungen?"
    shopkeep "Du weißt wie deine Mitmenschen immer mit dir reden obwohl du dich eigentlich auf die Straße konzenteren sollst?"
    shopkeep "Naja die Zeitungen helfen da auch nicht, aber immerhin hast du nach deiner Schicht was zum lesen."
    menu: 
        "Ich bin nicht daran interessiert. Zeig mir etwas anderes.":
            return
        "Hört sich gut an. Was kosten die denn?":
            $text_price = price[item_ID]
            shopkeep "[text_price] CRP"
            
            
            menu:
                "Versuchen mit ihm zu feilschen" if haggling[item_ID] < 2:
                    jump haggle_loop_zeitung
                "Es nehmen":
                    $money -= price[item_ID]
                    $upgrades[item_ID] = True
                    return
                "Ablehnen":
                    return
            label haggle_loop_zeitung:
                menu:
                    "Aber die sind doch schon Jahre alt!" if not options[item_ID][0]:
                        shopkeep "Na, eben. Es waren die Nachrichten, jetzt sind es Geschichtsbücher!"
                        $options[0] = True
                        $price[item_ID] -= base_fare
                    "Da sind ja Kaffeeflecken drauf!" if not options[item_ID][1]:
                        shopkeep "Ja, stimmt schon."
                        $options[item_ID][1] = True
                        $price[item_ID] -= base_fare
                    "Die würd ich morgens in jedem Papiermüll umsonst bekommen." if not options[item_ID][2]:
                        shopkeep "Du siehst auch wie jemand aus der morgens im Müll wühlt."
                        $options[item_ID][2] = True
                        $price[item_ID] += base_fare
                    "Darfst du die überhaupt verkaufen?" if not options[item_ID][3]:
                        shopkeep "Natürlich. Ich stehe über dem Gesetz."
                        $options[item_ID][3] = True
                    "Liest du gerne Zeitung?" if not options[item_ID][4]:
                        shopkeep "Klar. Aber nicht dieses Käseblatt"
                        $options[item_ID][4] = True
                        $price[item_ID] += base_fare * 2
                $haggling[item_ID] += 1
                if (haggling[item_ID] < 2):
                    jump haggle_loop_zeitung
                
            if money >= price[item_ID]:
                $text_price = price[item_ID]
                shopkeep "Gut, ich verkauf es dir für [text_price] CRP"
                menu:
                    "Ich nehm's":
                        $money -= price[item_ID]
                        $upgrades[item_ID] = True
                    "Ich lass es":
                        return
                "Du hast einen Haufen alter Zeitungen gekauft."
                "War es das Wert?"
            else:
                "Du hast nicht gnug Geld für die Zeitungen."
                "Ist vielleicht auch besser so."
            return