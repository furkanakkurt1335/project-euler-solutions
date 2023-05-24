def is_pal(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


l = []
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        s = str(i*j)
        if is_pal(s):
            l.append(int(s))
max = 0
for i in range(len(l)):
    if l[i] > max:
        max = l[i]

print(max)
