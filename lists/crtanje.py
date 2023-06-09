#Josip used to code in Logo. He loved to draw pictures, but those days are sadly over.
#Nostalgic, he decided to draw a line that represents the net worth of his company over a period of n days.
#
#For each of the n days, he knows if the net worth of his company increased by one unit (represented by +),
#decreased by one unit (represented by -), or remained the same (represented by =) during that day.
#Before the first day, the net worth was equal to zero.
#
#Josip will draw the line in a big infinite matrix of characters. Indices of matrix rows grow upwards,
#and indices of columns grow to the right. For the i -th day he will draw some character in the i -th column.
#
#The character and the index of the row are decided by the following rules:
#
#    If the net worth increased during the i -th day, he will draw /
#    in the row with index equal to the net worth at the beginning of the day.
#    If the net worth decreased during the i -th day, he will draw \
#            in the row with index equal to the net worth at the end of the day.
#    If the net worth didn't change during the i -th day, he will draw _ in the row with index equal to the net worth during the day.
#
#All other cells are filled with ..
#
#Your task is to output the minimal matrix that contains the whole line, i.e. contains all characters /, \ and _ that Josip drew.
#Input
#
#The first line contains an integer n ( 1 ≤ n ≤ 100 ) , the number of days.
#
#The second line contains a string of n characters +, - and = that represents how the company's net worth changed over the given period.
#Output
#
#Output the described matrix.

# Get the input
n_days = int(input())
change = input()
begin_net_worth = 0
end_net_worth = 0
# Keep a list of location of '/', '\' and '_' based on the change in net_worth: store in locs
locs = []
# Modify each element of locs to get the actual location that we need to draw: store in draw_locs
draw_locs = []
# List of what to draw: draw_chars
draw_chars = []
# Need to x_coordinates of locs to find the max. This is to obtain draw_locs 
x_locs = []
for i in range(n_days):
    # Compute the end of day net_worth and initial location based on what happens during that day
    begin_net_worth = end_net_worth
    if change[i] == '+':
        loc = (begin_net_worth, i)
        end_net_worth = begin_net_worth + 1
        draw_chars.append('/')
    elif change[i] == '-':
        end_net_worth = begin_net_worth - 1
        loc = (end_net_worth, i)
        draw_chars.append('\\')
    else:
        loc = (begin_net_worth, i)
        end_net_worth = begin_net_worth
        draw_chars.append('_')
    locs.append(loc)
    x_locs.append(loc[0])    
max_x = max(x_locs)    
x_draw_locs = []
# Now modify the coordinates in locs to obtain the coordinates where we need to make the drawing.
for i in range(n_days):
    draw_loc = (max_x - locs[i][0], locs[i][1])
    x_draw_locs.append(draw_loc[0])
    draw_locs.append(draw_loc)
# This is to ensure we draw the minimal number of ncessary rows
num_rows = max(x_draw_locs)
# Go each entry of the matrix and make the drawing
for j in range(num_rows+1):
    for i in range(n_days):
        if (j,i) not in draw_locs:
            print('.',end='')
        else:            
            loc = draw_locs.index((j, i))
            print(draw_chars[loc],end='')
    print('\n')

    
