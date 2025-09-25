l1=[1,2,3,4,5]
l2=[2,4,6,8]
print("elements of first list is:",l1)
print("elements of secont list is",l2)
if len(l1) == len(l2):
    print("list have some list")
else:
    print("list have different length")
s1=0
s2=0
for i in range(len(l1)):
    s1 = s1 + l1[i]
print("sum of first list",s1)
for i in range(len(l2)):
    s2 = s2 + l2[i]
print("sum of first list",s2)
if s1 == s2:
    print("list of sum is some")
else:
    print("list of sum is different")
print("the common elements is:")
for i in l1:
    for j in l2:
        if i == j:
            print(i)