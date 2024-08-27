import math as maths
def primenumbers():
    n=int(input())
    if(n == 1 or n == 0):
        print(f"{n} is neither prime nor composite")
        return n
    for i in range(2,int(maths.sqrt(n))+1):
        if(n%i==0):
            print("not prime")
            return n
    print("prime")
    return n
t=1
t=int(input("enter the number of test cases : "))
for i in range(t):
    primenumbers()