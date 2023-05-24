def is_prime(n):
    s = str(n)[-1]
    if s == '5':
        return False
    if int(s) % 2 == 0:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if (n / i) % 1 == 0:
            return False
    return True


n = 0
for i in range(3, 2000000, 2):
    if is_prime(i):
        n += i
n += 7
print(n)
