label day:
    $ game.start_day()
    "Du beginnst deine Schicht in deinem Taxi."    
    
    show taxi_inner
        
    label gameloop:       
        if game.is_day_finished():
            jump out
        $ current_passenger = game.next_passenger()
        
        call expression game.current_passenger.call_label # TODO Captain removed passenger nicht mehr.
            
        "Du hast [game.current_passenger.paying] CRP verdient!"
        $ game.money += game.current_passenger.paying
        
        jump gameloop
    label out:
    
    $neg_money = abs(game.money)
    if game.money >= 0:
        you "Glückwunsch! Du hast heute [game.money] CRP verdient!"
    else:
        you "Glückwunsch! Du hast heute [neg_money] CRP verloren!"
    
    hide taxi_inner
    call shop from _call_shop
    
    call news from _call_news
    
    $game.finish_day()
    
    return 