Q: using the python lambda function  create a fibonacci series from 1 to 50 elements?

Ans:

fib=lambda n: n if n<=1 else fib(n-1)+fib(n-2)
n=10
for i in range(n):
    print(fib(i))