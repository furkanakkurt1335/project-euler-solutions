# collatz problem
d = {}
for i in range(2, 10**6):
    num = i
    length = 0
    while True:
        if i == 1:
            d[num] = length
            break
        if i in d.keys():
            length += d[i]
            d[num] = length
            break
        if i % 2 == 0:
            i /= 2
        else:
            i = 3*i + 1
        length += 1

max = 0
for i in d.keys():
    if d[i] > max:
        max = d[i]
        n = i
print(n)
