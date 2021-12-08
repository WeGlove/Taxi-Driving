label day:
    $ game.start_day()
    "Du beginnst deine Schicht in deinem Taxi."    
    
    show taxi_inner
        
    label gameloop:       
        if game.is_day_finished():
            jump out
        $ current_passenger = game.next_passenger()
        
        show taxi_inner
        with Dissolve(0.5)
        call expression game.current_passenger.call_label # TODO Captain removed passenger nicht mehr.
        hide taxi_inner
        with Dissolve(0.5)
            
        "Du hast [game.current_passenger.paying] CRP verdient!"
        $ game.pay_passenger()
        if game.upgrades["Crypto Mining"]:
            $game.money += game.base_fare/10
            # TODO This is slightly wrong. But I don't know how to correctly show basefare/10 here.
            "Du erhälst extra Einnahmen in Höhe von [game.base_fare] CRP durch crypto Mining!"
            "{i}\U+266A Crypto Mining!\U+266A{/i}"
            "{i}\U+266A Machen auch Sie ihr Strom zu Geld!\U+266A {/i}"
        
        
        jump gameloop
    label out:
    
    $neg_money = abs(game.money)
    if game.money >= 0:
        "Glückwunsch! Du hast heute [game.money] CRP verdient!"
    else:
        "Glückwunsch? Du hast heute [neg_money] CRP verloren!"
    
    hide taxi_inner
    call shop from _call_shop
    
    call news from _call_news
    
    $game.finish_day()
    
    return 