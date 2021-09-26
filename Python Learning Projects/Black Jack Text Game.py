# Create a BlackJack game against ai, The player gets to choose how many ai players
# try to create the program to just not generate a number but to actually get the type of card
# The programs should be under 256 lines of code, so that they're small enough
# for anyone to casually read and understand

import os  # imports windows commands for commandline

clear = lambda: os.system('cls')  # this will clear the console as to show only one input , to call use clear()

# input for how many players to play against
while True:
    players = input("how many players do you want to play against ")
    try:
        players = int(players)
        break
    except:
        clear()
        print("invalid input,retry")
# input for what deck size to play with
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
print("There are " + str(players) + " Players")
print("Deck size is:" + str(deck_size))

# special cards value
counter = 0
ace = 1 or 11  # tricky as ace values differs depending on what card player has COME BACK TO THIS AND Deal with that
jack = 11
queen = 12
king = 13
# list for cards which depended on the previous answer on deck size
if deck_size == 312:
    card_list = ([ace, 2, 	3, 	4, 	5, 	6, 	7, 8, 9, 10, jack, queen, king] * 4) * 6  # makes list to 312 cards
else:
    card_list = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king] * 4  # makes deck into 52 cards
for i in card_list:   # small counter to for testing, REmove after
    counter += 1
print(card_list)
print(counter)
# function to draw cards
# does player want to hit or stand

# number generator from ace to king

# ai
