#A nice part of the Roman Catholic Mass is the rite of peace when people shake hands with their neighbours and say "peace be with you".
#Mirko has found a way to turn this ritual into his own favour.
#
#Inside the church, there are R rows of benches where each row can hold a capacity of S people.
#We can imagine the seating order as a matrix sized R × S where each element represents either a person or an empty seating space.
#Let us assume that each person shakes hands with their neighbours.
#That means that the neighbours are located in one of the eight neighbouring elements (if such element exists)
#A seating order of the people inside the church has been given before Mirko enters.
#Mirko is, of course, late for the morning Mass and will sit in an empty space so that he shakes hands with as many people as he can.
#If there are no empty seats left, Mirko will simply give up on the idea and go to the evening Mass instead.
#We can assume that nobody enters the church after Mirko.
#
#Calculate the total number of handshakes given during the morning Mass.
#Input
#
#The first line of input contains positive integers R and S ( 1 ≤ R , S ≤ 50 ) as stated in the text.
#Each of the following R lines contains S characters. These R × S characters represent the seating order.
#The character . represents an empty place and the character o represents a person.
#Output
#
#The first and only line of output should contain the required number of handshakes.

# Idea:
# 1. Write a function to count the number of handshakes at a location (i, j)
# 2. Given a matrix, write a function to count the total number of handshakes for the matrix.
# 3. If a matrix has empty seats, go through all empty seats and find the location that gives the max
# number of handshakes. 

# Implementation:
# STEP 1: Write a function that count the number of handshakes that a person seating at the (i,j) location
# in a matrix will perform
def handshakes_count_one(i, j, m):
    """
    i: integer that correspond to the row
    j: integer that correpond to the column
    m: 2 dimensional list

    return the number of handshakes that a person at (i,j) does
    """
    neighbors = []
    n_cols = len(m[0])
    n_rows = len(m)
    # Case where the matrix has only one row
    if n_rows == 1:
        if j == 0:
            neighbors += [m[i][j+1]]
        elif j == (n_cols-1):
            neighbors += [m[i][j-1]]
        else:
            neighbors += [m[i][j+1], m[i][j-1]]
    else:
        if i==0 and j==0:
            neighbors += [m[i][j+1], m[i+1][j], m[i+1][j+1]]
        elif i==(n_rows-1) and j==0:
            neighbors += [m[i][j+1], m[i-1][j], m[i-1][j+1]]
        elif i==0 and j==(n_cols-1):
            neighbors += [m[i][j-1], m[i+1][j], m[i+1][j-1]]
        elif i==(n_rows-1) and j==(n_cols-1):
            neighbors += [m[i-1][j], m[i][j-1], m[i-1][j-1]]
        else:
            if i==0:
                neighbors += [m[i][j-1], m[i][j+1], m[i+1][j-1], m[i+1][j], m[i+1][j+1]]
            elif i==(n_rows-1):
                neighbors += [m[i][j-1], m[i][j+1], m[i-1][j-1], m[i-1][j], m[i-1][j+1]]
            elif j==0:
                neighbors += [m[i+1][j], m[i-1][j], m[i+1][j+1], m[i][j+1], m[i-1][j+1]]
            elif j==(n_cols-1):
                neighbors += [m[i+1][j], m[i-1][j], m[i+1][j-1], m[i][j-1], m[i-1][j-1]]
            else:
                neighbors += [m[i][j-1], m[i-1][j-1], m[i+1][j-1],m[i-1][j], m[i+1][j], m[i][j+1], m[i+1][j+1], m[i-1][j+1]]
    return neighbors.count('o')
# Test handshakes_count_one function
#matrix = [['.','o','o'],['o','o','o'],['.','.','o']] 
#print(handshakes_count_one(1,1,matrix))

def handshakes_count_all(m):
    """
    m: 2 dimensional list, row (i,j) has either character 'o' or '.'

    return total number of handshakes in matrix m
    """
    total = 0
    n_cols = len(m[0])
    n_rows = len(m)
    for i in range(n_rows):
        for j in range(n_cols):
            if m[i][j] == 'o':
                total += handshakes_count_one(i,j,m)
    return total // 2

# Test handshakes_count_all function
#matrix = [['.','o','o'],['o','.','.']] 
#print(handshakes_count_all(matrix))


# Solve the problem
# Get the input
n_rows, n_cols = map(int, input().split(' '))
matrix = []
for i in range(n_rows):
    row = list(input())
    matrix.append(row)

# Set the max number of handshakes to be the number of handshakes before Mirko enters
max_handshakes = handshakes_count_all(matrix)

# Go through the matrix, whenever there is an empty seat, Mirko takes it and update the number of handshakes
temp_handshakes = 0
for i in range(n_rows):
    for j in range(n_cols):
        if matrix[i][j] == '.':
            matrix[i][j] = 'o'
            temp_handshakes = handshakes_count_all(matrix)
            if temp_handshakes > max_handshakes:
                max_handshakes = temp_handshakes
            matrix[i][j] = '.'

print(max_handshakes)

# TODO: This is probably O(n^4) with large coefficient. Find a way to do it more efficiently.
