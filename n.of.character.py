text=input("enter the string:")
dic={}
for char in text:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1
print("character frequency:")
for key,value in dic.items():
    print(key, ":" , value)