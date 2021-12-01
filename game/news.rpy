# The logic for the news displayed after each day.

define news_anchor = Character("Günther Gotschalk")

label news:
    show news
    "Nach deiner Schicht setzt du dich gemütlich vor deinen Fernseher und schaust die Nachrichten."
    
    news_anchor "Guten Abend meine Damen und Herren {b} zu den {i}wild{/i} *Löwengebrüll* action news!{/b}"
    news_anchor "Mit ihrem Narichtensprecher Günther Gotschalk"
    news_anchor "Und heute:"
    
    if "bfj" in game.past_passengers_of_today:
        if game.get_passenger("bfj"]).status["beaten"]:
            news_anchor "Ein gebrächlicher alter Mann wurde heute von einem Taxifahrer angegriffen."
            news_anchor "Wie wir hier von Außenaufnahmen sehen können, hält der Mann eigentlich nur ein kleines Gespräch mit dem Fahrer."
            news_anchor "Der Fahrer wiederum begint grundlos auf den Mann einzuprügeln."
            news_anchor "Glücklicherweise, kann sich der Mann aber gut verteidigen oder wie er selbst sagt:"
            bfj "Ich habe damals in während meiner Zeit im Studiun viel Kampfsport gemacht wissen Sie."
            bfj "Aber die jungen Leute sind ja auch alle viel zu faul für so was heute."
            
    if game.current_day == 0:
        "Nachrichten des Tages 0"
    
    news_anchor "Das war's für heute wieder mit den {b} {i}wild{/i} *Löwengebrüll* action news mit ihrem Nachrichtensprecher Günther Gotschalk."
    
    
    hide news
    return