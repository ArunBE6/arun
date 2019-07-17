arr,buy=input().split()
for i in arr:
    cod=arr.count(i)
for j in buy:
    dot=buy.count(j)
if cod==dot:
    print("yes")
else:
    print("NO")
