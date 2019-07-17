ar=int(input())
pt=[]
for i in range(ar):
  ass=input()
  pt.append(ass)
ma1=min(pt,key=len)
pt.remove(ma1)
for i in range(len(ma1)):
  for j in range(len(pt)):
     ba1=pt[j]
     if ma1[:i+1]==ba1[:i+1]:
       result=ma1[:i+1]
     else:
       break
print(result)
