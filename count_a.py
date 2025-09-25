names=["shikha" "sivani" "nandhana"]
count_a=0
for name in names:
    for ch in name:
        if ch=='a' or ch=='A':
            count_a+=1
print("occuarence of a:",count_a)