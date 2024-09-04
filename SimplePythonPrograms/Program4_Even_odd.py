def solve():
    n=int(input("enter the number : "))
    def Even_odd(n):
        if(n%2==0):
            print("Even")
        else:
            print("odd")
    Even_odd(n)
t=1
t=int(input("enter the number of test cases : "))
for i in range(t):
   solve()
