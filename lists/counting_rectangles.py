#While playing in his favourite text editor, Daniel decided to draw a picture that was N characters high and M characters wide.
#The picture consists solely of characters . and * such that characters * form some non-overlapping rectangles.
#The rectangles don't even touch each other on their sides or corners.
#
#Help Daniel count the number of rectangles drawn on the picture.
#Input
#
#The first line contains two integers N and M ( 1 ≤ N , M ≤ 100 ) from task description.
#
#Each of the next N lines contains M characters . or * which represent the picture that Daniel drew.
#Output
#
#In a single line you should output the number of rectangles on the picture.
#Scoring
#
#In the test cases worth a total of 20 % of the points, all rectangles will consist of a single * character.
#
#In the test cases worth additional 30 % of the points, it will hold N = 1 .



# Hint: The number of rectangles in the image is equal to the number of upper-left corners of rectangles in the image.
# Cell ( i , j ) is an upper-left corner of some rectangle if that cell contains the character *
# while cells ( i − 1 , j ) and ( i , j − 1 ) (if they exist) contain the character ..

n, m = map(int, input().split(' '))
picture = []
n_rectangles = 0
for i in range(n):
    line = input()
    picture.append(line)
for i in range(n):
    for j in range(m):
        if i >= 1 and j >= 1:
            if picture[i][j] == '*' and picture[i-1][j] == '.' and picture[i][j-1] == '.':
                n_rectangles += 1
        elif i == 0:
            if j == 0:
                if picture[i][j] == '*':
                    n_rectangles += 1
            else: 
                if picture[i][j] == '*' and picture[i][j-1] == '.':
                    n_rectangles += 1
        else:
            if picture[i][j] == '*' and picture[i-1][j] == '.':
                n_rectangles +=1  

print(n_rectangles)

