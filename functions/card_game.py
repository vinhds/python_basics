#Write a program that will keep score for a simple two-player game, played with a deck of cards.
#There are 52 cards in the deck; four of each of 13 possible names:
#    two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace.
#    The cards labelled jack, queen, king, and ace are collectively known as high cards.
#
#The deck is shuffled and placed face-down on the table. Player A turns over the top card and places it on a pile;
#then player B turns over the top card and places it on the pile.
#A and B alternate until the deck is exhausted. The game is scored as follows:
#
#    If a player turns over an ace, with at least 4 cards remaining to be turned over,
#    and none of the next 4 cards is a high card, that player scores 4 points
#    If a player turns over a king, with at least 3 cards remaining to be turned over,
#    and none of the next 3 cards is a high card, that player scores 3 points
#    If a player turns over a queen, with at least 2 cards remaining to be turned over,
#    and none of the next 2 cards is a high card, that player scores 2 points
#    If a player turns over a jack, with at least 1 card remaining to be turned over,
#    and the next card is not a high card, that player scores 1 point
#
#Input Specification
#
#The input will contain 52 lines. Each line will contain the name of a card in the deck, in lowercase letters.
#The first line denotes the first card to be turned over; the next line the next card; and so on.
#Output Specification
#
#Whenever a player scores, print Player X scores n point(s). where X is the name of the player (A or B)
#and n is the number of points scored (1, 2, 3, or 4). At the end of the game, print the total score for each player, on two lines:
#Copy
#
#Player A: n point(s).
#Player B: m point(s).


