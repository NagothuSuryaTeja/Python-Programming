def solve():
    n=int(input("enter the year : "))
    def Leaf_Year(n):
        if(n%400 == 0):
            print("leaf year")
        elif(n%100==0):
            print("not leaf year")
        elif(n%4==0):
            print("leaf Year")
        else:
            print("not leaf year")
    Leaf_Year(n)
t=1
t=int(input("enter the number of test cases : "))
for i in range(t):
   solve()
