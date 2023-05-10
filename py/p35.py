'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
'''

def is_prime(n):
	if n < 2: return False
	elif n % 2 == 0 and n != 2: return False
	elif n == 2: return True
	elif n > 2:
		for i in range(2, int(n**(1/2))+1):
			if (n / i) % 1 == 0:
				return False
		return True

circular_prime_count = 0
circular_primes = set()
for i in range(10**6):
	is_circular_prime = True
	nums = set()
	if i not in circular_primes:
		num_str = str(i)
		rotate_count = len(num_str)-1
		rotates = {num_str}
		for i in range(rotate_count):
			num_str = num_str[-1] + num_str[:-1]
			rotates.add(num_str)
		for j in rotates:
			num = ''
			for k in j:
				num += k
			num = int(num)
			nums.add(num)
			if not is_prime(num):
				is_circular_prime = False
				break
	if is_circular_prime:
		for j in nums:
			circular_primes.add(j)
		circular_primes.add(i)
		circular_prime_count += 1

print(circular_prime_count)
print(circular_primes)
