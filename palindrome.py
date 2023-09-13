Q:write a function that takes a string And returns true if it is palindrome ,false otherwise?
Ans:

def palindrome(str):
    reverse=str[::-1]
    if (str==reverse):
        print("palindrome")
    else:
        print("not a palindrome")

str=input("enter string: ")
palindrome(str)