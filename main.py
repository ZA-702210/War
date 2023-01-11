#Name: Zubair Azizi
#Date: Jan 20, 2023
#Purpose: To create a randomized war game that saves the number of wins you have. 

#Randomizer
import random

#Setting a wait
import time

#SQL
import sqlite3

#Font colour
import colorama #Fore.(colour) determines the colour
from colorama import Fore, Back

#Used for clearing the console
import os
def clear_console():
  os.system('clear')
#clear_console()

#Collection of all the cards in rows, column (1) is the cards name and column (2) is the cards value which determines if its better or not than the opponents card
deckOfCards = [("Ace of Spades",11),("Two of Spades",2),("Three of Spades",3),("Four of Spades",4),("Five of Spades",5),("Six of Spades",6),("Seven of Spades",7),("Eight of Spades",8),("Nine of Spades",9),("Ten of Spades",10),("Jack of Spades",11),("Queen of Spades",12),("King of Spades",13),("Ace of Clubs",11),("Two of Clubs",2),("Three of Clubs",3),("Four of Clubs",4),("Five of Clubs",5),("Six of Clubs",6),("Seven of Clubs",7),("Eight of Clubs",8),("Nine of Clubs",9),("Ten of Clubs",10),("Jack of Clubs",11),("Queen of Clubs",12),("King of Clubs",13),("Ace of Hearts",11),("Two of Hearts",2),("Three of Hearts",3),("Four of Hearts",4),("Five of Hearts",5),("Six of Hearts",6),("Seven of Hearts",7),("Eight of Hearts",8),("Nine of Hearts",9),("Ten of Hearts",10),("Jack of Hearts",11),("Queen of Hearts",12),("King of Hearts",13),("Ace of Diamonds",11),("Two of Diamonds",2),("Three of Diamonds",3),("Four of Diamonds",4),("Five of Diamonds",5),("Six of Diamonds",6),("Seven of Diamonds",7),("Eight of Diamonds",8),("Nine of Diamonds",9),("Ten of Diamonds",10),("Jack of Diamonds",11),("Queen of Diamonds",12),("King of Diamonds",13)]
  
#Start Game
def startGame():
  print(Fore.RED+'Welcome to War!')
  print("""
        _____
       |A .  | _____
       | /.\ ||A ^  | _____
       |(_._)|| / \ ||A _  | _____
       |  |  || \ / || ( ) ||A_ _ |
       |____V||  .  ||(_'_)||( v )|
              |____V||  |  || \ / |
                     |____V||  .  |
                            |____V|

  """)

  
  #Asks the player if theyre a new user, returning user, if they wanna play without saving their wins, or if they want to exit the game. Done in a loop in case of erroring. 
  while True:
    print(Fore.RESET + '\n\n[1] New User\n[2] Returning User\n[3] Play without saving game data\n[4] Exit')
   
    #Gets the players choice, and error checks responses
    try:
      plrAnswer = int(input('\n\nYour option:'))
      if plrAnswer == 1 or plrAnswer == 2 or plrAnswer == 3 or plrAnswer == 4:
        return plrAnswer #sets plrChoice equal to the answer to provide for the next function
        break
      
      #If response is not an accepted integer
      else:
        input('Invalid response. Press enter to try again.')
        clear_console()
    
    #If response is not an integer
    except:
      input('Invalid response. Press enter to try again.')
      clear_console()

#

def plrChoiceHandler(int):
  if int == 1:
    clear_console()


plrChoice = startGame()