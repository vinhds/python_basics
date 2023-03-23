#Wesley has recently visited the arcade and has tasked himself with mastering all songs on Dance Dance Revolution.
#Unfortunately, the machine that Wesley has claimed is broken and is unable to keep track of his score.
#Can you help Wesley determine his final score?
#
#In Dance Dance Revolution, there are 4 different moves that can be played - up, down, left, and right.
#
#The song that Wesley plays consists of multiple beats and he will match each beat with a single move.
#Every move is worth 1 point (regardless of whether it is part of a combo or not).
#The song is described by a sequence of characters consisting of U, D, L, and R, representing the moves up, down, left, and right.
#We will call this sequence S .
#
#A combo is defined by a specific ordering of moves played consecutively.
#There are M different combos, which can also be described by a sequence of characters consisting of U, D, L, and R
#the i t h of which is C i . Each combo is also associated with a point value P i , which is earned each time a combo is completed.
#
#To determine which moves are part of combos, the following algorithm is used.
#
#    Set the current move to the first move that Wesley performs.
#    Select the longest combo such that the | C i | moves in the combo match the next | C i | moves (starting from the current move)
#    in the sequence of moves that Wesley performs (in the same order), where | C i | is the length of the chosen combo.
#    It may be the case that such a combo does not exist, in which case, the longest combo has a length of 0 .
#    The current move becomes the move immediately after the last move in the longest combo 
#    (or the move immediately after the current move if no such combo exists).
#    If the current move is past the end of the sequence, terminate the algorithm.
#    Go to step 2.
#
#It can be seen that a single move may only correspond to at most one combo, although the same combo may be played multiple times.
#
#No two combos will be identical.
#
#Given a series of moves that Wesley performs, can you determine how many points he scored?
#Constraints
#
#For this problem, you will NOT be required to pass all the samples in order to receive points.
#In addition, you must pass all previous subtasks to earn points for a specific subtask.
#
#For all subtasks:
#
#1 ≤ | S | ≤ 1 000 where | S | is the length of S .
#1 ≤ M ≤ 5
#2 ≤ | C i | ≤ 5 where | C i | is the length of C i .
#2 ≤ P i ≤ 1 000
#
#S and C i will consist only of the characters U, D, L, and R.
#Subtask 1 [30%]
#
#M = 1
#Subtask 2 [70%]
#
#No additional constraints.
#Input Specification
#
#The first line will contain a string S , Wesley's moves. Each character will be one of U, D, L, or R.
#
#The second line of input will contain M , the number of different combos.
#
#The next M lines will each contain C i , the combo sequence and P i , the points the combo is worth.
#Each character in C i will be one of U, D, L, or R.
#Output Specification
#
#Output a single integer, the number of points that Wesley scored.

# Get the input
# The first line is a string S, Wesley's moves. 
wesley_moves = input()
# The second line is the number of different combos.
n_combos = int(input())
combos_list = []
points_list = []
# The next n_combos lines will each contain a combo sequence and the points the combo is worth.
# Store these in two lists.
for i in range(n_combos):
    sequence = input()
    combo, points = sequence.split(' ')
    points = int(points)
    combos_list.append(combo)
    points_list.append(points)
score = 0
score_earned = 0
max_length = 0
current_loc = 0
combo_found =  False
while current_loc < len(wesley_moves):
    current_move = wesley_moves[current_loc]
    for i in range(n_combos):
        if combos_list[i][0] == current_move:
            combo_length = len(combos_list[i])
            if (current_loc + combo_length) < len(wesley_moves):
                if wesley_moves[current_loc:(current_loc + combo_length)] == combos_list[i]:
                    combo_found = True
                    if combo_length > max_length:
                        max_length = combo_length
                        score_earned = points_list[i]
    if combo_found == True:
        current_loc += max_length
        score += score_earned
    else:
        current_loc += 1
    max_length = 0
    combo_found = False

print(score + len(wesley_moves))





