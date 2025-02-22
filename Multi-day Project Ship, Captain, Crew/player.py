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
        Player class in the program, attributes
        :param NAME: str
        :param HAND: list -> int
        """
        self.__NAME = input("Name: ") # INPUT
        self.__UNFOUNDDIE = [Dice(6), Dice(6), Dice(6), Dice(6), Dice(6)]
        self.__FOUNDDIE = []
        self.__GOLD = 0
        self.__ROLLS = 3
        self.__SABOTAGE = False
        self.__EXTRAROLLS = False
        self.__JACKPOT = False
        self.__CONSOLATIONGOLD = False
    # MODIFIER method PROCESSING
    def rollDice(self):
        """
        Rolls the dice in the hand
        :return: none
        """
        for die in self.__UNFOUNDDIE:
            die.rollDie()
        self.__ROLLS = self.__ROLLS - 1
    def addGold(self, GAINS):
        """
        Adds score to the Player
        :return: none
        """
        self.__GOLD = self.__GOLD + GAINS
    def checkFoundDie(self):
        """
        Checks first if ship is found, then captain, then crew
        :return: none
        """
        if len(self.__FOUNDDIE) == 0: # This function may be called upon more than once, so we must first find out the length of the found dice's list, so we know what other numbers to find.
            CONFIGURED_ARRAY = [] # Creates an empty array to convert the objects to processable numbers
            for i in range(len(self.__UNFOUNDDIE)):
                CONFIGURED_ARRAY.append(self.__UNFOUNDDIE[i].getDiceValue())
            for j in range(6,3,-1):
                try:
                    LOCATION = CONFIGURED_ARRAY.index(j) # Uses the index function to find first 6, and then 5, and then 4
                    self.__FOUNDDIE.append(self.__UNFOUNDDIE.pop(LOCATION))
                    CONFIGURED_ARRAY.pop(LOCATION)
                except ValueError:
                    break
        elif len(self.__FOUNDDIE) == 1:
            CONFIGURED_ARRAY = []
            for i in range(len(self.__UNFOUNDDIE)):
                CONFIGURED_ARRAY.append(self.__UNFOUNDDIE[i].getDiceValue())
            for i in range(5, 3, -1):
                try:
                    LOCATION = CONFIGURED_ARRAY.index(i)
                    self.__FOUNDDIE.append(self.__UNFOUNDDIE.pop(LOCATION))
                    CONFIGURED_ARRAY.pop(LOCATION)
                except ValueError:
                    break
        elif len(self.__FOUNDDIE) == 2:
            CONFIGURED_ARRAY = []
            for i in range(len(self.__UNFOUNDDIE)):
                CONFIGURED_ARRAY.append(self.__UNFOUNDDIE[i].getDiceValue())
            for i in range(4, 3, -1):
                try:
                    LOCATION = CONFIGURED_ARRAY.index(i)
                    self.__FOUNDDIE.append(self.__UNFOUNDDIE.pop(LOCATION))
                    CONFIGURED_ARRAY.pop(LOCATION)
                except ValueError:
                    break
    def resetHand(self):
        """
        Resets the hand of the player after the round is over. Appends the found die back into the un-found die array. It also resets all the power-ups that the player has.
        :return: none
        """
        for i in range(len(self.__FOUNDDIE)):
            RESET = self.__FOUNDDIE.pop()
            self.__UNFOUNDDIE.append(RESET)
    def resetPowerUps(self):
        """
        Resets the powerups that each player has. This happens after the round ends, and before the shopping phase. Power-up would reset and the player would enter the shopping phase, thus buying a new power-up for the next round.
        :return: none
        """
        self.__SABOTAGE = False
        self.__EXTRAROLLS = False
        self.__JACKPOT = False
        self.__CONSOLATIONGOLD = False
    def askBuy(self):
        """
        Asks the user if they want to buy any powerups.
        :return: none
        """
        # INPUT
        print("""There is a tide in the affairs of men, Which taken at the flood, leads on to fortune....
        Welcome to the Power Up Shop! Pick your Choice! Input an integer! ALL POWER-UPs ONLY LAST FOR ONE ROUND!
        1. 6$ Jackpot: Doubles the amount of the gold at the end of rolls. If the requirements are not met 
        (ship, captain, crew), the powerup will be null.
        2. 8$ Extra Re-roll: Gives you 4 rolls instead of 3 rolls, counters Sabotage ability!
        3. 5$ Sabotage: Give your opponent one less roll!
        4. 1$ Consolation Gold: If you do not get any gold at the end of the round, receive 4 gold
        as compensation
        5.. Leave ...
        """)
        CHOICE = input("> ")
        if CHOICE.isnumeric():
            CHOICE = int(CHOICE)
        else:
            print("""Please enter a proper integer!""")
            return self.askBuy()
        if CHOICE > 0 and CHOICE < 6:
            pass
        else:
            print("Please input a integer within the given ranges!")
            return self.askBuy()
        # PROCESSING
        if CHOICE == 1:
            if self.__GOLD >= 6:
                self.__GOLD -= 6
                self.__JACKPOT = True
                print("You have bought Jackpot")
            else:
                print("You do no have enough gold. Go find more gold.")
        elif CHOICE == 2:
            if self.__GOLD >= 8:
                self.__GOLD -= 8
                self.__EXTRAROLLS = True
                print("You have bought Extra rolls")
            else:
                print("You do no have enough gold. Go find more gold.")
        elif CHOICE == 3:
            if self.__GOLD >= 5:
                self.__GOLD -= 5
                self.__SABOTAGE = True
                print("You have bought Sabotage")
            else:
                print("You do no have enough gold. Go find more gold.")
        elif CHOICE == 4:
            if self.__GOLD >= 1:
                self.__GOLD -= 1
                self.__CONSOLATIONGOLD = True
                print("You have bought consolation gold")
            else:
                print("You do no have enough gold. Go find more gold.")
        else:
            pass
    def resetRolls(self, SABOTAGE):
        """
        Resets the rolls of the player. If the opposing player has the power-up
        "Sabotage", then the player gets only 2 rolls, if the player
        :return: none
        """
        if self.getExtraRolls():
            self.__ROLLS = 4
        elif SABOTAGE:
            self.__ROLLS = 2
        else:
            self.__ROLLS = 3


    # ACCESSOR method OUTPUTS
    def getNumberRolls(self):
        """
        gets the number of rolls that this individual player has
        :return: int
        """
        return self.__ROLLS
    def getUnfoundDie(self):
        """
        prints the hand that the user has
        :return: list
        """
        DISPLAY_HAND = []
        for i in range(len(self.__UNFOUNDDIE)):
            DISPLAY_HAND.append(self.__UNFOUNDDIE[i].getDiceValue())
        return DISPLAY_HAND
    def getGold(self):
        """
        prints the score
        :return: int
        """
        return self.__GOLD
    def getFoundDie(self):
        """
        prints the hand that the user has
        :return: list
        """
        DISPLAY_HAND = []
        for i in range(len(self.__FOUNDDIE)):
            DISPLAY_HAND.append(self.__FOUNDDIE[i].getDiceValue())
        return DISPLAY_HAND

    def getName(self):
        """
        Gets the name of the player
        :return: str
        """
        return self.__NAME
    def getJackpot(self):
        """
        returns bool Jackpot
        :return: bool
        """
        return self.__JACKPOT
    def getExtraRolls(self):
        """
        Returns bool extra rolls
        :return: bool
        """
        return self.__EXTRAROLLS
    def getSabotage(self):
        """
        Returns bool sabotage
        :return: bool
        """
        return self.__SABOTAGE
    def getConsolationGold(self):
        """
        Returns bool consolation gold
        :return: bool
        """
        return self.__CONSOLATIONGOLD
    def askKeepGold(self):
        """
        Asks the player if they want to keep the gold or reroll it
        :return: bool
        """
        print(f"You currently found {sum(self.getUnfoundDie())} gold pieces! Keep Gold?")
        CHOICE = input("> (Y/n) ")
        if CHOICE == "Y" or CHOICE == "n" or CHOICE == "y" or CHOICE == "N":
            if CHOICE == "Y" or CHOICE == "y":
                return True
            else:
                return False
        else:
            print("Please enter a valid letter. (Y/N)")
            return self.askKeepGold()


if __name__ == "__main__":
    PLAYER = Player()
    PLAYER.rollDice()
    print(PLAYER.askKeepGold())



