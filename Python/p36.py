def is_palindromic(number):
	num_str = str(number)
	num_len = len(num_str)
	for i in range(num_len//2):
		if num_str[i] != num_str[num_len-i-1]:
			return False
	return True

res_sum = 0
for i in range(10**6):
	if is_palindromic(i) and is_palindromic(str(bin(i))[2:]):
		res_sum += i
print(res_sum)
# solved, 2022-01-27 10:20: 872187