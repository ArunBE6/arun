a=input()
b=input()
b=b.split()
b.sort(reverse = True)
p=""
for i in b:
	p+=i
print(int(p))
