Q:create proper member variables inside the task if required and use them when necessary.for ex. for this task create class private variable named pi=3,141?


Ans:

class circle():
    __pi=3.141
    def __init__(self,n):
        self.n=n
    def area(self,radius):
        return circle.__pi*(radius**2)
    def circumference(self,radius):
        return 2*circle.__pi*radius

#creating object and passing list as parameter
cir_obj=circle([10,501,22,37,100,999,87,351])

#accessing each element from list
result= cir_obj.n
print(result)

#declaring radius variable
radius=5
