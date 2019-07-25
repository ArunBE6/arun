import sys, string, math
num1,num2 = input().split()
num1,num2 = int(num1), int(num2)
list1 = [ int(ans) for ans in input().split()]
for i in range(0,num2) :
    ans = 0
    num3,num4 = input().split()
    num3,num4 = int(num3), int(num4)
    for j in range(num3-1,num4) :
        ans = ans ^ list1[j]
    print(ans)
