import sys, string, math
line1 = input().split(' ')
line2 = []
for s in line1 :
    line2.append(s[::-1])
print(*line2)
