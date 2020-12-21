from move import Move

class Board:
    def __init__(self):

        # Reading the chess board template
        # And coercing it to a list
        # To allow changing characters
        with open("board.txt") as board:
            template = board.read()

        self.template = list(template)
        
        # Reading the correspondence between algebraic
        # positions and positions in the board list
        with open("algebraic_positions.txt") as algebra:
            alg = algebra.readlines()

        alg = [i.rstrip() for i in alg]
        alg = [i.split(" ") for i in alg]
        alg = {i[0] : int(i[1]) for i in alg}
        self.algebra = alg

        # Reading the correspondence between pieces and
        # their unicode string for display
        with open("pieces_unicode.txt") as pieces_unicode:
            ucodes = pieces_unicode.readlines()

        ucodes = [i.rstrip() for i in ucodes]
        ucodes = [i.split(" ") for i in ucodes]
        ucodes = {i[0] : i[1] for i in ucodes}
        self.unicode = ucodes

        # Creating a state variable which is a dictionary mapping
        # all algebraic coordinates to the piece located in that
        # square. We base it on a copy of self.algebra
        state = self.algebra.copy()

        # Initialize all values to " " (empty square)
        for i in state:
            state[i] = " "

        # Now we read the initial state of the board from file
        with open("initial_state.txt") as initial_state:
            initial = initial_state.readlines()

        initial = [i.rstrip() for i in initial]
        initial = [i.split(" ") for i in initial]
        initial = {i[0] : i[1] for i in initial}

        # We use those initial values to update the state variable
        for i in initial:
            state[i] = initial[i]
        
        self.state = state


    def display(self):
        for i in self.state:
            if self.state[i] != ' ':
                self.template[self.algebra[i]] = self.unicode[self.state[i]]
            else:
                self.template[self.algebra[i]] = ' '
        print("".join(self.template))

    def move(self, move):
        piece = self.state[move.start]
        self.state[move.start] = " "
        self.state[move.stop]  = piece

