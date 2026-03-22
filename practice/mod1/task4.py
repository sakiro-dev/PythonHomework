s = input().split(';')
lengths = [len(phrase.split()) for phrase in s]
print(*s)
print(*lengths)
