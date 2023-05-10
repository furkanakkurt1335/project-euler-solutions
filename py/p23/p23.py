from time import perf_counter
import os

def get_divisors(number):
	divisors = {1}
	limit = int(number**(1/2))+1
	for i in range(2, limit):
		div = number / i
		if div.is_integer():
			divisors.add(i); divisors.add(int(div))
	return divisors

# print(get_divisors(25));exit()

def is_abundant(number):
	if sum(get_divisors(number)) > number: return True
	return False

def can_be_written(number):
	global abundant_numbers
	for i in range(len(abundant_numbers)):
		an1 = abundant_numbers[i]
		if an1 > number: return False
		for j in range(i, len(abundant_numbers)):
			sum_t = an1 + abundant_numbers[j]
			if sum_t == number: return True
			elif sum_t > number: break
	return False

limit = 28123
# result_list = []
# abundant_numbers = [12]
# abundant_numbers = list()
# for current_number in range(1, 2*limit):
# 	if is_abundant(current_number): abundant_numbers.append(current_number)
path = os.path.dirname(os.path.realpath(__file__))
# with open(f'{path}\\abundant numbers.txt', 'w', encoding='utf-8') as f:
# 	for i in range(len(abundant_numbers)):
# 		f.write(str(abundant_numbers[i]))
# 		if i != len(abundant_numbers)-1: f.write(',')
# exit()
abundant_numbers = open(f'{path}\\abundant numbers.txt', 'r', encoding='utf-8').read().split(',')
for i in range(len(abundant_numbers)):
	abundant_numbers[i] = int(abundant_numbers[i])
# print(can_be_written(28125));exit()
# exit()
# print(perf_counter()) # Output: 13.142111

# for i in range(10):
# 	print(can_be_written(limit+1+i))
# exit()
res_sum = 0
# for current_number in range(1, limit+1):
for current_number in range(limit+1):
	if not can_be_written(current_number): res_sum += current_number
	# if not can_be_written(current_number): print(current_number,end=',')
	# print(current_number,end=',')
	# print(res_sum, current_number)
	# if current_number % 1000 == 0: print(res_sum, current_number, perf_counter())
	# if perf_counter()%5 < 1: print(res_sum, current_number)
	# print(result_list[-1])
print(res_sum)
# solved, 2022-02-11 23:16: 4179871