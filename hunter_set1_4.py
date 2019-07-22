var1=int(input())
list1=list(map(int,input().split()))
for i in list1:
	if list1.count(i)==1:
		print(i)
		break
