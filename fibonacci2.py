n=int(input("enter the number:"))
def fib(n):
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
         return(fib(n-1)+fib(n-2))
if n ==0 or n==1:
    print(fib(n))
else:
    for i in range(n):
        print(fib(i))
#print(fib(n))
