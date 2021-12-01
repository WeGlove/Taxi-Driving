class Passenger:

    def __init__(self, call_label, pool):
        self.call_label = call_label # The label renpy should call to get to the chars script
        self.paying = 0 # How much the character is paying to the driver.
        self.has_driven = False
        self.pool = pool
        self.status = {} # Misc status effects special to the character