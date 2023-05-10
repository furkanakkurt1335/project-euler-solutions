'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''

res = 0
for i in range(1, 1001):
	n_t = 1
	for j in range(i):
		n_t *= i
		if len(str(n_t)) > 10:
			n_t = int(str(n_t)[-10:])
	res += n_t
print(res)
# Output: 4629110846700