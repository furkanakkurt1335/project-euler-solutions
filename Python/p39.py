def get_soln_count(p):
	count = 0
	for i in range(1, p):
		for j in range(i+1, p):
			# print(i, j);input()
			if i + j + j + 1 > p: break
			k = (i**2 + j**2)**(1/2)
			if k % 1 != 0: continue
			if k + i + j == p: count += 1 # ; print(i, j, k)
	return count

# print(get_soln_count(120))

max_soln_count = 0
max_i = 0
for i in range(1, 1001):
	count_t = get_soln_count(i)
	if count_t > max_soln_count:
		max_soln_count = count_t
		max_i = i
print(max_soln_count, max_i)
# solved, 2022-01-28 20:52: 840