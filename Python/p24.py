'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
2783915460
'''

def solve(nums, perm, depth):
	global count
	if len(perm) == depth:
		count += 1
		if count == 10**6: print(perm)
	for i in nums:
		if i not in perm:
			perm.append(i)
			solve(nums, perm, depth)
			perm.pop()
	return False

count = 0
nums = [i for i in range(10)]
solve(nums, [], len(nums))