def largest_prime_factor(n):
    l = []
    for i in range(2, int(n**(1/2))+1):
        while True:
            if n == 1:
                break
            if n % i == 0:
                n /= i
                if i in l:
                    continue
                l.append(i)
            else:
                break
    print(l[-1])


largest_prime_factor(600851475143)
