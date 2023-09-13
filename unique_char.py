Q:write a function that takes a string and returns a no of unique character in it?

Ans:


def unique_char(string):
    print(string)

str=input("enter string:")
string=set(str)

unique_char(string)
print(len(string))