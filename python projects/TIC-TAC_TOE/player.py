import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or 0
        self.letter = letter

    #we want then players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

 