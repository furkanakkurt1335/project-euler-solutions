def is_prime(n):
	if n < 2: return False
	elif n % 2 == 0 and n != 2: return False
	elif n == 2: return True
	elif n > 2:
		for i in range(2, int(n**(1/2))+1):
			if (n / i) % 1 == 0:
				return False
		return True
	
def is_trunc_prime(n):
	nums = {n}
	left_str = str(n)
	while left_str != '':
		nums.add(int(left_str))
		left_str = left_str[:-1]
	right_str = str(n)
	while right_str != '':
		nums.add(int(right_str))
		right_str = right_str[1:]
	for num in nums:
		if not is_prime(num): return False
	return True

trunc_primes = []

n = 11
while len(trunc_primes) != 11:
	if is_trunc_prime(n): trunc_primes.append(n)
	n += 2
print(trunc_primes)
print(sum(trunc_primes))