c=int(input())
d=list(map(int,input().split()))
a1=0
r=[]
for i in range(0,c):
	if(d[i]==i):
		temp=d[i]
		a1=1
		r.append(temp)
		r=sorted(r)
print(*r)

if(a1==0):
	print(-1)
