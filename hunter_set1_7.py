n=int(input())
list1=list(map(int,input().split()[:n]))
for i in range(0,n):
    if i%2==0 and list1[i]%2!=0:
        print(list1[i],end=" ")
    elif i%2!=0 and list1[i]%2==0:
        print(list1[i],end=" ")
