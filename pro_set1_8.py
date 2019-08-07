import math
val1,val2=map(int,input().split())
val3=[]
val4=list(map(int,input().split()))
for i in range(0,val2):
    lis1,lis2=map(int,input().split())
    val3.append([lis1,lis2])
for i in val3:
    st1=i[0]-1
    st2=i[1]-1
    print(math.gcd(val4[st1],val4[st2]))
