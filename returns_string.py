Q: write a function that takes a string and returns a new string with all the vowels removed?

Ans:

def return_string(str):
    str1=str.upper()
    print("string with vowels:",str1)
    str2=' '
    vowels="AEIOUaeiou"
    for i in str1:
        if i not in vowels:
            str2+=i
    print("string  with all the vowels removed:", str2)
return_string("I Am Beginner For Python")
