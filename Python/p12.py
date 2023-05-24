def factor_count(n):
    res = 2
    k = n**(1/2)
    if k % 1 == 0:
        res += 1
        k -= 1
    k = int(k)
    for i in range(2, k):
        if n % i == 0:
            res += 2
    return res


m = 0
for i in range(1000000):
    m += i
    if factor_count(m) > 500:
        print(m)
        break
