label shop_putzlappen:
    $item_ID = "Putzlappen"
    $item_base_cost = game.base_fare * 2
    
    you "Was ist denn mit dem Fensterputzlappen da?"
    $text_price = game.price[item_ID]
    shopkeep "Oh der den hab ich da nur liegen um die Vitrinen zu... Äh, ich meine, der interessiert dich? [text_price] CRP!"
    menu:
        "Versuchen mit ihm zu feilschen" if game.haggling[item_ID] < 2:
            jump haggle_loop_putze
        "Es nehmen":
            $game.money -= game.price[item_ID]
            $game.upgrades[item_ID] = True
            return
        "Ablehnen":
           return
    
    label haggle_loop_putze:
        menu:
            "Das ist ein Lappen..." if not game.options[item_ID][0]:
                shopkeep "Und noch so viel mehr, wenn man ihn richtig einsetzt. Wenn ich es mir recht überlege ist der Preis sogar noch zu billig" 
                $game.options[item_ID][0] = True
                $game.price[item_ID] += game.base_fare
            "Wie war das mit den Vitrinen?" if not game.options[item_ID][1]:
                shopkeep "Na gut vielleicht ist der Preis ein {i}bisschen{/i} übertrieben."
                $game.options[item_ID][1] = True
                $game.price[item_ID] -=game.base_fare
            "Sir. Das ist ein {i}Lappen{/i}" if game.options[item_ID][0]:
                shopkeep "Ich bin {b}enttäuscht{/b} von deinem Mangel an Vorstellungsvermögen. Du kannst ihn zum Beispiel auch als Kopftuch verwenden. Oder als Taschentuch. So viele Möglichkeiten. Diese Elabnoration ist übrigens nicht um sonst"
                $game.price[item_ID] += game.base_fare
            "Der ist dann doch benutzt, oder?" if game.options[item_ID][1]:
                shopkeep "Vielleicht kann ich an dem Preis doch noch was machen"
                $game.price[item_ID] -= game.base_fare
            "So viele Möglichkeiten..." if not game.options[item_ID][2]:
                $game.options[item_ID][2] = True
                shopkeep "Ja. Ein Lappen kann schon nützlich sein."
            "... Endlos viele Möglichkeiten":
                shopkeep"Wenn du das so sagst, sollte ich es vielleicht noch etwas teurer machen"
                $game.price[item_ID] += game.base_fare
        $game.haggling[item_ID] +=1
        if (game.haggling[item_ID] < 2):
                    jump haggle_loop_putze      
    if game.money >= game.item_cost:
            $text_price = game.price[item_ID]
            shopkeep "Gut, ich verkauf es dir für [text_price] CRP"
            menu:
                "Ich nehm's":
                    $game.money -= game.price[item_ID]
                    $game.upgrades[item_ID] = True
                    $game.friendliness += 3
                "Ich lass es":
                    return
            "Du hast einen Lappen gekauft"
    else:
            "Du hast nicht genug Geld für den Cryptominer. Vielleicht auch besser so..."
            return
    