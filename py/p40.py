num_to_achieve = 1000000
s = ''
num = 1
while len(s) < num_to_achieve:
	s += str(num)
	num += 1
num = 1
res = 1
while num != num_to_achieve:
	# print(int(s[num-1]), end=' ')
	res *= int(s[num-1])
	# print(res)
	num *= 10
res *= int(s[num_to_achieve-1])
# print(s[num_to_achieve-1])
print(res)
# solved, 2022-01-24 21:40: 210