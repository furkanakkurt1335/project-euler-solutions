nums = []
for num = 1:999
	if num % 3 == 0 || num % 5 == 0
		push!(nums, num)
	end
end
arr_sum = 0
for i = nums
	global arr_sum += i
end
print(arr_sum)
