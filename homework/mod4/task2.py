def fast_exp(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exp(a * a, n // 2)
    else:
        return a * fast_exp(a, n - 1)


a, n = list(map(int, input().split()))
print(fast_exp(a, n))
