import random
from passenger import Passenger

class Game:
    
    base_fare = 20
    number_of_days = 2
    friendliness = 0
    acquired_images = []
    favorite_passenger = ""

    
    def __init__(self):
        self.money = 0 # The current amount of money the player has
        
        self.current_day = 0 # The current day of the game. Starts at zero
        self.current_passenger = None # The passenger currently riding the taxi.
        self.future_passengers_of_today = [] # Passengers that are going to drive the taxi today.
        self.past_passengers_of_today = [] # Passengers that have been in the taxi today.
        
        self.default_function = lambda game: True
        self.all_passengers = [Passenger(name, "tier_1", self.default_function) for name in ["baby", "mime", "maffay", "gameshow", "zeuge", "captain", "clown", "dance", "bobby", "bfj"]] +\
                              [Passenger(name, "tier_2", self.default_function) for name in ["fail_invent", "hero",  "happy_man"]] +\
                              [Passenger(name, "esoteric", self.default_function) for name in ["test"]]
        
        self.pools = {}
        
        
        """Shop Items"""
        self.item_list = ["Staubsauger", "Bilderrahmen",  "Crypto Mining", "Zeitungen", "Putzlappen"]
        self.upgrades = {}
        self.haggling = {}
        self.price = {}
        self.options = {}
        for item in self.item_list:
            self.upgrades[item] =  False
            self.haggling[item] = 0
            self.price[item] = 2*20
            self.options[item] = [False, False, False, False, False]
            
    def get_passenger(self, name):
        """Returns a passenger of a given ID"""
        for passenger in self.all_passengers:
            if passenger.call_label == name:
                return passenger
        return None #TODO throw exception here!
    
    def refill_pools(self):
        return{
            "tier_1": [passenger for passenger in self.all_passengers if passenger.pool == "tier_1" if not passenger.has_driven and passenger.conditional(self)],
            "tier_2": [passenger for passenger in self.all_passengers if passenger.pool == "tier_2" if not passenger.has_driven and passenger.conditional(self)],
            "esoteric": [passenger for passenger in self.all_passengers if passenger.pool == "esoteric" if not passenger.has_driven and passenger.conditional(self)]
        } # The pools of passengers from which to build passenger lists. Constraint ein Character is in höchstens einem Pool
        
    
    def _get_passengers(self):
        """
            Creates a list of passengers for the current day.
        """
        if self.current_day == 0:
            return self.draw_from_pool(7, self.pools["tier_1"]) + self.maybe_draw_from_pool(1, self.pools["esoteric"], 0.01)
        elif self.current_day == 1:
            return self.draw_from_pool(3, self.pools["tier_1"]) + self.draw_from_pool(3, self.pools["tier_2"])
        else:
            return []
    
    def draw_from_pool(self, amount, pool):
        """Draws an amount of elements from the given pool without giving elements back"""
        pool_copy = list(pool) # Make a copy of the pool
        passengers = []
        for _ in range(amount): # Draw without returning
            passenger = random.choice(pool_copy)
            pool_copy.remove(passenger)
            passengers.append(passenger)
        return passengers
    
    def maybe_draw_from_pool(self, amount, pool, probability):
        pool_copy = list(pool) # Make a copy of the pool
        passengers = []
        for _ in range(amount): # Draw without returning
            if random.random() < probability:
                passenger = random.choice(pool_copy)
                pool_copy.remove(passenger)
                passengers.append(passenger)
        return passengers
    
    
    def skip_a_character(amount=1):
        """
            Skips characters that would otherwise have ridden the taxi
        """
        for i in range(amount):
            if len(self.future_passengers_of_today) > 0:
                self.current_passenger = random.choice(self.future_passengers_of_today)
                self.future_passengers_of_today.remove(self.current_passenger)
            else:
                return
            
    def start_day(self):
        """
            Set up for the current day.
        """
        self.pools = self.refill_pools()
        self.future_passengers_of_today = self._get_passengers()
        
    def next_passenger(self):
        """
            Returns the next passenger and handles not having the last passenger again. 
        """
        if self.current_passenger is not None:
            self.current_passenger.has_driven = True
        self.current_passenger = random.choice(self.future_passengers_of_today)
        self.future_passengers_of_today.remove(self.current_passenger)
        self.past_passengers_of_today.append(self.current_passenger)
        return self.current_passenger
    
    def is_day_finished(self):
        """
            Whether the day is finished after a passenger has ridden in the car.
        """
        return len(self.future_passengers_of_today) == 0
    
    
    def finish_day(self):
        """
            End the current day.
        """
        for passenger in self.past_passengers_of_today:
            self.pools[passenger.pool].remove(passenger)
        self.current_day += 1
    
    def get_acquired_upgrades(self):
        return[key for key in self.upgrades.keys() if self.upgrades[key]]

        