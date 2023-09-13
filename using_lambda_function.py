Q: write a python program using lambda function to check every element of a list is an integer or string?

Ans:

a=[10,501,22,37,100,999,87,351]
result=list(map(lambda x:isinstance(x,(int,str)),a))
print(result)
