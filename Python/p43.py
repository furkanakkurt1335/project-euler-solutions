div_l = [2, 3, 5, 7, 11, 13, 17]
digits = [str(i) for i in range(10)]

def is_div(number): # comes as str
	for i in range(len(div_l)):
		divisor = div_l[i]
		num_t = int(number[i+1:i+4])
		if num_t % divisor != 0:
			return False
	return True
	
def rec_solve(current_number):
	global res_sum
	if len(current_number) == 10:
		if is_div(current_number):
			res_sum += int(current_number)
	avail_digits = [str(i) for i in range(10)]
	for i in current_number:
		avail_digits.remove(i)
	for dig_t in avail_digits:
		if current_number == '' and dig_t == 0: continue
		rec_solve(current_number+dig_t)

res_sum = 0
rec_solve('')
print(res_sum)
# solved, 2022-01-25 17:18: 16695334890