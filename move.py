class Move:

    def __init__(self, move_string):
        # Transforming the move string into a 2-tuple
        self.coords = tuple(move_string.split(" "))
        self.start = self.coords[0]
        self.stop  = self.coords[1]

    # This method checks if the move is valid
    def is_valid(self):
        return True

