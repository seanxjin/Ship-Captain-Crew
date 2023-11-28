'''
title: Dice element class
author: Sean Jin
date-created: 2023-11-28
'''

from random import randint


class Dice:
    """
    Creates a class of dice for the game Captain ship crew. 1 to 6
    """

    # Constructor
    def __init__(self, SIDES):
        self.__SIDES = SIDES
        self.__VALUE = 1

    # MODIFIER Methods
    def rollDie(self):
        """
        Updating the die with a new number
        :return: none
        """
        self.__VALUE = randint(1, self.__SIDES)
    # ACCESSOR Methods
    def getDiceValue(self):
        """
        Returns the value of the dice
        :return: int
        """
        return self.__VALUE

if __name__ == "__main__":
    DICE = Dice(27)
    for i in range(10):
        DICE.rollDie()
        print(DICE.getDiceValue())