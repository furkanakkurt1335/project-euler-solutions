def is_prime(n):
	if n < 2: return False
	elif n % 2 == 0 and n != 2: return False
	elif n == 2: return True
	elif n > 2:
		for i in range(2, int(n**(1/2))+1):
			if (n / i) % 1 == 0:
				return False
		return True

def is_written(number):
	global primes
	num_calc = 0
	num_sqr = 0
	while 1:
		num_sqr += 1
		num_squared_doubled = 2*(num_sqr**2)
		if num_squared_doubled > number: break
		for prime in primes:
			num_calc = num_squared_doubled + prime
			if num_calc == number: return True
			elif num_calc > number: break
	return False

primes = [2, 3]
number = 3
while 1:
	while primes[-1] < number:
		num = primes[-1] + 2
		while 1:
			if is_prime(num):
				primes.append(num)
				break
			num += 2
	if number not in primes and not is_written(number):
		break
	number += 2
print(number)
# solved, 2022-01-24 18:56: 5777