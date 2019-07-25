var1=input()
var1=var1.split()
var2=var1[0]
var3=var1[1]
sum1=0
n=0
while(n<len(var2) and sum1<2):
    if(var2[n]!=var3[n]):
        sum1+=1
    n+=1
if(sum1==1 or sum1==0):
    print("YES")
else:
    print("NO")
