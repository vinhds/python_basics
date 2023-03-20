#In a basketball match, we know how many points both Team A and Team B have scored and the exact second when it happened.
#Within a second, it will not be possible to score more than one point.
#King James is observing the task input and wants to answer the following two questions:
#
#    How many points have been scored during the first half-time, that is in the first half of the game,
#    if we know that the entire game lasts 4 × 12 minutes?
#
#    How many "turnarounds" have happened during the match, i.e.
#    how many times has a team come from a losing situation (has strictly fewer points scored than the other team)
#    to a leading one (has strictly more points scored than the other team)?
#
#Input Specification
#
#The first line contains a positive integer A ( 1 ≤ A ≤ 2879 ) ,
#the number of points Team A has scored. In the following A lines there are positive integers A s ( 1 ≤ A s ≤ 2880 ) ,
#the seconds in which Team A was scoring points ordered from the smallest to the largest number.
#
#In the ( A + 2 ) t h line there is a positive integer B ( 1 ≤ B ≤ 2879 ) ,
#the number of points Team B has scored. In the following B lines there are positive integers B s ( 1 ≤ B s ≤ 2880 ) ,
#the seconds in which Team B was scoring points ordered from the smallest to the largest number.
#Output Specification
#
#In the first line print an integer value, the answer to the first question from the text of the task.
#
#In the second line print an integer value, the answer to the second question from the text of the task.

team_A_pts = int(input())
team_A_when = []
for i in range(team_A_pts):
    score_time = int(input())
    team_A_when.append(score_time)

team_B_pts = int(input())
team_B_when = []
for i in range(team_B_pts):
    score_time = int(input())
    team_B_when.append(score_time)
score_times = team_A_when + team_B_when
score_times.sort()
first_half_pts = 0
A_score = 0
B_score = 0
num_turnarounds = 0
result = []

for i in range(len(score_times)):
    if score_times[i] <= 1440:
        first_half_pts += 1
    if score_times[i] in team_A_when:
        A_score += 1
    elif score_times[i] in team_B_when:
        B_score += 1
    current_result = A_score > B_score
    result.append(current_result)
for i in range(2, len(result)):
    if result[i-2:i+1] == [True, False, False] or result[i-2:i+1] == [False, False, True]:
        num_turnarounds += 1
        
print(first_half_pts)
print(num_turnarounds)
