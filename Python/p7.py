def is_prime(n):
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


count = 0
n = 2
while True:
    if is_prime(n):
        count += 1
    if count == 10001:
        print(n)
        exit()
    n += 1
