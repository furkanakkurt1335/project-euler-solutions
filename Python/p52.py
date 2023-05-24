def is_fine(n):
	global digs
	n_str = str(n)
	n_len = len(n_str)
	for i in digs:
		n_t = str(n*i)
		for i in n_t:
			if n_t.count(i) != n_str.count(i):
				return False
	return True

n = 1
digs = [i for i in range(2, 7)]
while 1:
	if is_fine(n):
		break
	n += 1
print(n)
# solved, 2022-01-31 21:22: 142857