#Lena has n boxes, numbered from 1 to n. Box number i contains ki action figures, each of its own size aij.
#Lena wants to finish quickly, but it’s very important to put all the figures in a non-decreasing order by their size.
#If it’s impossible, then the cleaning cannot be finished at all. Lena has quite a lot of boxes, so she isn’t sure if it can be done.
#Lena values her boxes with action figures a lot, and she would never open one, because that would require to tear the wrapping.
#She also enjoys admiring all the figures, and the boxes only have one clear side, so putting a box back to front is out of question.
#Help Lena to see if she could tell mom that cleaning cannon be finished,
#or if it’s possible and she has to arrange the boxes on the shelf anyway.
#Input
#The first line contains one integer n — the amount of boxes with action figures (1 ≤ n ≤ 100).
#Each of next n lines contains a integer ki — amount of figures in i-th box (1 ≤ ki ≤ 100),
#followed by ki integers aij — sizes of action figures in order from left to right (1 ≤ aij ≤ 104).
#Integers in one line are separated with spaces.
#Output
#Print “YES” (without quotes), if boxes can be arranged in such a way that action figues would be in a non-decreasing order by their size. Otherwise, print “NO” (without quotes).

# Plan: 
# 1. Check if each box is sorted in non-decreasing order. If not, return NO.
# 2. Store the content of each box in non-decreasing order.
# For any two boxes i and j, if max_i <= min_j or min_i >= max_j, it means they can be ordered. Otherwise, immediately return NO. 
# 4. Store in 3 lists: box_list, content_list, extrema_list
# Challenge: what if all items in a box have the same height.

n_boxes = int(input())
boxes = []
all_content = []
extrema = []
check = True
for box in range(n_boxes):
    line = list(map(int, input().split(' ')))
    boxes.append(line[0])
    content = line[1:]
    sorted_content = sorted(content)
    if content != sorted_content: 
        check = False
    else:
        all_content.append(sorted_content)
        extrema.append([sorted_content[0], sorted_content[-1]])

print(boxes)
print(all_content)
print(extrema)

if check == True:
    for i in range(n_boxes):
        if i < n_boxes - 1:
            for j in range(i+1, n_boxes):
                if not ((extrema[i][1] <= extrema[j][0]) or (extrema[i][0] >= extrema[j][1])):
                    check = False
                    break
if check == True:
    print('YES')
else:
    print('NO')
                        
