# Lychrel

def is_palindromic(number):
	if type(number) != type(''): number = str(number)
	num_len = len(number)
	for i in range(len(number)//2):
		if number[i] != number[num_len-i-1]: return False
	return True

def is_lychrel(number):
	for _ in range(49): # iter_count, less than 50 iterations
		number_str = str(number)
		rev_str_l = list(reversed(number_str))
		rev_str = ''
		for i in rev_str_l: rev_str += i
		add_t = int(number_str) + int(rev_str)
		if is_palindromic(add_t):
			# print(number, add_t);input()
			return True
		number = add_t
	return False

count = 0
for i in range(10**4):
	if not is_lychrel(i): count += 1
	# else: print(i);input()
print(count)
# solved, 2022-01-28 12:10: 249