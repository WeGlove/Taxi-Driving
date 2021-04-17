# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Du")


# The game starts here.

label start:
    $base_fare = 20 # The base fare that a taxi rider will pay.
    $money = 0 # Money is the variable that shows how much the player currently has.
    $passengers = ["baby", "mime", "maffay", "gameshow", "zeuge", "captain", "clown", "dance", "bobby", "bfj"]
    $passenger_stats = [{"id":1, "paid":1, "status":{}}] # The list of passengers that rode in the players taxi. List of dicts where {"id":sdsad, "paid":x, "status":{char specific}}

    you "Du bist ein Taxifahrer."
    
    # 20CRP pro driver
    label gameloop:
        if len(passengers) == 0:
            jump out
        $ current_passenger = renpy.random.choice(passengers)
        $ current_passenger_stats = {"id": current_passenger, "paid": 0, "status": {}}
        $ passengers.remove(current_passenger)
        if current_passenger == "baby":
            call baby from _call_baby
        elif current_passenger == "mime":
            call mime from _call_mime
        elif current_passenger == "maffay":
            call maffay from _call_maffay
        elif current_passenger == "gameshow":
            call gameshow from _call_gameshow
        elif current_passenger == "zeuge":
            call zeuge from _call_zeuge
        elif current_passenger == "captain":
            call captain from _call_captain
        elif current_passenger == "clown":
            call clown from _call_clown
        elif current_passenger == "dance":
            call dance from _call_dance
        elif current_passenger == "bobby":
            call bobby from _call_bobby
        elif current_passenger == "bfj":
            call bfj from _call_bfj
        "Du hast [current_passenger_stats[paid]] verdient!"
        $ money += current_passenger_stats["paid"]
        jump gameloop
    label out:
    
    you "Glückwunsch! Du hast heute [money] CRP verdient!"
   

    # This ends the game.

    return

