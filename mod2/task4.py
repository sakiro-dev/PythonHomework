def binary(n):
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return result


def octal(n):
    result = ""
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    return result


def hexadecimal(n):
    result = ""
    digits = "0123456789ABCDEF"
    while n > 0:
        result = digits[n % 16] + result
        n //= 16
    return result


a = input().strip()
if a.isdigit():
    n = int(a)
    if n > 0:
        print(f"{binary(n)}, {octal(n)}, {hex(n)}")
    else:
        print("Неверный ввод")
else:
    print("Неверный ввод")
