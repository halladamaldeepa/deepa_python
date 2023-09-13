Q:write a python program to find the sum of the first and last digit of an iteger?

Ans:

#defining function#
def first_last(n):
    #converting integer in to string#
    num_str=str(n)
    #storing index number of digit in to variables
    first_digit=int(num_str[0])
    last_digit=int(num_str[-1])
    #adding digits#
    return first_digit+last_digit

# taking input from user#
int_ip=int(input("enter integer: "))
#storing output in to the result#
result= first_last(int_ip)
#printing result#
print("sum of first and last digit is:" ,result)