string=input("enter the string:")
fch=string[0]
nstr=fch
l=len(string)
for i in range(1,l):
    if string[i] == fch:
        nstr += "$"
    else:
        nstr += string[i]
print(nstr)

