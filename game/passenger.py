class Passenger:

    def __init__(self, call_label, pool, conditional= None):
        """
            Conditional must be of form {some_passenger: {has_driven: bool, paying:int, status:some_dict}, ...}
        """
        self.call_label = call_label # The label renpy should call to get to the chars script
        self.paying = 0 # How much the character is paying to the driver.
        self.has_driven = False
        self.pool = pool
        self.status = {} # Misc status effects special to the character
        if conditional is None:
            conditional = {}
        self.conditional = conditional # The condition on which a char should be added to its pool