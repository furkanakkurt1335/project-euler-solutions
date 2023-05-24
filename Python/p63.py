res_sum = 0
i = 1
while 1:
	n_t = 1
	adds_nothing = True
	while 1:
		calc = n_t**i
		calc_len = len(str(calc))
		if calc_len == i:
			# print(calc, n_t, i);input()
			adds_nothing = False
			res_sum += 1
		elif calc_len > i:
			break
		n_t += 1
	i += 1
	if adds_nothing: break
print(res_sum)
# solved, 2022-01-25 18:18: 49
