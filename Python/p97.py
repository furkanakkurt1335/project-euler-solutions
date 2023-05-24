# Large non-Mersenne prime
length = 10
n = 1
for i in range(7830457):
	# print(n)
	n *= 2
	n_str = str(n)
	if len(n_str) > length: n = int(n_str[-length:])
print(str(n*28433+1)[-length:])
# solved, 2022-01-28 21:21: 8739992577

'''
# Normal
2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16384
32768
65536
131072
262144
524288
1048576

# 3 length
2
4
8
16
32
64
128
256
512
24
48
96
192
384
768
536
72
144
288
576
'''