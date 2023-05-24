num = 1
p = False
while True:
    for i in range(1, 21):
        if num % i != 0:
            break
        if i == 20:
            print(num)
            exit()
    num += 1
