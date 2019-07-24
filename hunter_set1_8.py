val1 = input()
list1 = list(map(int,input().split()))
for i in range(len(list1)):
    for j in range(len(list1)):
        for k in range(len(list1)):
            if list1[i]+list1[j] == list1[k] and i<j<k:
                print(list1[i],list1[j],list1[k])
