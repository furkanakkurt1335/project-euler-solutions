n = 1
for i in range(1, 100):
    n *= i
s = str(n)
k = 0
for i in range(len(s)):
    k += int(s[i])

print(k)
