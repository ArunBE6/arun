import sys, string, math
s,p = map(int,input().split())
lis1 = list(map(int,input().split()))
lis2 = list(map(int,input().split()))
val1 = 1
for i in range(0,len(lis2)) :
    if lis2[i] not in lis1 :
        val1 = 0
        break
if val1 : print('YES')
else :    print('NO')
