def is_prime(n):
	if n < 2: return False
	elif n % 2 == 0 and n != 2: return False
	elif n == 2: return True
	elif n > 2:
		for i in range(2, int(n**(1/2))+1):
			if (n / i) % 1 == 0:
				return False
		return True


max_n = 0
max_res = 0
for a in range(-1000, 1001):
	for b in range(-1000, 1001):
		n = 0
		while 1:
			if is_prime(n**2 + a*n + b): n += 1
			else:
				if n > max_n:
					max_n = n
					max_res = a, b, n
				break
print(max_res)