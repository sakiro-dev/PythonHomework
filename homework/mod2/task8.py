s = input()
words = []
start = 0
for i in range(len(s)):
    if s[i] == ' ':
        words.append(s[start:i])
        start = i + 1
words.append(s[start:])

result = ""
for w in words:
    result += w[-1]
print(result)
