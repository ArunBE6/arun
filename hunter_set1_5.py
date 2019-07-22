var1=list(map(str,input()))
var2=sar1=0
for var3 in range(0,len(var1)-1):
  para=var1[var3]
  if int(p)!=0:
   for j in range(var3+1,var3+2):
    para=para+var1[j]
    if int(para)<27 and int(para)>0: var2=var2+1
    elif int(para)==0: var2=var2-1
    else: break
if var2!=1: sar1=var2%2
print(var2+sar1+1)
