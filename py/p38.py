def is_pandigital(s):
	global digs
	l = list(s)
	if len(l) != 9 or '0' in l:
		return False
	for i in l:
		if l.count(i) > 1:
			return False
	return True

digs = [i for i in range(1, 10)]
n = 1
max_pan = 123456789
while 1:
	s = str(n)
	for i in range(2, 10):
		s += str(n*i)
		if len(s) > 9: break
		if is_pandigital(s) and int(s) > max_pan:
			print(n, int(s));input()
			max_pan = int(s)
	n += 1
# solved, 2022-01-31 12:38: 932718654