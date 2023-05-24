function is_prime(n)
	if iseven(n) return false end
	ceil_num = Int64(ceil(n^(1/2)))
	if iseven(ceil_num) ceil_num += 1 end
	for i = ceil_num:-2:2
		if n % i == 0
			return false
		end
	end
	return true
end

num = 600851475143
ceil_num = Int64(ceil(num^(1/2)))
if iseven(ceil_num) ceil_num += 1 end
for i = ceil_num:-2:3
	if num % i == 0 && is_prime(i)
		print(i)
		break
	end
end