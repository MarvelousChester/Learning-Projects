# Create a BlackJack game against ai, The player gets to choose how many ai players
# try to create the program to just not generate a number but to actually get the type of card
# The programs should be under 256 lines of code, so that they're small enough
# for anyone to casually read and understand

import os  # imports windows commands for commandline
import random

clear = lambda: os.system('cls')  # this will clear the console as to show only one input , to call use clear()

# input for how many players to play against
while True:
    players = input("how many players do you want to play against(Max players: 4) ")
    if players == 1:
        continue
    try:
        players = int(players)
        if players == 1:
            print("Invalid input, Players have to be more than 1")
            continue
        else:
            clear()
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
clear()

# Deck and creating sample size for 312 deck
if deck_size == 312:
    deck = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit1 = (["Spades"] * 13) * 6
    suit2 = (["Diamonds"] * 13) * 6
    suit3 = (["Hearts"] * 13) * 6
    suit4 = (["Clubs"] * 13) * 6
    total_suits = suit1 + suit2 + suit3 + suit4
    # Drawing card move elsewhere
    v = random.randint(1, 13)
    suit_pick = random.sample(total_suits, k=1)
    print("I got a " + str(suit_pick[0]) + " " + str(v))
else:
    suit1 = (["Spades"] * 13)
    suit2 = (["Diamonds"] * 13)
    suit3 = (["Hearts"] * 13)
    suit4 = (["Clubs"] * 13)
    total_suits = suit1 + suit2 + suit3 + suit4


# function to draw cards
# assigning player hands

for i in range(5):
    print("-----------------")
    print("GAME IS STARTING")
    print("-----------------")

if players == 2:
    player1_hand = []   # player1 hand is always players hand
    player1_value = 0
    player2_hand = []
    player2_value = 0
elif players == 3:
    player1_hand = []
    player1_value = 0
    player2_hand = []
    player2_value = 0
    player3_hand = []
    player3_value = 0
elif players == 4:
    player1_hand = []
    player1_value = 0
    player2_hand = []
    player2_value = 0
    player3_hand = []
    player3_value = 0
    player4_hand = []
    player4_value = 0

# Player hand generator
while True:
    i = 0
    i = i + 1
    # assigns cards and value to player hand
    # generates a number from 1 to 13
    while True:
        v = random.randint(1, 13)
# gets a sample from 312 or 52 deck size cards so that there are unique suits but have not found solution for unique num
        suit_pick = random.sample(total_suits, k=1)
        h = suit_pick[0] + " " + str(v)
        # add whatever is drawn into a list
        player1_hand.append(h)
        print("I got a " + str(suit_pick[0]) + " " + str(v))
        print(player1_hand)
        # value of player hand
        player1_value += v
        print(player1_value)
    # does player want to hit or stand
        hit_stand = input("Do you want to hit or stand ")
        if hit_stand == "Hit" or hit_stand.lower() == "hit" or player1_value >= 21:
            if player1_value >= 21:
                break
            continue
        elif hit_stand == "Stand" or hit_stand.lower() == "stand" or player1_value >= 21:
            break
        # checks value of players and too see if they have lost or won
        if player1_value == 21:
            break
        elif player1_value > 21:
            print("Player 1 has lost")
        elif 21 >= player1_value > player2_value:
            print("Player 1 has won")
        elif player1_value == player2_value:
            print("Its a draw")


# number generator from ace to king

# ai

## https://www.youtube.com/watch?v=KzqSDvzOFNA watch this video on RAndom Module
