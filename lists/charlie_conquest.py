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

# Get the input
# Store Charlie's actions and the bot's actions in 2 lists
# Store the damages from Charlie's actions and the bot's actions in 2 other lists

n_rounds, health = map(int, input().split(' ')) 
charlie_actions = []
bot_actions = []
charlie_damages = []
bot_damages = []
charlie_health = health
bot_health = health
for i in range(n_rounds):
    charlie_c, charlie_d = input().split(' ')
    charlie_actions.append(charlie_c)
    charlie_damages.append(int(charlie_d))
for i in range(n_rounds, 2*n_rounds):
    bot_c, bot_d = input().split(' ')
    bot_actions.append(bot_c)
    bot_damages.append(int(bot_d))
#print(charlie_actions)
#print(charlie_damages)
#print(bot_actions)
#print(bot_damages)
for i in range(2*n_rounds):
    index = i // 2
    if i % 2 == 0:
        if charlie_actions[index] == 'A':
            if i == 0:
                bot_health -= charlie_damages[index]
            else:
                if bot_actions[index-1] != 'D':
                    bot_health -= charlie_damages[index]
        else:
            if i > 0 and bot_actions[index - 1] == 'D':
                bot_health -= bot_damages[index-1]
        #print(f'After the {i+1} turn, Charlie\'s health is {charlie_health}')                 
        #print(f'After the {i+1} turn, Bot\'s health is {bot_health}')
    else:
        if bot_actions[index] == 'A':
            if charlie_actions[index] == 'A':
                charlie_health -= bot_damages[index]
        else:
            if index == n_rounds-1:
                bot_health -=  bot_damages[index]
            else:
                if charlie_actions[index] == 'D':
                    charlie_health -= charlie_damages[index]
        #print(f'After the {i+1} turn, Charlie\'s health is {charlie_health}')                 
        #print(f'After the {i+1} turn, Bot\'s health is {bot_health}')
    #print(f'Charlie\'s health in round {i} is {charlie_health}')
    #print(f'Bot\'s health in round {i} is {bot_health}')
    if charlie_health <= 0 or bot_health <= 0:
        break
if charlie_health <= 0:
    print('DEFEAT')
elif bot_health <= 0:
    print('VICTORY')
else:
    print('TIE')
