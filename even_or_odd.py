Q. You have been given a python list [10,501,22,37,100,999,87,351] your task is to create two lists one which have all the even numbers and another list which will have all the odd numbers in it?
Ans:

# Given list#
a=[10,501,22,37,100,999,87,351]
#initializing empty lists for even and odd#
even=[]
odd=[]
#iterating through the a#
for i in a:
#applying condition to get even and odd numbers#
    if i%2==0:
# adding(appending) even numvers to the empty even list#
        even.append(i)
    else:
#adding (appending) odd numbers to the empty odd list#
        odd.append(i)

#printing the outputs for given list,even list and odd list#
print("The given list is:",a)
print("even numbers:" ,even)
print("odd numbers:" ,odd)