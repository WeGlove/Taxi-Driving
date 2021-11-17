label shop_bilderrahmen:
    $item_ID = "Bilderrahmen"
    $item_base_cost = base_fare * 2
    $item_cost = item_base_cost
    you "Hmm, der Bilderrahmen sieht interessant aus."
    shopkeep "Ich werde nie verstehen warum Menschen so etwas brauchen. Aber diese Dinger sind scheinbar sehr beliebt. Kostet [item_base_cost] CRP"
    
    $options = [False, False, False, False, False]
    menu:
        "Versuchen mit ihm zu feilschen" if haggling[item_ID] < 2:
            jump haggle_loop_bilder
        "Es nehmen":
            $money -= item_cost
            $upgrades[item_ID] = True
            return
        "Ablehnen":
           return

    label haggle_loop_bilder:
        menu:
            "Wenn du das nicht verstehst, gibst du ihn mir bestimmt billiger" if not options[0]:
                shopkeep "Nur weil ich nicht verstehe {i} warum {\i} Leute etwas kaufen, verstehe ich trotzdem  dass sie es kaufen"
                shopkeep "Und die Nachfrage ist gerade sehr hoch. Ich glaube, der Preis hier wäre sogar zu niedrig "
                $options[0] = True
                $item_cost += 2*base_fare
            "Bitte. {i}für  Mich{\i}" if options[0]:
                shopkeep "Für dich? Dann verdopple ich den Preis eher noch. Hey... Mach doch nicht so nen Hundeblick. Na gut, dann erhöh ich den Preis eben nicht."
                
                $item_cost -= 2*base_fare
            "Ich habe auf der Fahrt gehört, dass Bilderrahmen eine Blase sind, die bald platzen wird." if not options[1]:
                shopkeep "Blödsinn! Wobei. Du kommst wirklich rum in deinem Taxi. Ich geb ihn dir etwas billiger"
                $options[1] = True
                $item_cost -= 2*base_fare
            "Bist du dir sicher dass du dafür überhaupt noch Abnehmer findest? Der Markt an Bilderrahmen ist ja ziemlich gesättigt" if options[1]:
                shopkeep"Ok. Jetzt verarschst du mich aber. Über's Ohr hauen lass' ich mich nicht. Du bezahlst den vollen Preis"
                shopkeep "Blödsinn! Wobei. Du kommst wirklich rum in deinem Taxi. Ich geb ihn dir etwas billiger"
                
                $item_cost += 2* base_fare
            "Wir können auch zusammen ein Bild machen. Dann verstehst du vielleicht wieso Leute die Dinger kaufen":
                shopkeep "Ein Bild? Mit dir? Wieso sollte ich mir deine {i}hässliche{\i} Visage ansehen wollen. Wobei... Dann hab ich wenigstens was zu lachen, wenn ich 'nen schlechten Tag hab."
                "Ein Bild später"
                shopkeep "Das ist gut geworden. Jetzt brauch' ich den Rahmen aber selbst."
                return
        $haggling[item_ID] += 1
        if (haggling[item_ID] < 2):
                    jump haggle_loop_bilder   
    if money >= item_cost:
            shopkeep "Gut, ich verkauf es dir für [item_cost] CRP"
            menu:
                "Ich nehm's":
                    $money -= item_cost
                    $upgrades[item_ID] = True
                "Ich lass es":
                    return
            "Du hast einen Bilderrahmen gekauft"
    else:
            "Du hast nicht genug Geld für den Bilderrahmen. Enttäuscht denkst du an all die Erinnerungen, die du darin nicht festhalten können wirst"
            return