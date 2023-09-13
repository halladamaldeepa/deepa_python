Q:create a python class called circle with constructor which will take a list as an argument for the tak. the list is [10,501,22,37,100,999,87,351]?

Ans:
 
#creating class for circle
class circle():
    def __init__(self,n): #n will be a local variable and we are storing n to the class variable
        self.n=n


#creating object for circle which accepta list as argument
cir_obj= circle([10,501,22,37,100,999,87,35])

#here it will access the each element of cir_obj object
result=cir_obj.n

print("The elements of circle are",result)
