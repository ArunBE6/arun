elements,sh_count=map(int,input().split())

var1=list(map(int,input().split()))
for i in range(sh_count):
    var1=[var1[-1]]+var1[:-1]
print(*var1,end=" ")
