import random
from passenger import Passenger

class Game:
    
    base_fare = 20
    number_of_days = 2
    
    def __init__(self):
        self.money = 0 # The current amount of money the player has
        
        self.current_day = 0 # The current day of the game. Starts at zero
        self.current_passenger = None # The passenger currently riding the taxi.
        self.passengers_of_the_day = [] # Passengers that have already driven with the taxi.
        
        self.pools = { 
        "tier_1": [Passenger(name) for name in ["baby", "mime", "maffay", "gameshow", "zeuge", "captain", "clown", "dance", "bobby", "bfj"]],
        "tier_2": [Passenger(name) for name in ["fail_invent", "hero",  "happy_man"]]
        } # The pools of passenges from which to build passenger lists.
        self.upgrades = {"staubsauger": False, "zeitungen": False} # The dict of items available in the shop
    
    def get_passengers(self):
        if self.current_day == 0:
            return self.pools["tier_1"]
        elif self.current_day == 1:
            return self.pools["tier_2"]
        else:
            return []
            
    def start_day(self):
        self.passengers_of_the_day = self.get_passengers()
    
    def finish_day(self):
        self.current_day += 1
    
    def is_day_finished(self):
        return len(self.passengers_of_the_day) == 0
    
    def next_passenger(self):
        self.current_passenger = random.choice(self.passengers_of_the_day)
        self.current_passenger_stats = {"paid": self.base_fare, "status": {}}
        self.passengers_of_the_day.remove(self.current_passenger)
        return self.current_passenger
        