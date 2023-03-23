#Tusk has been stranded on an island for some time now, and it's fair to say that he's grown terribly bored.
#As such, he's started to find ordinary things immensely fascinating.
#
#Today, he's interested in the waves he sees. He notes that at certain times of
# the day, the water level either increases or decreases.
# Realizing this phenomenon is due to tides, he is now most fervent about determining the difference in water level
#between high tide and low tide.
#
#To this end, he's measured the water level N times throughout the day using a high-precision measuring device
#such that each reading is a unique integer in the range 1 … 10 000 inclusive.
#
#He knows that after measuring the absolute minimum reading at low tide,
#the transition to the absolute maximum reading representing the water level at high tide
#consists of a strictly increasing sequence of water level readings. He's interested in the difference
#between the absolute maximum and absolute minimum readings: the water level difference between tides.
#
#It's possible that he made a mistake in writing down these readings, however,
#in which case the sequence between the low tide reading and high tide reading will not be strictly increasing.
#If this is the case, it's likely that the data is useless — the water level difference cannot be accurately determined —
#and should be scrapped.
#Input Specification
#
#The first line will contain the single integer N ( 3 ≤ N ≤ 1 000 ) .
#
#The second line will contain N space-separated positive integers: the water level readings in chronological order.
#Output Specification
#
#The integer difference in water level between high tide and low tide. If the difference cannot be accurately determined, output unknown.
# Get the input
n_measures = int(input())
second_line = input()
measures = list(map(int, second_line.split(' ')))
check = True
min_measure = min(measures)
min_loc = measures.index(min_measure)
max_measure = max(measures)
max_loc = measures.index(max_measure)
# This is when the max location happens before the min location
if max_loc < min_loc:
    end_loc = len(measures) - 1
else:
    end_loc = max_loc
# Check to see whether the transition from min to max follows an 
# increasing sequence
for i in range(min_loc, end_loc):
    if measures[i] > measures[i+1]:
        check = False
        break
if check == True:
    difference = max_measure - min_measure
    print(difference)
else:
    print('unknown')

