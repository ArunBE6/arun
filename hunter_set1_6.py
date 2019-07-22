num=int(input())
sp=input().split()
flow=False
for ip in sp:
    if sp.count(ip)>1:
        print(ip,end='')
        flow=True
        break
if flow==False:
    print("unique") 
