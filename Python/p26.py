import decimal

decimal.getcontext().prec = 10000
numerator = decimal.Decimal("1")

longest_d = {i: 0 for i in range(2, 1000)}

for denominator in range(2, 1000):
  div = numerator / denominator
  div_str = str(div)
  dec_part = div_str[div_str.find('.')+1:]
  dec_len = len(dec_part)
  curr_len = 1
  while curr_len < dec_len / 2:
    curr_seq = dec_part[:curr_len]
    rem_seq = dec_part[curr_len:]
    recurring = True
    recurred_times = 0
    while rem_seq:
      for i, ch in enumerate(curr_seq):
        if len(rem_seq) == i:
          break
        if ch != rem_seq[i]:
          recurring = False
          break
      if not recurring:
        break
      else:
        recurred_times += 1
      if recurred_times > 5:
        break
      rem_seq = rem_seq[curr_len:]
    if recurring:
      longest_d[denominator] = curr_len
      break
    curr_len += 1

longest_re = 0
longest_denom = 0
for key in longest_d:
  t = longest_d[key]
  if t > longest_re:
    longest_re = t
    longest_denom = key
print(longest_re, longest_denom)