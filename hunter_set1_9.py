var1=int(input())
lis1=list(map(int,input().split()))
pr1=len(lis1)
max1=max(lis1)
m,n=0,0
for i in range(0,pr1-1):
 for j in range(i+1,pr1):
  if abs(lis1[i]+lis1[j])< max1:
   m,n=lis1[i],lis1[j]
   max1=abs(m+n)
print(m, n)
