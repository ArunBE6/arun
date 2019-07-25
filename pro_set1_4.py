num1,num2=map(str,input().split())
ans1=0
if len(num1)>len(num2):
  num1,num2=num2,num1
val1=0
while val1<len(num1):
  ans1+=(ord(num2[val1])-ord(num1[val1]))
  val1+=1
for val1 in range(val1,len(num2)):
  ans1+=ord(num2[val1])-ord('a')+1
print(ans1)
