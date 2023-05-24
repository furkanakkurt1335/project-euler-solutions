def is_prime(n):
	if n < 2: return False
	elif n % 2 == 0 and n != 2: return False
	elif n == 2: return True
	elif n > 2:
		for i in range(2, int(n**(1/2))+1):
			if (n / i) % 1 == 0:
				return False
		return True

def rec_solv(cl):
	global nums, mul_dd
	if len(cl) == 3:
		num = mul_dd[cl[0]][2] + mul_dd[cl[1]][3] + mul_dd[cl[2]][4]
		if num < 50*(10**6): nums.add(num)
		return
	for i in digs:
		rec_solv(cl + [i])

# digs = [i for i in range(7100**2) if is_prime(i)]
digs = [i for i in range(10**4) if is_prime(i)]
# print(len(digs));input()
mul_dd = dict()
for dig in digs:
	mul_dd[dig] = {2: dig**2, 3:dig**3, 4:dig**4}
# print(len(mul_dd));input()
nums = set()
limit = 50*(10**6)-1
for a in digs:
	a_sqr = mul_dd[a][2]
	if a_sqr > limit: break
	for b in digs:
		ab_added = a_sqr + mul_dd[b][3]
		if ab_added > limit: break
		for c in digs:
			abc_added = ab_added + mul_dd[c][4]
			if abc_added > limit: break
			nums.add(abc_added)
			
print(len(nums))
# solved, 2022-02-05 11:59: 1097343

# rec_solv([])
# ctr = 0
# for i in nums:
	# if i < 50: ctr += 1 # 4
	# if i < 50*(10**6): ctr += 1
# print(sorted(list(nums))[-100:])