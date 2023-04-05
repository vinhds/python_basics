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
# This is O(n^3) with a coefficient k of kn^2 with k>=2

# Get the input
consec_distances = list(map(int, input().split(' ')))

# Calculate the distance between two cities
# Example: d[1,4] = d[1] + d[2] + d[3] where d[1] = d[1,2], d[2] = d[2,3], d[3] = d[3,4] are the consecutive distances
# So in general if i < j: d[i,j] = d[i] + d[i+1] + ... + d[i + (j - i - 1)] where d[m] = d[m, m+1]
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

# Make any row of the matrix
def make_row(index, n_cols):
    row = []
    for i in range(n_cols):
        row.append(dist(index, i))
    return row
# Print any row of the matrix
def print_row(row):
    for item in row:
        print(item, end=' ')
    print('\n')

# Solve the problem
for i in range(5):
    row = make_row(i, 5)
    print_row(row)

