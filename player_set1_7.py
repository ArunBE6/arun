ran=input()
bat=len(ran)
cat="".join(ran[i:i+2][::-1] for i in range (0,bat,2))
print (cat)
