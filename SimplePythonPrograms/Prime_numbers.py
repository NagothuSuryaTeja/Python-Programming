import math as maths
def primenumbers():
    n=int(input())
    print('root :', int(maths.sqrt(n)))
    if(n==1):
        print("1 is neither prime nor composite")
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