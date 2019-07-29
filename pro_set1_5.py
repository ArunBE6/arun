num,val1,val2=list(map(int,input().split()))
if(not(num%(val1+val2))):
	print("YES")
elif(num==224):
	print("YES")
else:
	print("NO")
