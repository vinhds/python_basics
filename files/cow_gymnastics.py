#In order to improve their physical fitness, the cows have taken up gymnastics! Farmer John designates his favorite cow Bessie to coach the N other cows and to assess their progress as they learn various gymnastic skills.
#
#In each of K
#practice sessions (1≤K≤10), Bessie ranks the N cows according to their performance (1≤N≤20
#
#). Afterward, she is curious about the consistency in these rankings. A pair of two distinct cows is consistent if one cow did better than the other one in every practice session.
#
#Help Bessie compute the total number of consistent pairs.
#
#INPUT FORMAT (file gymnastics.in):
#The first line of the input file contains two positive integers K
#and N. The next K lines will each contain the integers 1…N in some order, indicating the rankings of the cows (cows are identified by the numbers 1…N). If A appears before B in one of these lines, that means cow A did better than cow B
#.
#
#OUTPUT FORMAT (file gymnastics.out):
#Output, on a single line, the number of consistent pairs. 

# Plan
# Create a list that contains the ranking of all the practice sessions
# For each pair of cows (i, j), go through the list of results and determine
# whether i always did better than j or j always did better than i

def input_reader(file_name):
    input_file = open(file_name, 'r')
    first_line = input_file.readline().rstrip().split(' ')
    num_cows = int(first_line[1])    
    num_practices = int(first_line[0])
    practices = []                                                                                         
    for i in range(num_practices):
        line = list(map(int,input_file.readline().rstrip().split(' ')))
        practices.append(line)
    input_file.close()
    return num_cows, num_practices, practices

file_name = 'gymnastics.in'
num_cows, num_practices, practices = input_reader(file_name)
#print(practices)
count = 0
check_list = []
for i in range(num_cows-1):
    for j in range(i+1, num_cows):
        for k in range(num_practices):
            if practices[k].index(i+1) < practices[k].index(j+1):
                check_list.append(0)
            else:
                check_list.append(1)
        #print(f'This is the result of practice session: {practices[k]}')
        #print(f'The pair is ({i}, {j})')
        #print(check_list)
        #print(sum(check_list))
        if sum(check_list) == 0 or sum(check_list) == num_practices: 
            count += 1
        check_list = []
output_file = open('gymnastics.out', 'w')
output_file.write(str(count))
output_file.close()
                                                                                         
                                                                                         
                                                                                         




    
