'''
title: Player class
author: Sean Jin
date-created: 2023-11-28
'''

from dice import Dice
class Player:

    # Constructor
    def __init__(self):
        """
        Player class in the program
        :param NAME: str
        :param HAND: list -> int
        """
        self.__NAME = input("What is your name? ")
        self.__UNFOUNDDIE = [Dice(6).getDiceValue(), Dice(6).getDiceValue(), Dice(6).getDiceValue(), Dice(6).getDiceValue(), Dice(6).getDiceValue()]
        self.__FOUNDDIE = []
        self.__SCORE = 0

    # MODIFIER method
    def rollDice(self):
        """
        Rolls the dice in the hand
        :return: none
        """
        for die in self.__UNFOUNDDIE:
            die.rollDie()
    def addScore(self, GAINS):
        """
        Adds score to the Player
        :return: none
        """
        self.__SCORE = self.__SCORE + GAINS

    def checkFoundDie(self):
        """
        Checks first if ship is found, then captain, then crew
        :return: none
        """
        SORTED_LIST = []

    # ACCESSOR method
    def getHand(self):
        """
        prints the hand that the user has
        :return: list
        """
        DISPLAY_HAND = []
        for i in range(len(self.__UNFOUNDDIE)):
            DISPLAY_HAND.append(self.__UNFOUNDDIE[i].getDiceValue())
        return DISPLAY_HAND

    def getScore(self):
        """
        prints the score
        :return: int
        """
        return self.__SCORE

    def getName(self):
        """
        Gets the name of the player
        :return: str
        """
        return self.__NAME


if __name__ == "__main__":
    PLAYER = Player()
    PLAYER.rollDice()
    PLAYER.checkFoundDie()



