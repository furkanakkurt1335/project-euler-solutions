n1 = 0
for i in range(101):
    n1 += i**2
n2 = 0
for i in range(101):
    n2 += i
n2 **= 2
print(n2-n1)
