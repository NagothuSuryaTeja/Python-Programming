def factorial():
   n=int(input())
   def recursion(n):#factorial function
    if(n==0 or n==1):
      return 1
    return n*recursion(n-1)
   print(recursion(n))
t=1
t=int(input("enter the number of test cases : "))
for i in range(t):
   factorial()