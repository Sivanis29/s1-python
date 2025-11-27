class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area (self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.breadth + self.length)

l1=int(input("Enter length of first rectangle"))
b1 = int(input("Enter breadth of first rectangle"))
r1 = Rectangle (l1,b1)
print("area of first rectangle=",r1.area())
print("perimeter of rectangle=",r1.perimeter())

l2=int(input("Enter length of secont rectangle"))
b2 = int(input("Enter breadth of secont rectangle"))
r2 = Rectangle (l2,b2)
print("area of secont rectangle=",r2.area())
print("perimeter of secont rectangle=",r2.perimeter())
a1=r1.area()
a2=r2.area()
if a1>a2:
    print("area of first rectangle is greater")
elif a1==a2:
    print("area of  rectangle is eqal")
else:
    print("area of secont rectangle is grater")



