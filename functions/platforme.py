#A level is being designed for a new platform game. The locations of the platforms have been chosen.
#Contrary to popular opinion, platforms can't float in the air, but need pillars for support.
#More precisely, each of the two ends of the platform needs to be supported by a pillar standing on the floor or on a different platform.
#
#You will be given the locations of the platforms in a coordinate system as in the left image below.
#Each platform's location is determined by its altitude (vertical distance from the ground)
#and the start and end coordinates in the horizontal direction.
#Each support pillar is placed half a unit from the end of a platform, as in the right image.
#
#Determine the total length of pillars needed to support all the platforms.
#Input Specification
#
#The first line contains the integer N , 1 ≤ N ≤ 100 , the number of platforms.
#Each of the following N lines contains the position of one platform, three coordinates Y , X 1 and X 2 .
#
#The first number is the altitude, the other two the horizontal coordinates.
#All coordinates will be positive integers less than 10 000 satisfying X 2 > X 1 + 1
#(i.e. the length of each platform will be at least 2 ).
#
#The input will be such that no two platforms overlap.
#Output Specification
#
#Output the total length of pillars needed to support all the platforms.

# Idea: 
# Store the coordinates of all platforms in a list of tuple (height, x_1, x_2)
# Sort the list. It will be sorted based on the height.
# For each platform, consider all platforms lower than it. Check on the left and check on the right
# to see whether a pillar can be built from a lower platform. Then calculate the height based on that.

# Implementation:

# STEP 1: Write a function that will calculate the height of a pillar for a given platform
def pillar_length(height, coordinate, platforms):
    """
    height: an integer that is the height f the platform under consideration
    coordinate: either the (left+0.5) or the (right-0.5) x-coordinate of the platform under consideration
    platforms: list of platforms each of whose height is smaller than that of the given platform
    each item in the list is a tuple of three integers (height, x_1, x_2)
    Also assume that the platforms are ordered in non-increasing height

    return the length of the pillar closest to coordinate (left pillar or right pillar only)
    """
    result = height
    for platform in platforms:
        if platform[1] <= coordinate <= platform[2]:
            result = height - platform[0]
            break
    return result
# Test the pillar_length function
# print(pillar_length(5, 3.5, [(3,1,5), (1,5,10)]))
# STEP 2: Solve the problem
# Get the input 
n_platforms = int(input())
platforms = []
for i in range(n_platforms):
    height, x_1, x_2 = map(int, input().split(' '))
    platforms.append((height, x_1, x_2))

sorted_platforms = sorted(platforms)
total_height = 2 * sorted_platforms[0][0]
for i in range(1, n_platforms):
    height = sorted_platforms[i][0]
    #print('Current platform height: ',height)
    left_coord = sorted_platforms[i][1] + 0.5
    right_coord = sorted_platforms[i][2] - 0.5
    left_length = pillar_length(height, left_coord, sorted_platforms[(i-1)::-1])
    #print('Length of left pillar: ', left_length) 
    right_length = pillar_length(height, right_coord, sorted_platforms[(i-1)::-1])
    #print('Length of right pillar: ', right_length)
    total_height += (left_length + right_length)

print(total_height)

