# Using this as way to note what the code is and understanding how to use classes and functions
# https://www.askpython.com/python/examples/blackjack-game-using-python
# code credited the person in link above
# did my method for dealing cards but problem lies where I can't show hidden card
# Dealing should be first then hit and stand phase but I don't have much to learn now with this project as its a tedious
# fix the issue but it would be to not to use loops and manually repeat the cards.
import random


def print_cards(cards, hidden):
    s = ""
    for i in cards:
        # \t: means tab
        s = s + "\t ________________"  # creates lines horizontally

    if hidden:
        s = s + "\t ________________"
    print(s)

    s = ""
    for i in cards:
        if i.value == 10:  # asking if 10 ask if it is that will mean the tab will moved one space extra
            s = s + "\t| {}             |".format(i.value)  # format will replace the {} with whatever card.value is

        else:
            s = s + "\t| {}              |".format(i.value)

    if hidden:
        s = s + "\t|                |"
    print(s)

    s = ""
    for i in cards:
        s = s + "\t|                |"
        if hidden:
            s = s + "\t|                |"
    print(s)
    s = ""
    for i in cards:
        s = s + "\t|       {}        |".format(i.suit)
        if hidden:  # the second card that is hidden in black jack will result in this line of code
            s = s + "\t|    UNKNOWN     |"
    print(s)

    s = ""
    for i in cards:
        s = s + "\t|                |"
        if hidden:
            s = s + "\t|                |"
    print(s)

    s = ""
    for i in cards:
        if i.value == 10:
            s = s + "\t|             {} |".format(i.value)
        else:
            s = s + "\t|              {} |".format(i.value)  # gets the value inside the class

        if hidden:
            s = s + "\t|                |"
    print(s)

    s = ""
    for i in cards:
        s = s + "\t ________________"
        if hidden:
            s = s + "\t ________________"
    print(s)


# Card
class Card:
    def __init__(self, suit, play_card, value):
        self.suit = suit
        self.play_cards = play_card
        self.value = value


# Deck
# Declaring the Suits
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

# suit character
suit_character = {"Spades": "♠", "Hearts": "♥", "Diamonds": "⬥", "Clubs": "♧"}

# declaring playing cards
playing_cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# declaring playing cards to values (ACE might have to be changed)
values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10,
          "King": 10}

# List for deck
deck = []
# Looping through each suit
for suit in suits:
    # looping through each playing card
    for card in playing_cards:
        # adds card to the deck
        deck.append(Card(suit_character[suit], card, values[card]))  # Stores object into list

print()


# Hands
def black_jack(deck):
    # player hand

    player_hand = []

    # player hand value

    player_value = 0

    win = 0
    # Dealing

    while True:
        # Players Turn
        card_pick = random.choice(deck)
        player_hand.append(card_pick)

        # Giving card value to hand
        player_value = player_value + card_pick.value

        # printing cards
        print("Player Hand: ", player_value)
        print_cards(player_hand, False)

        # Removing that card from List
        deck.remove(card_pick)

        # Ace Card
        if len(player_hand) == 2:  # Checks if player has 2 cards to decide what ace will be
            if player_hand[0] == 11 and player_hand[1]:
                player_hand[0] = 1
                player_hand[1] -= 10

        # Hit or stand
        if len(player_hand) >= 2:
            if player_value >= 21:
                break
            hit_stand = input("Would you like to hit or stand? ")
            if hit_stand.lower() == "stand":
                break
            else:
                continue

    # Dealer hand and value
    dealer_hand = []
    dealer_value = 0

    while True:
        # checks if player has hit more than 21
        if player_value > 21:
            print("Dealer Wins")
            win = 1
            break
        elif player_value == 21:
            print("Player BlackJack!")
        # Dealers hand
        card_pick = random.choice(deck)
        dealer_hand.append(card_pick)
        dealer_value = dealer_value + card_pick.value  # Giving dealers hand value
        print("Dealer Hand:")
        print_cards(dealer_hand, False)  # True means that it will show second card as unknown/ hide it
        print(dealer_value)

        # Ace Card
        if len(dealer_hand) == 2:  # Checks if player has 2 cards to decide what ace will be
            if dealer_hand[0] == 11 and dealer_hand[1]:
                dealer_hand[0] = 1
                dealer_hand[1] -= 10

        if dealer_value < 17:
            continue
        else:
            break
    # checks if dealer value is greater than player value and less than 21
    if win != 1:
        if player_value < dealer_value <= 21 or player_value > 21 > dealer_value:
            print("Player has lost")
        elif dealer_value < player_value <= 21 or dealer_value > 21 > player_value:
            print("Player has won")
        else:
            print("Draw")


# Check Win or Loss
black_jack(deck)
input()

