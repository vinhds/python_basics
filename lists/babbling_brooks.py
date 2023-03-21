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

# Retreive input: number of streams and the flow in each of the streams
num_streams = int(input())
flows = []
for i in range(num_streams):
    flow = int(input())
    flows.append(flow)

# Perform split or join on the flows depending on the input
action = int(input())
while action != 77:
    if action == 99:
        flow_loc = int(input())
        flow_loc -= 1
        percentage = int(input())
        # Calculate the percentage of the flow at the split location
        # that flows to the left fork
        left_flow = flows[flow_loc] * percentage / 100
        # The rest flows to the right fork
        right_flow = flows[flow_loc] - left_flow
        # Modify the stream, replace the flow that is split by the left and right forks
        flows = flows[:flow_loc] + [left_flow, right_flow] + flows[(flow_loc + 1):]
    elif action == 88:
        flow_loc = int(input())
        flow_loc -= 1
        # The stream at flow_loc location is joined with the one to its right
        new_flow = flows[flow_loc] + flows[(flow_loc + 1)]
        # Modify the stream, replace the two flows by the combined flow
        flows = flows[:flow_loc] + [new_flow] + flows[(flow_loc+2):]
    action = int(input())
# Print the output
for flow in flows:
    print(round(flow), end=' ')
