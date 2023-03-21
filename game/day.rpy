﻿label day:
    $ game.start_day()
    "Du beginnst deine Schicht in deinem Taxi."    
    
    show taxi_inner
        
    label gameloop:       
        if game.is_day_finished():
            jump out
        $ current_passenger = game.next_passenger()
        
        show taxi_inner
        with Dissolve(0.5)
        call expression game.current_passenger.call_label from _call_expression
        hide taxi_inner
        with Dissolve(0.5)
            
        
        $ acquired_money = game.pay_passenger()
        "Du hast [acquired_money] CRP verdient!"
        if game.upgrades["Crypto Mining"]:
            $ game.money += game.base_fare/10 # TODO this should be a function of Game
            # TODO This is slightly wrong. But I don't know how to correctly show basefare/10 here.
            "Du erhälst extra Einnahmen in Höhe von [game.base_fare] CRP durch Crypto Mining!"
            "{i}\U+266A Crypto Mining!\U+266A{/i}"
            "{i}\U+266A Machen auch Sie ihr Strom zu Geld!\U+266A {/i}"

        jump gameloop
    label out:
    
    $ neg_money = abs(game.money)
    if game.money >= 0:
        "Glückwunsch! Du hast heute [game.money] CRP verdient!" # TODO There should be a get_monex function
    else:
        "Glückwunsch? Du hast heute [neg_money] CRP verloren!"
        
    if game.money < 0:
        $ debt_collector = game.get_debt_collector()
        call expression debt_collector.call_label from _call_debts
        $ game.finish_debt_collector()
    
    hide taxi_inner
    call shop from _call_shop
    
    call news from _call_news
    
    $game.finish_day()
    
    return 