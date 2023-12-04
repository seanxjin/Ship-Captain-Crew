'''
title: Game class of Ship Captain Crew
author: Sean Jin
date-created: 2023-12-03
'''

from player import Player
from dice import Dice

class Game:

    # Constructor
    def __init__(self):
        self.__Player1 = Player()
        self.__Player2 = Player()

    # RUN THE PROGRAM
    def Run(self):
        print("""Welcome to Ship Captain Crew, a game of chance and money!""")
        while True:
            print(f"{self.__Player1.getName()}'s turn")
            for i in range(self.__Player1.getNumberRolls()):
                self.__Player1.rollDice()
                self.__Player1.checkFoundDie()
                self.__Player1.getFoundDie()

if __name__ == "__main__":
    GAME = Game()
    GAME.Run()