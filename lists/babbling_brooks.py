#A series of streams run down the side of a mountain. The mountainside is very rocky so the streams split and rejoin many times.
# At the foot of the mountain, several streams emerge as rivers. Your job is to compute how much water flows in each river.
#
#At any given elevation there are m streams, labelled 1 to m from left-to-right. As we proceed down the mountainside,
#one of the streams may split into a left fork and a right fork, increasing the total number of streams by 1 , or two streams may rejoin,
#reducing the total number of streams by 1 . After a split or a rejoining occurs,
#the streams are renumbered consecutively from left-to-right.
#There is always at least one stream and there are never more than 100 streams.
#Input Specification
#
#The first line of input contains n , the initial nu#mber of streams at some high altitude.
#The next n lines give the flow in each of the streams from left-to-right. Proceeding down the mountainside,
#several split or rejoin locations are encountered. For each split location, there will be three lines of input.
#
#    a line containing 99 (to indicate a split)
#    a line containing an integer, the number of the# stream that is split
#    a line containing an integer between 0 and 100 #, the percentage of flow from the split stream that flows to the left fork.
#(The rest flows to the right fork)
#
#For each join location, there will be two lines of #input:
#
#    a line containing 88 (to indicate a join)
#    a line containing an integer, the number of the# stream that is rejoined with the stream to its right
#
#The flow from both joined streams is combined. Afte#r the last split or join location will be:
#
#    a single line containing 77 (to indicate end of# input)
#
#Output Specification
#
#Your job is to determine how many streams emerge at# the foot of the mountain and what the flow is in each.
#Your output is a sequence of real numbers, rounded to the nearest integer, giving the flow in rivers 1 through m .
