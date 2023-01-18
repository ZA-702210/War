#Name: Zubair Azizi
#Date: Jan 20, 2023
#Purpose: To create a randomized war game that saves the number of wins you have. 

#Randomizer
import random

#Font colour
import colorama #Fore.(colour) determines the colour
from colorama import Fore, Back

#Used for clearing the console
import os
def clear_console():
  os.system('clear')
#clear_console()
  
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

#Takes the players input from the main screen
def plrChoiceHandler(int):
  
  global plrUsername
  plrUsername = False
  if int == 1:
    clear_console()
    while True:
      plrUsername = input(Fore.BLUE+'Please type your username: ')
      if os.path.exists(plrUsername+'.txt'):
        print('Welcome back, '+plrUsername+"!")
        entry = open(plrUsername+'.txt', 'r')
        print('You have '+entry.read()+" wins so far.")
        entry.close()
        input('Press enter to continue.')
        clear_console()
        runGame(1)
        break
      else:
        entry = open(plrUsername+'.txt', 'w')
        entry.write('0')
        print('Welcome to War!, '+plrUsername)
        input('Press enter to continue.')
        entry.close()
        clear_console()
        runGame(1)
        break
    
  elif int == 2:
    clear_console()
    while True:
      plrUsername = input('Please type your username: ')
      if os.path.exists(plrUsername+'.txt'):
        print('Welcome back, '+plrUsername+"!")
        entry = open(plrUsername+'.txt', 'r')
        print('You have '+entry.read()+" wins so far.")
        entry.close()
        input('Press enter to continue.')
        runGame(1)
        break
      else:
        print('Your username was not found, check for spelling errors and try again.')
        input('Press enter to continue.')
  
  elif int == 3:
    clear_console()
    runGame(2)
  
  elif int == 4:
    clear_console()
    print('Exitting')
    exit()

#

