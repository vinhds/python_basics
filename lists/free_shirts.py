#Throughout the year, there are many programming events that students can attend to meet like-minded individuals,
#hone their skills and, most importantly, get a free t-shirt.
#
#Ian is an avid attender of these events because he hates doing laundry. Ian only does his laundry when all his shirts are dirty,

#
#Ian starts with N clean shirts. Ian wears one clean shirt every day, after which it becomes dirty.
#If at the beginning of a day (before any events) Ian only has dirty shirts, then he will do the laundry,
#which makes all his shirts clean again. If Ian goes to an event, then he will receive one clean shirt.
#
#Given the initial number of shirts that Ian has and the schedule of events for the next D days,
#how many times will Ian do the laundry in the next D days?
#Input Specification
#
#The input contains 10 datasets. Each dataset begins with three integers N , M , D ( 1 ≤ N , M ≤ 100 , 1 ≤ D ≤ 1 000 )
#, the initial number of shirts that Ian has, the number of events coming up, and the number of days, respectively.
#
#The next line contains M integers A i ( 1 ≤ A i ≤ D ) , the days on which there are events.
#There may be multiple events in a single day.
#Output Specification
#
#For each dataset, output the number of times that Ian will do the laundry in the next D days.

# Get the input
for j in range(10):
    first_line = input()
    n, m, d = map(int, first_line.split(' '))
    event_days = []
    second_line = input()
    event_days = list(map(int, second_line.split(' ')))
    n_clean_shirts = n
    laundry = False
    n_laundry = 0
# For each day:
# Count the number of free t-shirts based on the number of events
# Update the total number of shirts, the number of clean shirts
# Make the laundry decision based on the number of clean shirts
# Keep track of the number of laundries done
    for i in range(d):
        n_free_shirts = event_days.count(i+1)
        n += n_free_shirts
        if n_clean_shirts == 0:
            laundry = True
            n_laundry += 1
        elif n_clean_shirts > 0:
            laundry = False
        if laundry == True:
            n_clean_shirts = n
        elif laundry == False:
            n_clean_shirts += n_free_shirts        
        n_clean_shirts -= 1
    print(n_laundry)
