import os
words = open(f'{os.path.dirname(os.path.realpath(__file__))}\\words_t.txt', 'r', encoding='utf-8').read().split('\n')
letter_values_d = dict()
letters = [chr(c) for c in range(65, 91)]
for i in range(len(letters)):
	letter = letters[i]
	letter_values_d[letter] = i+1
triangle_numbers = [(1/2)*n*(n+1) for n in range(1, 200)]
res_count = 0
for word in words:
	val_t = 0
	for letter in word:
		val_t += letter_values_d[letter]
	if val_t in triangle_numbers:
		res_count += 1
print(res_count)
# solved, 2022-01-31 12:46: 162