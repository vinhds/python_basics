#You decide to go for a very long drive on a very straight road. Along this road are five cities.
#As you travel, you record the distance between each pair of consecutive cities.
#
#You would like to calculate a distance table that indicates the distance between any two of the cities you have encountered.
#Input Specification
#
#The first line contains 4 positive integers less than 1 000 ,
#each representing the distances between consecutive pairs of consecutive cities:
#    specifically, the i th integer represents the distance between city i and city i + 1 .
#Output Specification
#
#The output should be 5 lines, with the i th line ( 1 ≤ i ≤ 5 )
#containing the distance from city i to cities 1 , 2 , 3 , 4 , 5 in order, separated by one space.

# Plan:
# 1. Write a distance function that calculate dist(i,j) from city i and city j.
# 2. Write a function to make each row of the matrix.
# 3. Write a function to print each row.

# Get the input
consec_distances = list(map(int, input().split(' ')))

def dist(i, j):
    d = 0
    if i < j:
        k = j - i
        l = 0
        while l < k:
            d += consec_distances[i + l]
            l += 1
    elif i > j:
        d = dist(j, i)
    return d

