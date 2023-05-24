
from time import perf_counter


factorials = {'0': 1, '1': 1}
for i in range(2, 10):
	mul_t = 1
	for j in range(2, i+1):
		mul_t *= j
	factorials[str(i)] = mul_t

n = 10
res_sum = 0
while 1:
	sum_t = 0
	for i in str(n):
		sum_t += factorials[i]
	if n == sum_t: res_sum += n
	n += 1
	if perf_counter() > 15: break
print(res_sum)
# solved, 2022-01-26 20:54: 40730