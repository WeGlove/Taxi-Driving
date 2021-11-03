label shop_staubsauger:
    $item_base_cost = base_fare * 2
    $item_cost = item_base_cost
    you "Was ist denn mit dem Handstaubsauger?"
    shopkeep "Du weißt wie deine Mitfharer immer ihre ekligen Krümel hinterlassen?"
    shopkeep "Damit bekommst du sie weg."
    shopkeep "Es macht es leicht angenehmer in deiner Müllhalde mitzufahren."
    menu: 
        "Ich bin nicht daran interessiert. Zeig mir etwas anderes.":
            return
        "Hört sich gut an. Was kostet das Ding denn?":
            shopkeep "[item_base_cost] CRP"
            $number_of_haggles = 0
            $options = [False, False, False, False, False]
            label haggle_loop:
                menu:
                    "Aber schau mal auf das Preischild!" if not options[0]:
                        shopkeep "Na gut, hab es eben etwas billiger bekommen"
                        $options[0] = True
                        $item_cost -= base_fare
                    "Dreh mal um, dass hat doch bestimmt Kratzer" if not options[1]:
                        shopkeep "Ja, ja, ok ist secon hand, der geht an dich."
                        $options[1] = True
                        $item_cost -= base_fare
                    "Schau mal auf das Baujahr, das sieht ja schon ewig alt aus." if not options[2]:
                        shopkeep "Genau, das macht es antik, und damit eigentlich teurer."
                        $options[2] = True
                        $item_cost += base_fare
                    "Das Ding hab ich doch schon im Supermarkt billiger gesehen." if not options[3]:
                        shopkeep "Na dann geh doch in den Supermarkt"
                        $options[3] = True
                    "Bitte, bitte" if not options[4]:
                        shopkeep "{i}nein.{/i}"
                        shopkeep "Mir ist grade auch wieder eingefallen, das hier ist ein Erbstück des späten Künstlers Hanswurst."
                        shopkeep "Es ist eigentlich noch sehr viel mehr wert."
                        $options[4] = True
                        $item_cost += base_fare * 2
                $number_of_haggles += 1
                if (number_of_haggles < 2):
                    jump haggle_loop
                
            if money >= item_cost:
                shopkeep "Gut, ich verkauf es dir für [item_cost] CRP"
                menu:
                    "Ich nehm's":
                        $money -= item_cost
                        $upgrades["Staubsauger"] = True
                    "Ich lass es":
                        return
                "Du hast einen Staubsauger gekauft"
            else:
                "Du hast nicht genug Geld für den Handststaubsauger"
            return