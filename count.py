line=input("enter the line:")
words=line.split()
d= {}
for word in words:
     if word in d:
         d[word ]+= 1
     else:
         d[word]= 1

print(d)