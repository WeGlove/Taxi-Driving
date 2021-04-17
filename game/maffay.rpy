define maffay = Character("Keine Ahnung")
$current_passenger_stats["paid"] = base_fare
label maffay:
    "Eine Frau mit Dreadlocks steigt in dein Taxi."
    maffay "Alter, ich bin grade so high, fahr mich einfach irgendwo hin"
    menu:
        "Dich weigern sie zu fahren":
            maffay "Alter, ich bezahl dich auch man. Hier ich hab Geld dabei"
            menu:
                "Nein, ich will keine Junkies!":
                    maffay "Alter, ...  du bist schon echt ne Systemhure, weißt du?"
                    "Sie steigt aus."
                    $current_passenger_stats["paid"] = 0
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
                                    $waterprice = 0.5*base_fare
                                    you "Das kostet [waterprice] CRP!"
                                    "Murrend gibt sie dir [waterprice] Cryptobucks"
                                    $current_passenger_stats["paid"] += 0.5*base_fare
                                "Den regulären Preis nennen":
                                    $waterprice = 0.1 *base_fare
                                    you "Das kostet [waterprice] CRP!"
                                    "Murrend gibt sie dir [waterprice] Cryptobucks"
                                    $current_passenger_stats["paid"] += 0.1*base_fare
                        
            "Nein, leider nicht":
                maffay "Schade"
        
            

        
    

