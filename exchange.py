string=input("enter the string:")
fch=string[0]
l=len(string)
lch=string[l-1]
mid_string =string[1:l-1]
new_string = lch + mid_string + fch

print(new_string)