def solve():
    n=int(input("enter the number : "))
    def Sum_of_n_NaturalNumbers(n):
        Sum = (n*(n+1))/2
        return Sum
    print(Sum_of_n_NaturalNumbers(n))
t=1
t=int(input("enter the number of test cases : "))
for i in range(t):
   solve()
