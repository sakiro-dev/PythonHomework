s = input()
dots = []
for i in range(len(s)):
    if s[i] == '.':
        dots.append(i)


parts = []
start = 0
for dot in dots:
    parts.append(s[start:dot])
    start = dot + 1
parts.append(s[start:])

for i in range(len(parts) - 1, - 1, - 1):
    print(parts[i])
