#Farmer John has lost his prize cow Bessie, and he needs to find her!
#
#Fortunately, there is only one long path running across the farm, and Farmer John knows that Bessie has to be at some location on this path. If we think of the path as a number line, then Farmer John is currently at position x
#And Bessie is currently at position y (unknown to Farmer John). If Farmer John only knew where Bessie was located, he could walk directly to her, traveling a distance of |x−y|
#
#. Unfortunately, it is dark outside and Farmer John can't see anything. The only way he can find Bessie is to walk back and forth until he eventually reaches her position.
#
#Trying to figure out the best strategy for walking back and forth in his search, Farmer John consults the computer science research literature and is somewhat amused to find that this exact problem has not only been studied by computer scientists in the past, but that it is actually called the "Lost Cow Problem" (this is actually true!).
#
#The recommended solution for Farmer John to find Bessie is to move to position x+1
#, then reverse direction and move to position x−2, then to position x+4, and so on, in a "zig zag" pattern, each step moving twice as far from his initial starting position as before. As he has read during his study of algorithms for solving the lost cow problem, this approach guarantees that he will at worst travel 9 times the direct distance |x−y|
#
#Between himself and Bessie before he finds her (this is also true, and the factor of 9 is actually the smallest such worst case guarantee any strategy can achieve).
#
#Farmer John is curious to verify this result. Given x
#And y
#
#, please compute the total distance he will travel according to the zig-zag search strategy above until he finds Bessie.
#
#INPUT FORMAT (file lostcow.in):
#The single line of input contains two distinct space-separated integers x
#And y. Both are in the range 0…1,000
#.
#
#OUTPUT FORMAT (file lostcow.out):
#Print one line of output, containing the distance Farmer John will travel to reach Bessie. 

# Plan:
# Have a way to check whether farmer John has passed Bessie's location or not
# While the farmer has not passed the cow, keep the farmer moving and have
# variables keeping track of his current location and the total distance he moved

file_name = 'lostcow.in'
input_file = open(file_name, 'r')
line = input_file.readline().rstrip().split(' ')
farmer_loc = int(line[0])
cow_loc = int(line[1])
input_file.close()
#print(farmer_loc)
#print(cow_loc)
original_dist = cow_loc - farmer_loc
current_dist = original_dist
current_loc = farmer_loc
i = 0
total_dist = 0
prev_loc = 0
while current_dist * original_dist > 0:
    displacement = 2**i
    prev_loc = current_loc 
    if i % 2 == 0:
        current_loc = farmer_loc + displacement
    else:
        current_loc = farmer_loc - displacement
    total_dist += abs(current_loc - prev_loc)
    current_dist = cow_loc - current_loc
    i += 1
output_file = open('lostcow.out', 'w')
output_file.write(str(total_dist - abs(current_dist)))
output_file.close()
