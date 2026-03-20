import area_module

base=int(input("enter base :: "))
height=int(input("enter height :: "))
print("Area of Triangle is :: ",area_module.areaoftriangle(base,height))

radius=float(input("Enter Radius :::"))
print("Area of circle is :: ",area_module.areaofcircle(radius))


side=int(input("Enter Side :::"))
print("Area of square is :: ",area_module.areaofsquare(side))

length=int(input("enter length :: "))
breadth=int(input("enter breadth :: "))
print("Area of Rectnagle is :: ",area_module.areaofrectnagle(length,breadth))