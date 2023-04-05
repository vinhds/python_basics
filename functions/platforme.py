#A level is being designed for a new platform game. The locations of the platforms have been chosen.
#Contrary to popular opinion, platforms can't float in the air, but need pillars for support.
#More precisely, each of the two ends of the platform needs to be supported by a pillar standing on the floor or on a different platform.
#
#You will be given the locations of the platforms in a coordinate system as in the left image below.
#Each platform's location is determined by its altitude (vertical distance from the ground)
#and the start and end coordinates in the horizontal direction.
#Each support pillar is placed half a unit from the end of a platform, as in the right image.
#
#Determine the total length of pillars needed to support all the platforms.
#Input Specification
#
#The first line contains the integer N , 1 ≤ N ≤ 100 , the number of platforms.
#Each of the following N lines contains the position of one platform, three coordinates Y , X 1 and X 2 .
#
#The first number is the altitude, the other two the horizontal coordinates.
#All coordinates will be positive integers less than 10 000 satisfying X 2 > X 1 + 1
#(i.e. the length of each platform will be at least 2 ).
#
#The input will be such that no two platforms overlap.
#Output Specification
#
#Output the total length of pillars needed to support all the platforms.


