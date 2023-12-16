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
        print("")
        while True:
            print(f"{self.__Player1.getName()}'s turn")
            ROLL_PLAYER1 = 0
            PLAYER1GO = 1
            while PLAYER1GO == 1: # Repeats the rolling function of player 1
                # PLAYER 1 IPO
                print("")
                ROLL_PLAYER1 += 1 # This is for user experiences, helps them keep track of which roll they are on
                print(f"Roll number {ROLL_PLAYER1}")
                # Processing
                self.__Player1.rollDice()
                self.__Player1.checkFoundDie()
                # Outputs
                for i in range(len(self.__Player1.getFoundDie())):
                    if self.__Player1.getFoundDie()[i] == 6:
                        print("Ship is found")
                    if self.__Player1.getFoundDie()[i] == 5:
                        print("Captain is found")
                    if self.__Player1.getFoundDie()[i] == 4:
                        print("Crew is found")
                # If the player has successfully found the necessary requirements
                if len(self.__Player1.getFoundDie()) == 3:
                    print(f"{self.__Player1.getName()} has gotten the ship, captain, and crew!")
                    while self.__Player1.getNumberRolls() > 0:
                        CHOICE = self.__Player1.askKeepGold()
                        if CHOICE:
                            if self.__Player1.getJackpot():
                                print("JACKPOT POWERUP!!!!!")
                                print(f"Nice, you keep {sum(self.__Player1.getUnfoundDie())*2} gold! Good Job! ")
                                self.__Player1.addGold(sum(self.__Player1.getUnfoundDie())*2)
                                PLAYER1GO = 0  # stops the loop of rolling for player 1 as the user decided to stop and keep his dice
                                break
                            else:
                                print(f"Nice, you keep {sum(self.__Player1.getUnfoundDie())} gold! Good Job! ")
                                self.__Player1.addGold(sum(self.__Player1.getUnfoundDie()))
                            PLAYER1GO = 0 # stops the loop of rolling for player 1 as the user decided to stop and keep his dice
                            break
                        else:
                            self.__Player1.rollDice()
                    else:
                        if self.__Player1.getJackpot():
                            print("JACKPOT POWERUP!!!!!")
                            print(f"Nice, you keep {sum(self.__Player1.getUnfoundDie()) * 2} gold! Good Job! ")
                            self.__Player1.addGold(sum(self.__Player1.getUnfoundDie()) * 2)
                            PLAYER1GO = 0
                        else:
                            print(f"Nice, you keep {sum(self.__Player1.getUnfoundDie())} gold! Good Job!")
                            self.__Player1.addGold(sum(self.__Player1.getUnfoundDie()))
                            PLAYER1GO = 0
                # If the player has not found the necessary requirements of the game
                else:
                    if self.__Player1.getNumberRolls() > 0:
                        pass
                    else:
                        print("No gold was found :(")
                        PLAYER1GO = 0
            print("Press any key to start player 2's turn")
            BUFFER = input("> ") # This just acts as a sort of stop or buffer to increase or improve the user experience
            # PLAYER 2 IPO
            ROLL_PLAYER2 = 0
            PLAYER2GO = 1
            print(f"{self.__Player2.getName()}'s turn")
            while PLAYER2GO == 1:
                # PLAYER 2 IPO
                print("")
                ROLL_PLAYER2 += 1  # This is for user experiences, helps them keep track of which roll they are on
                print(f"Roll number {ROLL_PLAYER2}")
                # Processing
                self.__Player2.rollDice()
                self.__Player2.checkFoundDie()
                # Outputs
                for i in range(len(self.__Player2.getFoundDie())):
                    if self.__Player2.getFoundDie()[i] == 6:
                        print("Ship is found")
                    if self.__Player2.getFoundDie()[i] == 5:
                        print("Captain is found")
                    if self.__Player2.getFoundDie()[i] == 4:
                        print("Crew is found")
                # If the player has successfully found the necessary requirements
                if len(self.__Player2.getFoundDie()) == 3:
                    print(f"{self.__Player2.getName()} has gotten the ship, captain, and crew!")
                    while self.__Player2.getNumberRolls() > 0:
                        CHOICE = self.__Player2.askKeepGold()
                        if CHOICE:
                            if self.__Player2.getJackpot():
                                print("JACKPOT POWERUP!!!!!")
                                print(f"Nice, you keep {sum(self.__Player2.getUnfoundDie()) * 2} gold! Good Job! ")
                                self.__Player2.addGold(sum(self.__Player2.getUnfoundDie()) * 2)
                                PLAYER2GO = 0
                                break
                            else:
                                print(f"Nice, you keep {sum(self.__Player2.getUnfoundDie())} gold! Good Job!")
                                self.__Player2.addGold(sum(self.__Player2.getUnfoundDie()))
                                PLAYER2GO = 0
                                break
                        else:
                            self.__Player2.rollDice()
                    else:
                        if self.__Player2.getJackpot():
                            print("JACKPOT POWERUP!!!!!")
                            print(f"Nice, you keep {sum(self.__Player2.getUnfoundDie()) * 2} gold! Good Job! ")
                            self.__Player2.addGold(sum(self.__Player2.getUnfoundDie()) * 2)
                            PLAYER2GO = 0
                        else:
                            print(f"Nice, you keep {sum(self.__Player2.getUnfoundDie())} gold! Good Job!")
                            self.__Player2.addGold(sum(self.__Player2.getUnfoundDie()))
                            PLAYER2GO = 0
                # If the player has not found the necessary requirements of the game
                else:
                    if self.__Player2.getNumberRolls() > 0:
                        pass
                    else:
                        print("No gold was found :(")
                        PLAYER2GO = 0
            if self.__Player1.getGold() > self.__Player2.getGold():
                print(f"{self.__Player1.getName()} wins this round!")
            elif self.__Player1.getGold() == self.__Player2.getGold():
                print("Its a tie!")
            else:
                print(f"{self.__Player2.getName()} wins this round!")
            BUFFER = input("> ")
            print("Welcome to the powerup shop, where all sorts of advantages can be bought with gold!")
            print(f"{self.__Player1.getName()} buys")
            self.__Player1.askBuy()
            print(f"{self.__Player2.getName()} buys")
            self.__Player2.askBuy()
            self.replay()
            self.__Player1.resetRolls(self.__Player2.getSabotage()) # Resets the rolls of player 1
            self.__Player2.resetRolls(self.__Player1.getSabotage()) # Resets the rolls of player 2

    def replay(self):
        """
        Asks the user if they want to play again
        :return: exit()
        """
        CHOICE = input("Press (1) to play again and (2) to exit.")
        if CHOICE.isnumeric():
            CHOICE = int(CHOICE)
        else:
            print("""Please enter a proper integer!""")
            return self.replay()
        if CHOICE > 0 and CHOICE < 3:
            pass
        else:
            print("Please input a integer within the given ranges!")
            return self.replay()
        if CHOICE == 1:
            pass
        else:
            return exit()

if __name__ == "__main__":
    GAME = Game()
    GAME.Run()