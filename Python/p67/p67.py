import os

path = os.path.dirname(os.path.realpath(__file__))

def get_triangle():
	tri_tmp = open(f'{path}\\p067_triangle.txt', 'r', encoding='utf-8').readlines()
	# print(tri_tmp[1].split());input()
	triangle = []
	count = 0
	for row in tri_tmp:
		row = row.split()
		int_row = []
		for el in row:
			int_row.append(int(el))
		triangle.append(int_row)
		# print(triangle);input()
	return triangle

def solve(triangle, curr_path, curr_index, depth):
	global max_sum, max_path
	if depth == len(triangle):
		curr_sum = sum(curr_path)
		if curr_sum > max_sum:
			max_sum = curr_sum
		return True
	row = triangle[depth]
	for i in range(len(row[curr_index:curr_index+2])):
		el = triangle[depth][curr_index+i]
		solve(triangle, curr_path + [el], curr_index+i, depth+1)
	return False

# print(triangle[-5:]);exit()
# max_sum = -1
# max_path = []
# solve(triangle, [], 0, 0)
# print(max_sum)

triangle = get_triangle()
while len(triangle) != 1:
	last_row = triangle[-1]
	el1 = last_row[0]
	for i in range(len(last_row)-1):
		# el_add = last_row[i]
		el2 = last_row[i+1]
		triangle[-2][i] += max(el1, el2)
		el1 = el2
		# if i == 0: triangle[-2][0] += el_add
		# elif i == len(last_row)-1: triangle[-2][-1] += el_add
		# else:
	del triangle[-1]
print(triangle[0])
# solved, 2022-02-05 08:54: 7273
