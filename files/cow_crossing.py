#As part of the study, Farmer John has been asked to document the number of times each of his cows crosses the road. He carefully logs data about his cows' locations, making a series of N observations over the course of a single day. Each observation records the ID number of a cow (an integer in the range 1…10
#
#, since Farmer John has 10 cows), as well as which side of the road the cow is on.
#
#Based on the data recorded by Farmer John, please help him count the total number of confirmed crossings. A confirmed crossing occurs when a consecutive sightings of a cow place it on different sides of the road.
#
#INPUT FORMAT (file crossroad.in):
#The first line of input contains the number of observations, N
#, a positive integer at most 100. Each of the next N
#lines contains one observation, and consists of a cow ID number followed by its position indicated by either zero or one (zero for one side of the road, one for the other side).
#
#OUTPUT FORMAT (file crossroad.out):
#Please compute the total number of confirmed crossings. 

def input_reader(file_name):
    """
    file_name is a string which corresponds to the name of the input file
    
    Return two lists: a list of cow IDs and a list of the positions of the cows
    """
    cow_IDs = []
    positions = []
    input_file = open(file_name, 'r')
    for line in input_file:
        cow = line.rstrip().split(' ')
        if len(cow) == 2:
            cow_IDs.append(int(cow[0]))
            positions.append(int(cow[1]))
    input_file.close()
    return cow_IDs, positions

file_name = 'crossroad.in'
#print(input_reader(file_name))
cow_IDs, positions = input_reader(file_name)
black_list = []
count = 0
num_cows = len(cow_IDs)
for i in range(num_cows-1):
    for j in range(i+1, num_cows):
        if (cow_IDs[j] == cow_IDs[i]) and (i not in black_list) and (j not in black_list): 
            if positions[i] != positions[j]:
                count += 1
                black_list.append(i)
                black_list.append(j)
                break
            else: 
                black_list.append(i)
                break
#print(count)
output_file = open('crossroad.out', 'w')
output_file.write(str(count))
output_file.close()


