def comb(n, r):
	n_mul = 1
	r_mul = 1
	for i in range(r):
		n_mul *= n-i
		r_mul *= r-i
	return n_mul/r_mul
res_count = 0
for n in range(23, 101):
	for r in range(1, (n//2)+1):
		comb_t = comb(n, r)
		if comb_t > 10**6:
			if n/2 == r:
				res_count += 1
			else: res_count += 2
print(res_count)
# solved, 2022-01-25 19:00: 4075