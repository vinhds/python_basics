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
n_plus = change.count('+')
n_minus = change.count('-')
max_change = max([n_plus, n_minus])
max_row = abs(n_plus - n_minus)
draw_locs = []
draw_chars = []
for i in range(n_days):
    begin_net_worth = end_net_worth
    if change[i] == '+':
        loc = (max_row - begin_net_worth, i)
        end_net_worth = begin_net_worth + 1
        draw_chars.append('/')
    elif change[i] == '-':
        end_net_worth = begin_net_worth - 1
        loc = (max_row - end_net_worth, i)
        draw_chars.append('\\')
    else:
        loc = (max_row - begin_net_worth, i)
        end_net_worth = begin_net_worth
        draw_chars.append('_')
    draw_locs.append(loc)
print(draw_locs)
print(draw_chars)
print(max_row)
print(n_days)
print(max_change)
for j in range(max_change):
    for i in range(n_days):
        if (j,i) not in draw_locs:
            print('.',end='')
        else:            
            loc = draw_locs.index((j, i))
            print(draw_chars[loc],end='')
    print('\n')            
