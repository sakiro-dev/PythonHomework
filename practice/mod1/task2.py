n = int(input())
numbers = list(range(n, n * n + 1))
sqrt_numbers = [x ** 0.5 for x in numbers]
print(*numbers)
print(*sqrt_numbers)
