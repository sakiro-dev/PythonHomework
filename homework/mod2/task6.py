s = input()
u = 0
z = 0
for i in range(len(s)):
    if (s[i] == '1'):
        u += 1
    elif (s[i] == '0'):
        z += 1
if u == z:
    print("yes")
else:
    print("no")
