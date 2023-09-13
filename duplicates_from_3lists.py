Q:you have been given 3 lists. ypur task is to find the duplicates in the  3 lists. write a python program for the same. you can use your own python lists?

Ans:
#lists#
a=[12,45,3,67,12]
b=[45,34,3,56,34]
c=[12,68,90,45,90]

#here we convert lists in to sets bcs sets doesnt allow duplicates

set1=set(a)
set2=set(b)
set3=set(c)

#now finding duplicates amomg 3 sets
set1.intersection(set2,set3)
# here we are converting set in to list#
print("here are the duplicates from 3 lists:",list(set1))

