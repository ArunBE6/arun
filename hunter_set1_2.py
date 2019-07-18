a=int(input())
b=[]
for i in range (0,a):
	b.append(input())
l=len(b[0])
q=""
for i in range (0,l):
	m=b[0][i]
	f=0
	for j in range (0,a):
		if(m!=b[j][i]):
			f=1
	if(f==0):
		q=q+m
	else:
		break
print(q)
