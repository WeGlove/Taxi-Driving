define maffay = Character("Keine Ahnung")

label maffay:
    "Eine Frau mit Treadlocks steigt in dein Taxi."
    maffay "Alter ich bin grade so high, fahr mich einfach irgendwo hin"
    menu:
        "Dich weigern sie zu fahren":
            $weigern = True
            "Du scheuchst sie aus dem Taxi"
        "Schön einen durchgezogen?":
            maffay "Aber so richtig Alter, ich brauch kurz einen Moment zum Runterkommen"
        "Schöner Tag heute.":
            "Hä?"
            menu:
                "Dich wiederholen":
                   maffay "Alter, du musst doch genauso high sein, wenn du unsere Situation momentan schön findest"
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
                        "Murrend gibt sie dir 2 Cryptobucks"
            "Nein, leider nicht":
                maffay "Schade"
        
            

        
    

