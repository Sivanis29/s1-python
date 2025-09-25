numbers=input("enter integers:")
numbers=[int(num) for num in numbers.split()]
list=["over" if num>100 else num for num in numbers]
print(list)