# 65 'A', 90 'Z'
f = open('p22/sorted_p022_names.txt', 'r', encoding='utf-8')
s = f.read().split('\n')
f.close()
sum = 0
for i in range(len(s)):
    temp_sum = 0
    for j in s[i]:
        temp_sum += ord(j) - 64
    temp_sum *= i + 1
    sum += temp_sum
print(sum)
