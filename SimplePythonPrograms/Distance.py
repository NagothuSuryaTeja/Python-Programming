#Basic Python Programming
from math import *
#Distance
def distance():
    x1=int(input("Enter first point coordinate (x1) : "))
    y1=int(input("Enter first point coordinate (y1) : "))
    x2=int(input("Enter first point coordinate (x2) : "))
    y2=int(input("Enter first point coordinate (y2) : "))
    dist=sqrt(((x2-x1)**2)+((y2-y1)**2))
    print(dist)
    return dist
#Test cases
t=1
t=int(input("enter the number of test cases : "))
for i in range(t):
    distance()