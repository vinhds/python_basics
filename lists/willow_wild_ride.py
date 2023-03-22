#Mandy is a working artist and is commissioned to create some art pieces for 2018.
#The client wants Mandy to create art pieces out of cardboard boxes to display at the local art show.
#Occasionally, Mandy plans to drive by the local store on her way home to grab some boxes for her art pieces.
#
#Mandy's cat, Willow, likes to play with every box that Mandy brings home. Willow plays with a box for T days before getting bored of it. Once Willow is bored with a box, she never returns to it again, meaning that Mandy can finally use the empty box in her art projects.
#
#If Mandy brings home another box before Willow finishes playing with the previous one,
#Willow will wait until she is bored with the previous box before moving onto the new one.
#
#Given Mandy's box-shopping habits over the next N days, can you determine by how many days the project will be delayed due to Willow?
#Input Specification
#
#The standard input will contain 10 datasets.
#
#Each dataset begins with two integers T ( 2 ≤ T ≤ 7 ) and N ( 1 ≤ N ≤ 365 ) .
#The next N lines each contain either the letter E or B which represent whether Mandy came home empty-handed or with a box that day.
#Output Specification
#
#For each dataset, output the number of days that Willow will be playing with the boxes after the N days given in the dataset.

# Get the input
for i in range(10):
    first_line = input()
    t, n = map(int, first_line.split(' '))
    mandy_actions = []
    for i in range(n):
        action = input()
        mandy_actions.append(action)
    next_day = 0
    for i in range(len(mandy_actions)):
        if mandy_actions[i] == 'B':
            if i <= next_day:
                next_day += t
            elif i > next_day:
                next_day = i + (t - 1) 
    if next_day <= len(mandy_actions) - 1:
        print(0)
    else:
        print(next_day - len(mandy_actions) + 1)













