car1=int(input())
car2=[int(o) for o in input().split(" ")]
car3=0
for i in range(car1):
      for j in range(i):
           if(car2[j]<car2[i]):
                car3+=car2[j]
print(car3)
