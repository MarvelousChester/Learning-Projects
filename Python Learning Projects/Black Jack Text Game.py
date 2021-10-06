# Create a BlackJack game against ai, The player gets to choose how many ai players
# try to create the program to just not generate a number but to actually get the type of card
# The programs should be under 256 lines of code, so that they're small enough
# for anyone to casually read and understand

import os  # imports windows commands for commandline
import random

clear = lambda: os.system('cls')  # this will clear the console as to show only one input , to call use clear()

# input for how many players to play against
# not needed code just there
while True:
    players = input("how many players do you want to play against(Max players: 2) ")
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

clear()
if players == 2:
    player1_hand = []   # player1 hand is always players hand
    player1_value = 0
    player2_hand = []
    player2_value = 0

# Player hand generator
while True:
    # Most likey could use function instead of all these loops to do the same thing with fewer lines
    # just don't know how. After Done program Redo this part as a function
    # assigns cards and value to player hand
    while True:

        while True:
            print("Player 1:")
            v = random.randint(1, 13)
# gets a sample from 312 or 52 deck size cards so that there are unique suits but have not found solution for unique num
            suit_pick = random.sample(total_suits, k=1)
            h = suit_pick[0] + " " + str(v)
            # add whatever is drawn into a list
            player1_hand.append(h)
            print("PLayer Hand: ")
            for i in range(len(player1_hand)):
                print (player1_hand[i], end=' ')
            # value of player hand
            print(end="\n")
            player1_value += v
            print("Hand Value:" + str(player1_value,))
        # does player want to hit or stand
            if player1_value <= 21:
                hit_stand = input("Do you want to hit or stand ")
            if hit_stand == "Hit" or hit_stand.lower() == "hit" or player1_value >= 21:
                if player1_value >= 21:
                    clear()
                    break
                continue
            elif hit_stand == "Stand" or hit_stand.lower() == "stand" or player1_value >= 21:
                clear()
                break
        print(player1_hand, player1_value)
        # PLAYER 2 LOOP
        while True:
            if player1_value > 21:
                print("Player 2 has won!")
                break
            print("Player 2:")
            v = random.randint(1, 13)
# gets a sample from 312 or 52 deck size cards so that there are unique suits but have not found solution for unique num
            suit_pick = random.sample(total_suits, k=1)
            h = suit_pick[0] + " " + str(v)
            # add whatever is drawn into a list
            player2_hand.append(h)
            print("PLayer Hand: ")
            for i in range(len(player2_hand)):
                print(player2_hand[i], end=' ')
            # value of player hand
            print(end="\n")
            player2_value += v
            print("Hand Value:" + str(player2_value,))
            # does player want to hit or stand
            if player2_value <= 21:
                hit_stand = input("Do you want to hit or stand ")
            if hit_stand == "Hit" or hit_stand.lower() == "hit" or player2_value >= 21:
                if player2_value >= 21:
                    break
                continue
            elif hit_stand == "Stand" or hit_stand.lower() == "stand" or player2_value >= 21:
                break

        # checks to see value too see what player has won
        if player1_value > 21 and player2_value > 21:
            print("Nobody has won")
            break
        elif player1_value == 21 and player2_value < 21 or player2_value < player1_value < 21:
            print("Player 1 Has won!")
            break
        elif player1_value == player2_value:
            print("Its a draw")
            break
        elif player2_value == 21 and player1_value < 21 or player1_value < player2_value < 21 or player1_value > 21:
            print("Player 2 has won!")
            break


    break
# Place Holder
print(input())

