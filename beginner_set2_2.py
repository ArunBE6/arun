m,v = map(int,input().split())
lis = list(map(int,input().split()))
lis = sorted(lis,reverse =True)
print(lis[v-1])
