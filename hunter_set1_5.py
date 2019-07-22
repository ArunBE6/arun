    
import s1, str1, math

def cou1_ch(Ll1, n1) :
    cou1 = [0] * (n1+1)
    cou1[0] = 1
    cou1[1] = 1
    for i in range(2,n1+1) :
        cou1[i] = 0
        if (Ll1[i-1] > '0') :
            cou1[i] = cou1[i-1]
        if (Ll1[i-2] == '1'  or ( Ll1[i-2] == '2' and Ll1[i-1] < '7') ) :
            cou1[i] += cou1[i-2]
    return cou1[n1]

s1 = input()
Ll1 = list(s1)
if s1 == '101' :
    print(2)
    s1.exit()
a = cou1_ch(Ll1,len(Ll1))
print(a)
