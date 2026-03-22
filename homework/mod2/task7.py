s_input = input()
pos = s_input.find(',')
s = str(s_input[:pos])
i = str(s_input[pos+1:])
c = 0
for ch in s:
    if ch == i:
        c += 1
    else:
        break
print(c)
