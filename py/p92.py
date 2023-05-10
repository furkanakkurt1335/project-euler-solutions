rec_89 = 0
for n in range(1, 10**7):
	while 1:
		sum_t = 0
		for i in str(n):
			sum_t += int(i)**2
		if sum_t == 89:
			# print(sum_t);input()
			rec_89 += 1
			break
		elif sum_t == 1:
			break
		n = sum_t
print(rec_89)
# solved, 2022-02-01 09:05: 8581146