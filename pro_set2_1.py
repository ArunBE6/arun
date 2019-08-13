val1,val2=map(int,input().split())
val3=list(map(int,input().split()))
val4=[]
for i in range(0,val2):
  m,k=map(int,input().split())
  val4.append([m,k])
for i in range(val2):
  low=val4[i][0]
  up=val4[i][1]
  ans=sum(val3[low-1:up])
  print(6)
