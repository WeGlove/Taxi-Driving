define maffay = Character("Keine Ahnung")

label maffay:


    $current_passenger.paying = game.get_base_fare()

    "Eine Frau mit rot geränderten Augen steigt in dein Taxi."
    maffay "Alter, ich bin grade so high, fahr mich einfach irgendwo hin"
    menu:
        "Dich weigern sie zu fahren":
            maffay "Alter, ich bezahl dich auch man. Hier ich hab Geld dabei"
            menu:
                "Nein, ich will keine Junkies!":
                    maffay "Alter, ...  du bist schon echt ne Systemhure, weißt du?"
                    "Sie steigt aus."
                    $current_passenger.paying = 0
                    return
                "Na gut, Geld ist Geld.":
                    menu:
                        "Schön einen durchgezogen?":
                            maffay "Aber so richtig Alter, ich brauch kurz einen Moment zum Runterkommen"
                        "Schöner Tag heute.":
                            maffay "Hä?"
                            menu:
                                "Dich wiederholen":
                                    maffay "Alter, du musst doch genauso high sein wie ich, wenn du unsere Situation momentan schön findest"
                                "Ach, nichts":
                                    "Sie starrt aus dem Fenster"
        "Schön einen durchgezogen?":
            maffay "Aber so richtig Alter, ich brauch kurz einen Moment zum Runterkommen"
        "Schöner Tag heute.":
            maffay "Hä?"
            menu:
                "Dich wiederholen":
                   maffay "Alter, du musst doch genauso high sein wie ich, wenn du unsere Situation momentan schön findest"
                "Ach, nichts":
                    "Sie starrt aus dem Fenster"
    "Nach einiger Zeit fragt sie:"
    maffay "Alter, hast du 'n bisschen Wasser?"
    menu: 
            "Klar, kostet aber extra.":
                maffay "Kannst'e da net mal ne Ausnahme machen?"
                menu:
                    "Ja":
                        "Danke, Mann"
                    "Nein":
                        maffay "Sie stöhnt. Was kostet's denn?"
                        menu:
                                "Versuchen sie abzuzocken":
                                    $waterprice = 0.5 * game.base_fare
                                    you "Das kostet [waterprice] CRP!"
                                    "Murrend gibt sie dir [waterprice] Cryptobucks"
                                    $current_passenger.paying += 0.5 * game.base_fare
                                "Den regulären Preis nennen":
                                    $waterprice = 0.1 * game.base_fare
                                    you "Das kostet [waterprice] CRP!"
                                    "Murrend gibt sie dir [waterprice] Cryptobucks"
                                    $current_passenger.paying += 0.1 * game.base_fare
                        
            "Nein, leider nicht":
                maffay "Schade"
            "Normalerweise kostet das extra, aber das geht heute auf mich":
                maffay "Alter du bist echt voll ok"
                "Glücklich lächelnd verlässt sie an der nächsten Pommesbude dein Taxi."
                $current_passenger.paying -= 0.1 * game.base_fare        
            

        
    

