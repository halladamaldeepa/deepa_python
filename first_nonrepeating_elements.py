Q: write a python program to find the first non-repeating elements in a given of integer?

Ans:

def first_non_repeating_element(arr):
#create dictionary to store the frequency of each element
    element={}
#iterate through the list to count element frequencies
    for i in arr:
        if i in element:
            element[i]+=1
        else:
            element[i]=1
#iterating through the list again to find the first non repeating element
    for i in arr:
        if element[i]==1:
            return i
#if no nonrepeating element is found,retun None
    return None

my_list=[2,7,3,4,2,4,5,6]
result=first_non_repeating_element(my_list)

if result is not None:
    print("the first non-repeating element is:",result)
else:
    print("There are no repeating elements in the list")


