fib1 = 1
fib2 = 2
sum = 2
while True:
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 % 2 == 0:
        sum += fib2
    if fib2 > 4 * (10**6):
        break
print(sum)
