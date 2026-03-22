s = list(map(int, input().split()))
k = int(input())
res = [x for x in s if x % k == 0]
print(*res)
