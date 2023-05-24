fib1 = 1
fib2 = 2
even_sum = 0
while fib2 <= 4*(10^6)
	global fib1, fib2, even_sum
	if fib2 % 2 == 0
		even_sum += fib2
	end
	tmp = fib2
	fib2 += fib1
	fib1 = tmp
end
println(string("Result: ", even_sum))