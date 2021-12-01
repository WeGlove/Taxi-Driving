define shopkeep = Character("Robby")

label shop:
    show shop
    shopkeep "Wilkommen zu Robbys robustem Ramsch, oder auch nicht. Mir eigentlich egal."
    menu:
        "Dir auch nen schönen Tag":
            shopkeep "Bist du hier warst, war es einer."
            you "Naja... Was gibt's denn heute?"
        "Was ist denn das für ein Service?":
            shopkeep "Service den einer wie du verdient hat."
            you "Was soll das denn jetzt heißen?"
            shopkeep "Kaufst du jetzt was oder gehst du?"
            menu:
                "Herumstöbern":
                    jump buy_loop
                "Gehen":
                    shopkeep "Bis morgen."
                    return
        "Haben wir ein Problem?":
            shopkeep "Ich nein, du ja, aber über dein Leben müssen wir uns ja jetzt nicht unterhalten."
            menu:
                "Ich zeig dir gleich wer Probleme in seinem Leben hat": # TODO Hier bahnfahrer jesus reference
                    shopkeep "Oh bitte."
                    you "..."
                    shopkeep "..., du hast das ernst gemeint?"
                    return
                "Schon gut, zeig mir einfach was du hast.":
                    shopkeep "So lob ich mir das."
        "Was auch immer...":
            jump buy_loop
        "...":
            jump buy_loop
    label buy_loop:
        menu:
            "Staubsauger" if not game.upgrades["Staubsauger"]:
                call shop_staubsauger from _shop_staubsauger
            "Bilderrahmen" if not game.upgrades["Bilderrahmen"]:
                call shop_bilderrahmen from _shop_bilderrahmen
            "Crypto Mining" if not game.upgrades["Crypto Mining"]:
                call shop_crypto from _shop_crypto
            "Zeitungen" if not game.upgrades["Zeitungen"]:
                call shop_zeitungen from _shop_zeitungen
            "Putzlappen" if not game.upgrades["Putzlappen"]:
                call shop_putzlappen from _shop_putzlappen
            "Den Laden verlassen.":
                hide shop
                return
        jump buy_loop