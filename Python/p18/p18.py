import os

path = os.path.dirname(os.path.realpath(__file__))

def get_triangle():
	tri_tmp = open(f'{path}\\p18 triangle.txt', 'r', encoding='utf-8').read().split()
	triangle = []
	count = 0
	for i in range(1,16):
		row = []
		for j in range(i):
			row.append(int(tri_tmp[count]))
			count += 1
		triangle.append(row)
	return triangle

def solve(triangle, curr_path, curr_index, curr_sum, depth):
	global max_sum, max_path
	if depth == len(triangle):
		if curr_sum > max_sum:
			max_sum = curr_sum
			max_path = curr_path
			# print(max_sum)
			# print(curr_path)
		return True
	row = triangle[depth]
	for i in range(len(row[curr_index:curr_index+2])):
		el = triangle[depth][curr_index+i]
		# print(curr_path, el);'''Cool Note''';input()
		solve(triangle, curr_path + [el], curr_index+i, curr_sum + el, depth+1)
	return False

triangle = get_triangle()
max_sum = -1
max_path = []
solve(triangle, [], 0, 0, 0)
print(max_sum, max_path)
print(sum(max_path))
# solved, 2022-01-29 12:47: 1074