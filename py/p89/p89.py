'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''
import os
cd = os.path.dirname(os.path.realpath(__file__))
romans = open(f'{cd}\\p089_roman.txt', 'r', encoding='utf-8').read().split('\n')

def get_minimal(roman): # return minimal string
	roman = roman.replace('IIII', 'IV')
	roman = roman.replace('VIV', 'IX')
	roman = roman.replace('XXXX', 'XL')
	roman = roman.replace('LXL', 'XC')
	roman = roman.replace('CCCC', 'CD')
	roman = roman.replace('DCD', 'CM')
	# roman = roman.replace()
	# roman = roman.replace()
	# roman = roman.replace()
	# roman = roman.replace()
	return roman

saved_count = 0
for roman in romans:
	saved_count += len(roman) - len(get_minimal(roman))
print(saved_count)
# solved, 2022-02-04 18:55: 743