Q: given a python list[10,501,22,37,100,999,87,351] your task is to count all the prime numbers in it?

Ans:

a=[10,501,22,37,100,999,87,351]
prime=[]
count=0
for i in a:
    for j in range(2,i):
        if i%j==0:
            pass
            break
    if i%j!=0:
            prime.append(i)
print("prime numbers are:",prime)
count=(len(prime))
print("no of prime numbers in prime list:",count)