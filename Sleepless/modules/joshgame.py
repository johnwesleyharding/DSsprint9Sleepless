# 1) make a doc string
"""
Classes to represent games
"""

# 2) any imports you need
from random import random

# 3) create a class
class Game:
    """General representation of an abstract game"""
    
    # 4) class attributes
    fun_level = 5
    
    # 5) constructor
    def __init__(self, player1="Stefano", player2="Rudy"):
        self.rounds = 2
        self.steps = 5
        self.player1 = player1
        self.player2 = player2

    def print_players(self):
        """ Print game players"""
        print('{} is playing {}'.format(self.player1, self.player2))

    def add_round(self):
        """Increment rounds by 1"""
        self.rounds += 1

    def winner(self):
        """pseudorandomly pick a winner"""
        return self.player1 if random() > 0.5 else self.player2


class Tic(Game):
    """
    Tictactoe subclass of game
    """

    def __init__(self, player1='Anika', player2='Hira'):
        super().__init__(player1, player2)
        self.rounds = 3

    def print_players(self):
        print('{} is playing TIC TAC TOE with {}'.format(self.player1,
                                                         self.player2))