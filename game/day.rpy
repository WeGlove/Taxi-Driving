label day:
    # 20CRP pro driver
    if current_day == 0:
        $passengers = passengers_day_1
    else:
        $passengers = passengers_day_2
    label gameloop:
        
        if len(passengers) == 0:
            jump out
        $ current_passenger = renpy.random.choice(passengers)
        $ current_passenger_stats = {"id": current_passenger, "paid": base_fare, "status": {}}
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
            if current_passenger_stats["status"]["storytime"] and len(passengers) > 0:
                $ passengers.remove(renpy.random.choice(passengers))
        elif current_passenger == "clown":
            call clown from _call_clown
        elif current_passenger == "dance":
            call dance from _call_dance
        elif current_passenger == "bobby":
            call bobby from _call_bobby
        elif current_passenger == "bfj":
            call bfj from _call_bfj
        elif current_passenger == "test":
            "You found the elusive test character. How did you get here?"
        "Du hast [current_passenger_stats[paid]] CRP verdient!"
        $ money += current_passenger_stats["paid"]
        jump gameloop
    label out:
    
    $neg_money = abs(money)
    if money >= 0:
        you "Glückwunsch! Du hast heute [money] CRP verdient!"
    else:
        you "Glückwunsch! Du hast heute [neg_money] CRP verloren!"
    
    call shop from _call_shop
    
    call news from _call_news
    
    return 