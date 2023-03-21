label shop_bilderrahmen:
    $item_ID = "Bilderrahmen"
    $item_base_cost = game.base_fare * 2
        
    you "Hmm, der Bilderrahmen sieht interessant aus."
    $text_price = game.price[item_ID]
    shopkeep "Ich werde nie verstehen warum Menschen so etwas brauchen. Aber diese Dinger sind scheinbar sehr beliebt. Du kannst zum Beispiel ein Bild deines Lieblingspassagiers rein machen.\
    Der wird sich bestimmt freuen! Kostet [text_price] CRP"
    
    
    menu:
        "Versuchen mit ihm zu feilschen" if game.haggling[item_ID] < 2:
            jump haggle_loop_bilder
        "Es nehmen":
            $game.money -= game.price[item_ID]
            $game.upgrades[item_ID] = True
            return
        "Ablehnen":
           return

    label haggle_loop_bilder:
        menu:
            "Wenn du das nicht verstehst, gibst du ihn mir bestimmt billiger" if not options[item_ID][0]:
                shopkeep "Nur weil ich nicht verstehe {i} warum {\i} Leute etwas kaufen, verstehe ich trotzdem  dass sie es kaufen"
                shopkeep "Und die Nachfrage ist gerade sehr hoch. Ich glaube, der Preis hier wäre sogar zu niedrig "
                $game.options[item_ID][0] = True
                $game.price[item_ID] += item_base_cost * 0.5
            "Bitte. {i}für  Mich{\i}" if game.options[item_ID][0]:
                shopkeep "Für dich? Dann verdopple ich den Preis eher noch. Hey... Mach doch nicht so nen Hundeblick. Na gut, dann erhöh ich den Preis eben nicht."
                
                $item_cost -= 2*game.base_fare
            "Ich habe auf der Fahrt gehört, dass Bilderrahmen eine Blase sind, die bald platzen wird." if not game.options[item_ID][1]:
                shopkeep "Blödsinn! Wobei. Du kommst wirklich rum in deinem Taxi. Ich geb ihn dir etwas billiger"
                $game.options[item_ID][1] = True
                $game.price[item_ID] -= item_base_cost * 0.5
            "Bist du dir sicher dass du dafür überhaupt noch Abnehmer findest? Der Markt an Bilderrahmen ist ja ziemlich gesättigt" if game.options[item_ID][1]:
                shopkeep"Ok. Jetzt verarschst du mich aber. Über's Ohr hauen lass' ich mich nicht. Du bezahlst den vollen Preis"
                
                
                $game.price[item_ID] += item_base_cost * 0.5
            "Den momentanen Preis akzeptieren" if game.options[item_ID][1]:
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                    return

            "Wir können auch zusammen ein Bild machen. Dann verstehst du vielleicht wieso Leute die Dinger kaufen":
                shopkeep "Ein Bild? Mit dir? Wieso sollte ich mir deine {i}hässliche{\i} Visage ansehen wollen. Wobei... Dann hab ich wenigstens was zu lachen, wenn ich 'nen schlechten Tag hab."
                "Ein Bild später"
                shopkeep "Das ist gut geworden. Jetzt brauch' ich den Rahmen aber selbst."
                return
            "Es nehmen" if game.haggling[item_ID] == 1:
                if game.money >= game.price[item_ID]:
                    shopkeep "Gut, ich verkauf es dir für [item_cost] CRP"
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
               
                    "Du hast einen Bilderrahmen gekauft"
                    return
                else:
                    "Du hast nicht genug Geld für den Bilderrahmen. Enttäuscht denkst du an all die Erinnerungen, die du darin nicht festhalten können wirst"
                    return


        $game.haggling[item_ID] += 1
        if (game.haggling[item_ID] < 2):
                    jump haggle_loop_bilder   
    if game.money >= game.price[item_ID]:
            shopkeep "Gut, ich verkauf es dir für [item_cost] CRP"
            menu:
                "Ich nehm's":
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                "Ich lass es":
                    return
            "Du hast einen Bilderrahmen gekauft"
    else:
            "Du hast nicht genug Geld für den Bilderrahmen. Enttäuscht denkst du an all die Erinnerungen, die du darin nicht festhalten können wirst"
            return