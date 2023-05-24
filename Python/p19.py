m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
y = 1900
count = 0
for i in range(110):
    for j in range(12):
        if y > 1900 and y < 2001 and day == 6:
            count += 1
        if j == 1:
            if y % 400 == 0:
                day += 29
            elif y % 100 == 0:
                day += 28
            elif y % 4 == 0:
                day += 29
        else:
            day += m[j]
        day %= 7
    y += 1
print(count)
