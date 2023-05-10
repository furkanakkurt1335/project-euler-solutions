
size = 5
# pen_t = n*(3*n-1)/2
pen_l = [n*(3*n-1)/2 for n in range(144,10**size)]
# hex_t = n*(2*n-1)
hex_l = [n*(2*n-1) for n in range(166,10**size)]

n = 286
for n in range(286,10**(size+1)):
	tri_t = n*(n+1)/2
	if tri_t in pen_l and tri_t in hex_l:
		print(tri_t, n)
		break
# solved, 2022-01-28 19:34: 1533776805