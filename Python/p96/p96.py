def board_finished(board):
	for i in range(len(board)):
		if '.' in board[i]:
			return False
	return True

def get_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == '.': return i, j
	return -1

def get_col(board, col_index):
	res_col = []
	for i in range(len(board)):
		res_col.append(board[i][col_index])
	return res_col

def valid(board, pos, val, nums):
	size = len(board)
	row, col = pos
	board[row][col] = val
	for i in range(len(board)):
		row = board[i]
		col = get_col(board, i)
		for j in nums:
			if col.count(j) > 1 or row.count(j) > 1: return False
	row_count = 0
	col_count = 0
	for k in range(9):
		l = []
		for i in range(3):
			for j in range(3):
				l.append(board[i+row_count][j+col_count])
		col_count += 3
		if k % 3 == 2:
			row_count += 3
			col_count = 0
		for j in nums:
			if l.count(j) > 1: return False
	return True
		
def solve_board(board, nums):
	if board_finished(board):
		return True
	
	pos = get_empty(board)
	if pos == -1: return True
	row, col = pos
	for i in nums:
		if valid(board, pos, i, nums):
			board[row][col] = i
			if solve_board(board, nums):
				return True
			board[row][col] = '.'
		else: board[row][col] = '.'
	return False
import os
path = os.path.dirname(os.path.realpath(__file__))
size = 9
res_sum = 0
board = [[-1 for i in range(size)] for j in range(size)]
with open(f'{path}\\p096_sudoku.txt', 'r', encoding='utf-8') as f:
	lines = f.readlines()
board = []
nums = [i for i in range(1, 10)]
for line in lines:
	if line.startswith('Grid'): continue
	else:
		row = []
		for i in line:
			if i == '0': row.append('.')
			elif i == '\n': continue
			else: row.append(int(i))
		board.append(row)
		if len(board) == size:
			solve_board(board, nums)
			num = 0
			power = 2
			for dig in board[0][:3]:
				num += dig * (10**power)
				power -= 1
			res_sum += num
			# print(board[0][:3])
			# input()
			board = []
			print(res_sum)
print(res_sum)
# solved, 2022-02-03 08:38: 24702