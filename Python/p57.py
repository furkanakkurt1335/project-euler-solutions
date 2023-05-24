numr, denm = 3, 2
res_sum = 0
for _ in range(10**3):
    old_denm = denm
    denm = numr + denm
    numr = denm + old_denm
    if len(str(numr)) > len(str(denm)): res_sum += 1
print(res_sum)
# solved, 2/1/2022 11:04 PM: 153
