def ComparingNumbers(n):
    s = set(n)
    if len(s) == len(n):
        print("Все числа разные")
    elif len(s) == 1:
        print("Все числа равны")
    else:
        print("Есть равные и неравные числа")


n = list(map(int, input().split()))
ComparingNumbers(n)
