#You might be surprised to know that 2013 is the first year since 1987 with distinct digits.
#The years 2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits.
#2012 does not have distinct digits, since the digit 2 is repeated.
#
#Given a year, what is the next year with distinct digits?
#Input Specification
#
#The input consists of one integer Y ( 0 ≤ Y ≤ 10 000 ), representing the starting year.
#Output Specification
#
#The output will be the single integer D , which is the next year after Y with distinct digits.

start_year = int(input()) 

def check_year(year):
    year = str(year)
    check = False
    for digit in year:
        if year.count(digit) > 1:
            check = True
            break
    return check

while True:
    start_year += 1
    if check_year(start_year) == False:
        break
print(start_year)
