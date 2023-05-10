'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time

nums = list()
curr_num = 10
while 1:
	if curr_num % 1000 == 0 and time.perf_counter() > 10: break
	sum_digs = 0
	for dig in str(curr_num):
		sum_digs += int(dig)**5
	if sum_digs == curr_num: nums.append(curr_num)
	curr_num += 1
print(nums, sum(nums))