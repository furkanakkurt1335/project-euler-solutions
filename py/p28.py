size = 1001
result_sum = 1
current_number = 1
end_number = 1001**2
current_increment = 2
while current_number < end_number:
	for _ in range(4):
		current_number += current_increment
		result_sum += current_number
	current_increment += 2
print(result_sum)
# solved, 2022-01-24 22:23: 669171001