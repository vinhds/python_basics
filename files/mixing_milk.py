
#Farming is competitive business -- particularly milk production. Farmer John figures that if he doesn't innovate in his milk production methods, his dairy business could get creamed!
#
#Fortunately, Farmer John has a good idea. His three prize dairy cows Bessie, Elsie, and Mildred each produce milk with a slightly different taste, and he plans to mix these together to get the perfect blend of flavors.
#
#To mix the three different milks, he takes three buckets containing milk from the three cows. The buckets may have different sizes, and may not be completely full. He then pours bucket 1 into bucket 2, then bucket 2 into bucket 3, then bucket 3 into bucket 1, then bucket 1 into bucket 2, and so on in a cyclic fashion, for a total of 100 pour operations (so the 100th pour would be from bucket 1 into bucket 2). When Farmer John pours from bucket a
#into bucket b, he pours as much milk as possible until either bucket a becomes empty or bucket b
#
#becomes full.
#
#Please tell Farmer John how much milk will be in each bucket after he finishes all 100 pours.
#
#INPUT FORMAT (file mixmilk.in):
#The first line of the input file contains two space-separated integers: the capacity c1
#of the first bucket, and the amount of milk m1 in the first bucket. Both c1 and m1 are positive and at most 1 billion, with c1≥m1
#. The second and third lines are similar, containing capacities and milk amounts for the second and third buckets.
#
#OUTPUT FORMAT (file mixmilk.out):
#Please print three lines of output, giving the final amount of milk in each bucket, after 100 pour operations. 

# Plan:
# 1. Write a function pour that takes two buckets, represented by two tuples (c_1, m_1) and (c_2, m_2)
# and return the new status of each bucket.
# 2. Loop 100 times and to keep applying the pour function.

def pour(c_1, m_1, c_2, m_2):
    """
    c_1, m_1, c_2, m_2 are the capacities and amounts of milk for the two buckets

    Return the new amounts of milk of the buckets after pouring 
    """
    if m_1 <= c_2 - m_2:
        m_2 += m_1
        m_1 = 0
    else:
        m_1 -= c_2 - m_2
        m_2 = c_2
    return m_1, m_2

# Check the pour function
#a, b = pour(12,12, 10, 0)
#print(a)
#print(b)

def input_reader(file_name):
    """
    file_name is a string that corresponds to the input file

    Return two lists: buckets is a list that contains the amounts of milk in the buckets
    capacities is a list that contains the capacities of the buckets
    """
    buckets = []
    capacities = []
    input_file = open(file_name, 'r')
    for line in input_file:
        bucket = line.rstrip().split(' ')
        buckets.append(int(bucket[1]))
        capacities.append(int(bucket[0]))
    input_file.close()
    return buckets, capacities

# Check the input_reader function
#file_name = 'mixing_milk_files/1.in'
#print(input_reader(file_name))

# Solve the problem
file_name = 'mixmilk.in'
buckets, capacities = input_reader(file_name)
i = 0
while i < 100:
    indx_1 = i % 3
    indx_2 = (i+1) % 3
    c_1 = capacities[indx_1]
    c_2 = capacities[indx_2]
    m_1 = buckets[indx_1]
    m_2 = buckets[indx_2]
    buckets[indx_1], buckets[indx_2] = pour(c_1, m_1, c_2, m_2)
    i += 1
#print(buckets)

output_file = open('mixmilk.out', 'w')
for i in range(len(buckets)):
    output_file.write(str(buckets[i]))
    output_file.write('\n')
output_file.close()