def runGame(saveStatus):
  
  
  #Collection of all the cards in rows, column (1) is the cards name and column (2) is the cards value which determines if its better or not than the opponents card
  plrDeckOfCards = [("Ace of Spades",11),("Two of Spades",2),("Three of Spades",3),("Four of Spades",4),("Five of Spades",5),("Six of Spades",6),("Seven of Spades",7),("Eight of Spades",8),("Nine of Spades",9),("Ten of Spades",10),("Jack of Spades",11),("Queen of Spades",12),("King of Spades",13),("Ace of Clubs",11),("Two of Clubs",2),("Three of Clubs",3),("Four of Clubs",4),("Five of Clubs",5),("Six of Clubs",6),("Seven of Clubs",7),("Eight of Clubs",8),("Nine of Clubs",9),("Ten of Clubs",10),("Jack of Clubs",11),("Queen of Clubs",12),("King of Clubs",13),("Ace of Hearts",11),("Two of Hearts",2),("Three of Hearts",3),("Four of Hearts",4),("Five of Hearts",5),("Six of Hearts",6),("Seven of Hearts",7),("Eight of Hearts",8),("Nine of Hearts",9),("Ten of Hearts",10),("Jack of Hearts",11),("Queen of Hearts",12),("King of Hearts",13),("Ace of Diamonds",11),("Two of Diamonds",2),("Three of Diamonds",3),("Four of Diamonds",4),("Five of Diamonds",5),("Six of Diamonds",6),("Seven of Diamonds",7),("Eight of Diamonds",8),("Nine of Diamonds",9),("Ten of Diamonds",10),("Jack of Diamonds",11),("Queen of Diamonds",12),("King of Diamonds",13)]

  botDeckOfCards = [("Ace of Spades",11),("Two of Spades",2),("Three of Spades",3),("Four of Spades",4),("Five of Spades",5),("Six of Spades",6),("Seven of Spades",7),("Eight of Spades",8),("Nine of Spades",9),("Ten of Spades",10),("Jack of Spades",11),("Queen of Spades",12),("King of Spades",13),("Ace of Clubs",11),("Two of Clubs",2),("Three of Clubs",3),("Four of Clubs",4),("Five of Clubs",5),("Six of Clubs",6),("Seven of Clubs",7),("Eight of Clubs",8),("Nine of Clubs",9),("Ten of Clubs",10),("Jack of Clubs",11),("Queen of Clubs",12),("King of Clubs",13),("Ace of Hearts",11),("Two of Hearts",2),("Three of Hearts",3),("Four of Hearts",4),("Five of Hearts",5),("Six of Hearts",6),("Seven of Hearts",7),("Eight of Hearts",8),("Nine of Hearts",9),("Ten of Hearts",10),("Jack of Hearts",11),("Queen of Hearts",12),("King of Hearts",13),("Ace of Diamonds",11),("Two of Diamonds",2),("Three of Diamonds",3),("Four of Diamonds",4),("Five of Diamonds",5),("Six of Diamonds",6),("Seven of Diamonds",7),("Eight of Diamonds",8),("Nine of Diamonds",9),("Ten of Diamonds",10),("Jack of Diamonds",11),("Queen of Diamonds",12),("King of Diamonds",13)]
  
  print('In war, you are dealt 26 random cards.\nIn this game, you will go up against a computer. Both of you will select cards at random each round, which makes this game purely based on luck.\nGood luck!')
  input('Press enter to continue. ')

  cardCounter = 26
  plrWins = 0
  botWins = 0
  global plrCard
  global botCard
 
  while True:
    if cardCounter > 0:
      print('Cards left: '+str(cardCounter))

      try:
        plrCard = plrDeckOfCards[random.randint(0,len(plrDeckOfCards))]
        plrCardValue = plrCard[1]
        botCard = botDeckOfCards[random.randint(0, len(botDeckOfCards))]
        botCardValue = botCard[1]
      except:
        plrCard = plrDeckOfCards[random.randint(0,len(plrDeckOfCards))]
        plrCardValue = plrCard[1]
        botCard = botDeckOfCards[random.randint(0, len(botDeckOfCards))]
        botCardValue = botCard[1]

      print('You placed down '+plrCard[0]+'\n')
      print('The bot placed down '+botCard[0]+'\n')
      input('Press enter to continue')
      clear_console()

      if plrCard[1]>botCard[1]:
        plrWins = plrWins + 1
        print('You had a better card than the bot.')
        print('\nPlayer wins: '+str(plrWins)+'\nBot wins: '+str(botWins))
        input('Press enter to continue')
        clear_console()
      elif botCard[1]>plrCard[1]:
        botWins = botWins + 1
        print('The bot had a better card than you.')
        print('\nBot wins: '+str(botWins)+'\nPlayer wins: '+str(plrWins))
        input('Press enter to continue')
        clear_console()
      elif botCard[1] == plrCard[1]:
        print('Tie! No points gained or loss.')
        input('Press enter to continue')
        clear_console()
      
      cardCounter = cardCounter - 1
      plrDeckOfCards.remove(plrCard)
      botDeckOfCards.remove(botCard)
    else:
      print('Game over!')
      if plrWins>botWins:
        print('You won: '+str(plrWins)+ " wins")
        if not plrUsername == False:
          newTotalWins = int(open(plrUsername+'.txt', 'r').read())+1
          open(plrUsername+'.txt','w').write(str(newTotalWins))
          print('You now have '+open(plrUsername+'.txt', 'r').read()+' wins in total.')
       
        
        input('Press enter to continue')
        clear_console()
        plrChoice = startGame()
        plrChoiceHandler(plrChoice)
            
      elif plrWins<botWins:
        print('The bot won: '+str(botWins)+" wins. You've gained no points. ")

        input('Press enter to continue')
        clear_console()
        plrChoice = startGame()
        plrChoiceHandler(plrChoice)
        
      elif plrWins == botWins:
        print('Tie game!')
        
        plrChoice = startGame()
        plrChoiceHandler(plrChoice)
        plrChoice = startGame()
        plrChoiceHandler(plrChoice)
        
      input('Press enter to continue')
      clear_console()
      break

plrChoice = startGame()
plrChoiceHandler(plrChoice)