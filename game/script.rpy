# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("Du")


# The game starts here.

label start:
    $base_fare = 20 # The base fare that a taxi rider will pay.
    $money = 0 # Money is the variable that shows how much the player currently has.
    $passengers_day_1 = ["baby", "mime", "maffay", "gameshow", "zeuge", "captain", "clown", "dance", "bobby", "bfj"] # Passengers day 1

    $passengers_day_2 = ["fail_invent", "hero",  "happy_man"] # Passengers day 2

    $passenger_stats = {} # The list of passengers that rode in the players taxi. dict where {<id of rider>: {"paid":x, "status":{char specific}}}
    
    $upgrades = {"staubsauger": False, "zeitungen": False} # The dict of items available in the shop
    $number_of_days = 2 # The number of days (levels) in the game
    $current_day = 0 # The current day of the game

    you "Du bist ein Taxifahrer."
    
    play music "audio/driving.wav" loop
    show taxi_inner
    
    label day_loop:
        call day from _call_day
        $current_day += 1
        if current_day < number_of_days:
            jump day_loop
   
    "That's all for the game so far. Come back later for more!"

    # This ends the game.

    return

