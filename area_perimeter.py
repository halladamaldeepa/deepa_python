Q:from the given list create 2 class methods area and perimeter which will be going to calculate the area and radius?


Ans:

class circle:
    __pi=3.141
    def __init__(self,n):
        self.n=n
    @classmethod
    def area(cls,radius):
        return cls.__pi*(radius**2)

    @classmethod
    def perimeter(cls,radius):
        return 2*cls.__pi*radius

cir_obj=circle([10,501,22,37,100,999,87,351])
result=cir_obj.n
print(result)

radius=7
area=cir_obj.area(radius)
perimeter=cir_obj.perimeter(radius)
print("Area of circle is:",area)
print("Perimeter of circle is:",perimeter )