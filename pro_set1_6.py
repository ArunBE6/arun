num1=int(input())
val1=list(map(int,input().split()))
val2=0
for i in range(0,num1-2):
	for j in range(1,num1-1):
		for k in range(2,num1):
			if(val1[i]<val1[j] and val1[j]<val1[k]):
				val2+=1
print(val2)
