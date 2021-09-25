# Create a BlackJack game against ai, The player gets to choose how many ai players
# try to create the program to just not generate a number but to actually get the type of card
# The programs should be under 256 lines of code, so that they're small enough
# for anyone to casually read and understand

import os # imports windows commands for commandline
clear = lambda: os.system('cls') # this will clear the console as to show only one input , to call use clear()

# input

players = int(input( "how many players do you want to play against "))
clear()

deck_size = ()

while True:
    deck_size = input("What deck size do you want it to be \n Standard: 1 \n 6 deck: 2 \n ")
    try:
        deck_size = int(deck_size)
    except:
        clear()
        print("Invalid input, retry")
        continue
    if deck_size == 1:
        deck_size = 52
        break
    elif deck_size == 2:
        deck_size = 52 * 6
        break

print(deck_size)
# does player want to hit or stand
# number generator from ace to king

# ai
