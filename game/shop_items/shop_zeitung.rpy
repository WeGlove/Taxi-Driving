label shop_zeitungen:
    $item_base_cost = base_fare * 2
    $item_cost = item_base_cost
    you "Was ist denn mit den Zeitungen?"
    shopkeep "Du wei�t wie deine Mitmenschen immer mit dir reden obwohl du dich eigentlich auf die Stra�e konzenteren sollst?"
    shopkeep "Naja die Zeitungen helfen da auch nicht, aber immerhin hast du nach deiner Schicht was zum lesen."
    menu: 
        "Ich bin nicht daran interessiert. Zeig mir etwas anderes.":
            return
        "H�rt sich gut an. Was kosten die denn?":
            shopkeep "[item_base_cost] CRP"
            $number_of_haggles = 0
            $options = [False, False, False, False, False]
            label haggle_loop:
                menu:
                    "Aber die sind doch schon Jahre alt!" if not options[0]:
                        shopkeep "Na, eben. Es waren die Nachrichten, jetzt sind es Geschichtsb�cher!"
                        $options[0] = True
                        $item_cost -= base_fare
                    "Da sind ja Kaffeeflecken drauf!" if not options[1]:
                        shopkeep "Ja, stimmt schon."
                        $options[1] = True
                        $item_cost -= base_fare
                    "Die w�rd ich morgens in jedem Papierm�ll umsonst bekommen." if not options[2]:
                        shopkeep "Du siehst auch wie jemand aus der morgens im M�ll w�hlt."
                        $options[2] = True
                        $item_cost += base_fare
                    "Darfst du die �berhaupt verkaufen?" if not options[3]:
                        shopkeep "Nat�rlich. Ich stehe �ber dem Gesetz."
                        $options[3] = True
                    "Liest du gerne Zeitung?" if not options[4]:
                        shopkeep "Klar. Aber nicht dieses K�seblatt"
                        $options[4] = True
                        $item_cost += base_fare * 2
                $number_of_haggles += 1
                if (number_of_haggles < 2):
                    jump haggle_loop
                
            if money >= item_cost:
                shopkeep "Gut, ich verkauf es dir f�r [item_cost] CRP"
                menu:
                    "Ich nehm's":
                        $money -= item_cost
                        $upgrades["zeitungen"] = True
                    "Ich lass es":
                        return
                "Du hast einen Haufen alter Zeitungen gekauft."
                "War es das Wert?"
            else:
                "Du hast nicht gnug Geld f�r die Zeitungen."
                "Ist vielleicht auch besser so."
            return