n = int(input())
names = []
for i in range(n):
    name = input()
    names.append(name)
uni = []
lengths = []
for name in names:
    if len(name) not in lengths:
        uni.append(name)
        lengths.append(len(name))
print(*uni)
print(*names)
