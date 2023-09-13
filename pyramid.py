Q: create pyramid of numbers from 1 to 20 using for loop?

Ans:
num=20
for i in range(num):
    for j in range(i,num):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()