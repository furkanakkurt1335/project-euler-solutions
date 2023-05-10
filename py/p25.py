f1=1
f2=2
c = 2
while 1:
	s=str(f2)
	if len(s) >= 3:
		print(c)
		break
	f1, f2=f2, f2+f1
	c+=1