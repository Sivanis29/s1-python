num=int(input("enter number:"))
a=0
b=1
print("fibonacci series:")

for i in range(num):
    print(a , end=" ")
    a , b = b, a + b