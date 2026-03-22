s = input()
first_space = s.find(' ')
a = int(s[:first_space])
second_space = s.find(' ', first_space+1)
b = int(s[first_space+1:second_space])
c = int(s[second_space+1:])
if (a <= b <= c) or (c <= b <= a):
    print(b)
elif (b <= a <= c) or (c <= a <= b):
    print(a)
else:
    print(c)
