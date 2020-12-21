from move import Move
from board import Board

class Game:

    gameover = False

    def __init__(self):
        self.board = Board()

    def display(self):
        self.board.display()

    # A function to trigger the move of a piece
    def move(self):

        # Asking the user for input
        x = input("Enter a move: ")

        # Checking if the user wants to end the game
        if x == "QUIT":
            self.gameover = True
            return None

        # Creating a move object
        move = Move(x)

        # Checking if the move is valid and asking
        # for a new move if not
        while not move.is_valid():
            x = input("Invalid move, please enter a new move: ")
            move = Move(x)

        # Remove the piece from the inital square
        # and move it to a new one
        self.board.move(move)

