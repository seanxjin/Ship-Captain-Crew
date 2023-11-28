'''
title: Player class
author: Sean Jin
date-created: 2023-11-28
'''

import dice
class Player:

    # Constructor
    def __init__(self, NAME, HAND):
        """
        Player class in the program
        :param NAME: str
        :param HAND: list -> int
        """
        self.__NAME = NAME
        self.__HAND = HAND

    # MODIFIER method

    # ACCESSOR method
    def getHand(self):
        """
        Gets the hand of the dice
        :return: list
        """
        return self.__HAND


