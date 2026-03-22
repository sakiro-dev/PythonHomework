s = input()
new_s = ""
for ch in s:
    if ch != '-' and ch != ')' and ch != '(' and ch != ' ':
        new_s += ch
print(new_s)
