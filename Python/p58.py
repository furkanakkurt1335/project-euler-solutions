'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
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

ratio = 100
primes = 0
all = 1
current_number, current_addition = 1, 2
while ratio > 0.1:
	for _ in range(4):
		current_number += current_addition
		if is_prime(current_number):
			# print(current_number, end=',')
			primes += 1
	all += 4
	current_addition += 2
	ratio = primes/all
print(ratio, primes, all)
print(f'Side length: {current_addition-1}')
# solved, 2/1/2022 10:48 PM: 26241