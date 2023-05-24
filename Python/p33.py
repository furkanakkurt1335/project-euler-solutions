
fracs = []
for numr in range(10, 100):
	for denm in range(numr+1, 100):
		if numr == denm: continue
		numr_s, denm_s = str(numr), str(denm)
		if numr_s[-1] == '0' and denm_s[-1] == '0':
			continue
		together = numr_s + denm_s
		for i in together:
			if together.count(i) == 2 and numr_s.count(i) == 1:
				new_numr, new_denm = int(numr_s.replace(i, '')), int(denm_s.replace(i, ''))
				if new_denm != 0 and new_numr/new_denm == numr/denm:
					fracs.append((numr, denm))
					break
numr, denm = 1, 1
for frac in fracs:
	numr *= frac[0]
	denm *= frac[1]
print(numr, denm)
curr_div = 2
while not (curr_div > numr):
	if (numr/curr_div).is_integer():
		numr /= curr_div
		denm /= curr_div
	else: curr_div += 1
print(numr, denm, curr_div)
# solved, 2022-02-03 13:47: 100