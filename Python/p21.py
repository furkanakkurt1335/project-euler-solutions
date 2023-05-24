from time import perf_counter

def get_divisors(number):
	divisors = [1]
	last_divisor = -1
	for i in range(2, number):
		if number % i == 0: divisors.append(i)
		if len(divisors) > 1: last_divisor = number / divisors[1]
		if i > last_divisor: return divisors
	return divisors

amicable_numbers = []
sum_dict = dict()
for i in range(1, 10000):
	sum_dict[i] = sum(get_divisors(i))
print(perf_counter())
for i in sum_dict.keys():
	sum1 = sum_dict[i]
	if sum1 < 10000 and i == sum_dict[sum1] and i != sum1:
		amicable_numbers.append(i)
		amicable_numbers.append(sum1)
print(sum(set(amicable_numbers)))
# solved, 2022-01-24 23:06: 31626