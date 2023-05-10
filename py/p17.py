def get_letter_count(n):
	return len(get_word_from_num(n).replace(' ', '').replace('-', ''))

def get_word_from_num(n):
	s = ''
	if n < 10:
		s += nums_to_words[n]
	elif n < 100:
		if n < 20:
			s += nums_to_words[n]
		else:
			ones = n%10
			tens = n//10
			s += nums_to_words[tens*10]
			if ones != 0: s += f'-{nums_to_words[ones]}'
	else: # n < 1000
		s += nums_to_words[n//100]
		least_two = n % 100
		s += ' hundred'
		if least_two != 0:
			s += ' and '
			if least_two < 20:
				s += nums_to_words[least_two]
			else:
				tens = least_two//10
				s += nums_to_words[tens*10]
				ones = least_two%10
				if ones != 0: s += f'-{nums_to_words[ones]}'
	return s

nums = list(range(1, 20)) + list(range(20, 100, 10))
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
nums_to_words = dict()
# for i in range(len(nums)):
# 	nums_to_words[nums[i]] = len(words[i])
for i in range(len(nums)):
	nums_to_words[nums[i]] = words[i]
# print(get_word_from_num(888))
letter_count = 0
for i in range(1, 1000):
	letter_count += get_letter_count(i)
letter_count += len('onethousand')
print(letter_count)
