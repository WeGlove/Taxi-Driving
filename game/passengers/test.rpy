define test = Character("Test")

label test:
    "Ein Test Character steigt in deinen Wagen"
    test "Hallo Welt"
    menu:
        "Ja":
            $current_passenger.paying += game.base_fare*3
        "Nein":
            $current_passenger.paying = 0
    "Der Test Character verlässt den Wagen."
    return

