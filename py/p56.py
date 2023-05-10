max_digital_sum = 0
for i in range(2, 100):
	for j in range(2, 100):
		exp_t = sum([int(i) for i in list(str(i**j))])
		if exp_t > max_digital_sum:
			max_digital_sum = exp_t
print(max_digital_sum)
# solved, 2022-01-30 08:20: 972