import random
import json
from passenger import Passenger

class Game:
    """
    The general controlling class for the game.
    """
    
    base_fare = 20
    number_of_days = 2
    friendliness = 0
    acquired_images = []
    favorite_passenger = ""
    newspaper_monies = 0.25 * base_fare

    
    def __init__(self):
        self.money = 0 # The current amount of money the player has
        self.current_day = 0 # The current day of the game. Starts at zero
        self.current_passenger = None # The passenger currently riding the taxi.
        self.future_passengers_of_today = [] # Passengers that are going to drive the taxi today.
        self.past_passengers_of_today = [] # Passengers that have been in the taxi today.
        self.debt_collector = None # The current debt collector
        self.number_of_debt_infractions = 0
        
        self.all_passengers = [Passenger(name, "tier_0") for name in ["passenger_failed_inventor", "hero",  "passenger_happy_man", "introvert"]] +\
                              [Passenger(name, "tier_1") for name in ["baby", "mime", "maffay", "gameshow", "zeuge", "captain", "clown", "dance", "bobby", "bfj"]] +\
                              [Passenger(name, "tier_2") for name in ["introvert", "passenger_faustings"]] +\
                              [Passenger(name, "esoteric") for name in ["test", "passenger_fall"]] +\
                              [Passenger(name, "debts") for name in ["passenger_debts"]]

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
            self.price[item] = 2*self.base_fare
            self.options[item] = [False, False, False, False, False]

    def get_current_day(self):
        """
        Returns the current day
        """
        return self.current_day

    def get_number_of_days(self):
        """
        Returns the total number of day
        """
        return self.number_of_days

    def get_money(self):
        """
        Returns the current amount of money the player has.
        """
        return self.money

    def add_money(self, amount):
        """
        Adds money to the players total
        """
        self.money += amount

    def get_base_fare(self):
        """
        Returns the base amount of money a passenger should pay when riding the Taxi
        """
        return self.base_fare

    def get_fav_passenger(self):
        """
        Returns the favorite passenger of the player
        """
        return self.favorite_passenger
            
    def get_passenger(self, name):
        """Returns a passenger of a given ID"""
        for passenger in self.all_passengers:
            if passenger.call_label == name:
                return passenger
        return None #TODO throw exception here!
    
    def refill_pools(self):
        return{
            "tier_0": [passenger for passenger in self.all_passengers if passenger.pool == "tier_0" if not passenger.has_driven and self.passenger_fulfills_condition(passenger)],
            "tier_1": [passenger for passenger in self.all_passengers if passenger.pool == "tier_1" if not passenger.has_driven and self.passenger_fulfills_condition(passenger)],
            "tier_2": [passenger for passenger in self.all_passengers if passenger.pool == "tier_2" if not passenger.has_driven and self.passenger_fulfills_condition(passenger)],
            "esoteric": [passenger for passenger in self.all_passengers if passenger.pool == "esoteric" if not passenger.has_driven and self.passenger_fulfills_condition(passenger)],
        } # The pools of passengers from which to build passenger lists. Constraint: ein Character is in höchstens einem Pool
    
    def get_debt_pool(self):
        return [passenger for passenger in self.all_passengers if passenger.pool == "debts" if not passenger.has_driven and self.passenger_fulfills_condition(passenger)]
    
    def passenger_fulfills_condition(self, passenger):
        for cond_passenger_name, cond_status in passenger.conditional.items():
            cond_passenger = self.get_passenger(cond_passenger_name)
            if "has_driven" in cond_status.keys():
                if cond_passenger.has_driven != cond_status["has_driven"]:
                    return False
            if "paying" in cond_status.keys():
                if cond_passenger.paying != cond_status["paying"]:
                    return False
            if "status" in cond_status.keys():
                for status_key, status_value in cond_status.items():
                    if cond_passenger.status[status_key] != status_value:
                        return False
            if "money" in cond_status.keys():
                if not (cond_status["money"][0] <= self.money <= cond_status["money"][1]):
                    return False
            if "infractions" in cond_status.keys():
                if not (cond_status["infractions"][0] <= self.number_of_debt_infractions <= cond_status["infractions"][1]):
                    return False
        return True
    
    def _get_passengers(self):
        """
            Creates a list of passengers for the current day.
        """
        if self.current_day == 0:
            return self.draw_from_pool(7, self.pools["tier_1"]) + self.maybe_draw_from_pool(1, self.pools["esoteric"], 0.01)
        elif self.current_day == 1:
            return self.draw_from_pool(3, self.pools["tier_1"]) + self.draw_from_pool(2, self.pools["tier_0"]) + self.draw_from_pool(1, self.pools["tier_2"]) + self.maybe_draw_from_pool(1, self.pools["esoteric"], 0.01)
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
    
    def skip_a_character(self, amount=1):
        """
            Skips characters that would otherwise have ridden the taxi
        """
        for i in range(amount):
            if len(self.future_passengers_of_today) > 0:
                self.future_passengers_of_today.remove(random.choice(self.future_passengers_of_today))
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
        self.past_passengers_of_today = []
        self.current_day += 1
        
    def get_debt_collector(self):
        self.debt_collector = self.draw_from_pool(1, self.get_debt_pool())[0]
        return self.debt_collector
        
    def finish_debt_collector(self):
        self.past_passengers_of_today.append(self.debt_collector)
        self.debt_collector.has_driven = True
    
    def get_acquired_upgrades(self):
        return[key for key in self.upgrades.keys() if self.upgrades[key]]
    
    def pay_passenger(self):
        acquired_money = 0
        acquired_money += self.current_passenger.paying
        acquired_money += self.friendliness
        if self.current_passenger.call_label == self.favorite_passenger:
            acquired_money = acquired_money * 2
        self.money += acquired_money
        return acquired_money
    
    def force_character(self, name):
        self.future_passengers_of_today = [self.get_passenger(name)] + self.future_passengers_of_today