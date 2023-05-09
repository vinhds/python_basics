#Farmer John's 3 prize cows, Bessie, Elsie, and Mildred, are always wandering off to the far reaches of the farm! He needs your help herding them back together.
#
#The main field in the farm is long and skinny -- we can think of it as a number line, on which a cow can occupy any integer location. The 3 cows are currently situated at different integer locations, and Farmer John wants to move them so they occupy three consecutive locations (e.g., positions 6, 7, and 8).
#
#Unfortunately, the cows are rather sleepy, and Farmer John has trouble getting their attention to make them move. At any point in time, he can only make a cow move if she is an "endpoint" (either the minimum or maximum position among all the cows). When he moves a cow, he can instruct her to move to any unoccupied integer location as long as in this new location she is no longer an endpoint. Observe that over time, these types of moves tend to push the cows closer and closer together.
#
#Please determine the minimum and maximum number of moves possible before the cows become grouped in three consecutive locations.
#
#INPUT FORMAT (file herding.in):
#The input file contains one line with three space-separated integers, giving the locations of Bessie, Elsie, and Mildred. Each location is an integer in the range 1…109
#.
#
#OUTPUT FORMAT (file herding.out):
#The first line of output should contain the minimum number of moves Farmer John needs to make to group the cows together. The second line of output should contain the maximum number of such moves he could conceivably make before the cows become grouped together. 

# Plan:
# Have a function to check if the locations of the cow are consecutive. 
# While the locations are not consecutive, move the cows in a way that maximize the number of moves and
# another way that minimize the number of moves.
# The number of moves would be maximized if one of the endpoints move to the wider interval.
# The number of moves would be minimized if the one of the endpoints move to the narrower interval.

def check_consecutive(num_list):
    """
    num_list is a list of sorted integers

    Return True if the 3 integers are consecutive and False otherwise
    """
    if (num_list[1] - num_list[0] == 1) and (num_list[2] - num_list[1] == 1):
        check = True
    else:
        check = False
    return check

# Test the check_consecutive function
#print(check_consecutive(1,2,4))
#print(check_consecutive(4,7,9))
#print(check_consecutive(10, 8, 9))
#print(check_consecutive(0,1,2))
def move(num_list): 
    """
    num_list is a list of sorted integers. Assume the integers are sorted in ascending order.

    Return a list by moving closer to consecutive integers in the either the longest possible way or the shortest possible way
    """
    smallest = num_list[0]
    middle = num_list[1]
    largest = num_list[2]
    if middle - smallest > largest - middle:
        num_list[1] = smallest + 1
        num_list[2] = middle
    else:
        num_list[0] = middle
        num_list[1] = middle + 1
    return num_list
#print(move([7,8,20]))
#print(move([4,7,9], choice='min'))


# Read input
file_name = 'herding_files/9.in'
input_file = open(file_name, 'r')
line = list(map(int,input_file.readline().rstrip().split(' ')))
input_file.close()
line.sort()
line_1 = line.copy()
max_count = 0
while check_consecutive(line) == False:
    line = move(line)
    max_count += 1
if check_consecutive(line_1) == True:
    min_count = 0
else:
    if (line_1[1] - line_1[0] == 2) or (line_1[2] - line_1[1] == 2): 
        min_count = 1
    else:
        min_count = 2
output_file = open('herding.out', 'w')
output_file.write(str(min_count))
output_file.write('\n')
output_file.write(str(max_count))
output_file.close()

