start = 2
l = [(1, 1), (1, 2)]
curr_k = 2
cursor = 0
dig_ctr = 3
while dig_ctr != 100:
	if cursor == 2:
		l.append((1, curr_k*2))
		curr_k += 1
		cursor = 0
	else:
		l.append((1, 1))
		cursor += 1
	dig_ctr += 1
# print(l[:20])
while len(l) != 1:
	last1_numr, last1_denm = l[-1]
	last2_numr, last2_denm = l[-2]
	mul = last1_denm * last2_denm
	add = mul + last1_numr
	l = l[:-1]
	l[-1] = (last2_numr*last1_denm, add)
	# print(l);input()
numr, denm = l[0]
digs_100 = [int(i) for i in str(start*denm + numr)]
print(sum(digs_100))
# solved, 2022-02-03 13:25: 272