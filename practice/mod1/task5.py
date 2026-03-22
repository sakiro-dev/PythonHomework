prices = list(map(float, input().split()))
k = int(input())
m = int(input())
discount = [price - int(price // k) * m for price in prices]
print(*prices)
print(*discount)
