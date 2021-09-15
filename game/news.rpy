# The logic for the news displayed after each day.

# The news already shown to the player
$played_news = []

label news:
    "Nach deiner Schicht setzt du dich gemütlich vor deinen Fernseher und schaust die Nachrichten."
    
    if "bahnfahrerjesus" in passengers_of_the_day:
        if passenger_stats["bahnfahrerjesus"]["special"]["beaten"]:
            "Ein Taxifahrer wurde heute von einem verwirrten alten Mann angegriffen."
    if current_day == 0:
        "Nachrichten des Tages 0"
    return