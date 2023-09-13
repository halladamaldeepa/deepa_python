Q: write a python program to calculate total no of vowels and count of each individual vowels A,E,I,O,U in the string "Guvi Geeks Private Limited" ?

Ans:

data="Guvi Geeks Private Limited"
string=data.upper()
count=0
list1=["A","E","I","O","U"]
for i in string:
    if i in list1:
        count=count+1
print("Total no of vowels are: ", count)