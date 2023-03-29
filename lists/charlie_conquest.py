#Charlie just downloaded the new free-to-play game Raid: Shadow Legends Conquest.
#Just what he wanted! In this game, he must defeat enemies, all of which are bots,
#and restore power to his clan. Both Charlie and the enemy before him start with H health points.
#Then, the two take turns performing actions, with Charlie going first. On each turn, one can perform one of two actions:
#
#    A d Attack your opponent, dealing d damage.
#    D d Dodge your opponent if they attack on the next turn. If they do not attack on the next turn, take d damage from self-humility.
#
#Bec computer genius, Charlie has hacked the game and created two lists of N actions
#each representing what the opponent will do and what he will do.
#Your job is to simulate his battle and find out who wins.
#If any person's health reaches 0 or below, your program is to output the correct answer and terminate.
#
#Note: Dodging at the end of the list of actions counts as a failed dodge.
#(i.e. if the enemy prepares a dodge as their last move, they will inflict self-harm.)
#Input Specification
#
#The first line of input contains two space separated positive integers N and H .
#
#The next N lines contain an uppercase Latin letter and a non-negative integer d representing Charlie's actions.
#
#The next N lines contain an uppercase Latin letter and a non-negative integer d representing his opponent's actions.
#Output Specification
#
#Output VICTORY if Charlie wins or DEFEAT if he loses or TIE if none of them die.
#Constraints
#
#1 ≤ N , H ≤ 1000
#
