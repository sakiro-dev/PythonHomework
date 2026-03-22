# a = int(input())
# b = int(input())
# print(a % b)


s = input()
pos = s.find(',')
a = int(s[:pos])
b = int(s[pos+2:])
# предполагаем, что формат ввода - строго через запятую и пробел (123, 12)
print(a % b)
