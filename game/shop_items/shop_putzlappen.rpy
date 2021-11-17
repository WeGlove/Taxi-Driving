label shop_putzlappen:
    $item_base_cost = base_fare * 2
    $item_cost = item_base_cost
    you "Was ist denn mit dem Fensterputzlappen da?"
    shopkeep "Oh der den hab ich da nur liegen um die Vitrinen zu... Äh, ich meine, der interessiert dich? [item_base_cost] CRP!"
    $number_of_haggles = 0
    $options = [False, False, False, False, False]
    label haggle_loop_putze:
        menu:
            "Das ist ein Lappen..." if not options[0]:
                shopkeep "Und noch so viel mehr, wenn man ihn richtig einsetzt. Wenn ich es mir recht überlege ist der Preis sogar noch zu billig" 
                $options[0] = True
                $item_cost += base_fare
            "Wie war das mit den Vitrinen?" if not options[1]:
                shopkeep "Na gut vielleicht ist der Preis ein {i}bisschen{/i} übertrieben."
                $options[1] = True
                $item_cost -= base_fare
            "Sir. Das ist ein {i}Lappen{/i}" if options[0]:
                shopkeep "Ich bin {b}enttäuscht{/b} von deinem Mangel an Vorstellungsvermögen. Du kannst ihn zum Beispiel auch als Kopftuch verwenden. Oder als Taschentuch. So viele Möglichkeiten. Diese Elabnoration ist übrigens nicht um sonst"
                $item_cost += base_fare
            "Der ist dann doch benutzt, oder?" if options[1]:
                shopkeep "Vielleicht kann ich an dem Preis doch noch was machen"
                $item_cost -= base_fare
            "So viele Möglichkeiten..." if not options [2]:
                $options[2] = True
                shopkeep "Ja. Ein Lappen kann schon nützlich sein."
            "... Endlos viele Möglichkeiten":
                shopkeep"Wenn du das so sagst, sollte ich es vielleicht noch etwas teurer machen"
                $item_cost += base_fare
        $number_of_haggles += 1
        if (number_of_haggles < 2):
                    jump haggle_loop_putze      
    if money >= item_cost:
            shopkeep "Gut, ich verkauf es dir für [item_cost] CRP"
            menu:
                "Ich nehm's":
                    $money -= item_cost
                    $upgrades["crypto"] = True
                "Ich lass es":
                    return
            "Du hast einen Lappen gekauft"
    else:
            "Du hast nicht genug Geld für den Cryptominer. Vielleicht auch besser so..."
            return
    