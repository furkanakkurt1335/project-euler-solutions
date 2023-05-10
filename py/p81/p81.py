import os
path = os.path.dirname(os.path.realpath(__file__))
# text = open(f'{path}\\example_matrix.txt', 'r', encoding='utf-8').readlines()
text = open(f'{path}\\p081_matrix.txt', 'r', encoding='utf-8').readlines()
matrix = []
for line in text:
	row_str = line.split(',')
	row_int = []
	for i in row_str: row_int.append(int(i))
	matrix.append(row_int)
size = len(matrix)
# size=20
# f = open(f'{path}\\{size}_matrix.txt', 'w', encoding='utf-8')
# for i in range(size):
# 	for j in range(size):
# 		f.write(str(matrix[i][j]))
# 		if j != size-1: f.write(',')
# 	if i != size-1: f.write('\n')
# f.close()
# exit()
# print(len(matrix), len(matrix[0])) # 80 80
# min_path_sum = -1

def solve(curr_sum, curr_pos, curr_sequence):
	global matrix, size, min_path_sum
	curr_row, curr_col = curr_pos
	if curr_row == size-1 and curr_col == size-1:
		if min_path_sum == -1 or curr_sum < min_path_sum: min_path_sum = curr_sum
		# print(curr_sum)
		# print(sequence)
		return True
	for i in range(2):
		if i == 0: pos = (curr_row+1, curr_col)
		else: pos = (curr_row, curr_col+1)
		# print(pos)
		if pos[0] > size-1 or pos[1] > size-1: continue
		if min_path_sum == -1 or curr_sum + matrix[pos[0]][pos[1]] < min_path_sum:
			solve(curr_sum=curr_sum+matrix[pos[0]][pos[1]], curr_pos=pos, curr_sequence=curr_sequence + [i])
	return False

# solve(curr_sum=0, curr_pos=(0, 0), curr_sequence=[])
# print(min_path_sum+matrix[0][0])

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j],end=' ')
		print()
	print()

# print_matrix(matrix)
for i in range(size-1, 0, -1):
	matrix[-1][i-1] += matrix[-1][i]
	matrix[i-1][-1] += matrix[i][-1]
# print_matrix(matrix)

for i in range(size-2, -1, -1):
	matrix[i][i] += min(matrix[i+1][i], matrix[i][i+1])
	# print_matrix(matrix);input()
	for j in range(i, 0, -1):
		matrix[i][j-1] += min(matrix[i+1][j-1], matrix[i][j])
		# print_matrix(matrix);input()
		matrix[j-1][i] += min(matrix[j-1][i+1], matrix[j][i])
		# print_matrix(matrix);input()
print(matrix[0][0])
# solved, 2022-02-05 11:43: 427337
