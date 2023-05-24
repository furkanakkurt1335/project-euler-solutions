def get_divisors(number):
	divisors = {number}
	limit = int(number**(1/2))+1
	for i in range(2, limit):
		div = number / i
		if div.is_integer():
			divisors.add(i); divisors.add(int(div))
	return divisors

def get_relatively_primes(number):
	rps = {1}
	# if not (number/2).is_integer(): rps.add(2)
	s2 = get_divisors(number)
	for i in range(2, number):
		s1 = get_divisors(i)
		rp = True
		for j in s1:
			if j in s2: rp = False; break
		if rp: rps.add(i)
	return rps

def is_prime(n):
	if n < 2: return False
	elif n % 2 == 0 and n != 2: return False
	elif n == 2: return True
	elif n > 2:
		for i in range(2, int(n**(1/2))+1):
			if (n / i) % 1 == 0:
				return False
		return True

primes = [i for i in range(10**3) if is_prime(i)]
i = 1
# print(primes[-5:])
for prime in primes:
	i *= prime
	if i > 10**6:
		i /= prime
		break
ratio = i / len(get_relatively_primes(i))
print(i, ratio)
# solved, 2022-02-05 19:56: 510510
# print(divs, len(divs))