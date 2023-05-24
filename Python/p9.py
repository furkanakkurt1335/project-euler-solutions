for i in range(500):
    for j in range(i, 500):
        k = (i ** 2 + j ** 2) ** (1/2)
        if k % 1 == 0 and i + j + k == 1000:
            print(i, j, k)
