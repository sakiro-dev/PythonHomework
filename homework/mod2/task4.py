s = input()
if s.isdigit():
    n = int(s)
    if n > 0:
        res_b = ""
        t = n
        while t > 0:
            res_b = str(t % 2) + res_b
            t //= 2
        
        res_o = ""
        t = n
        while t > 0:
            res_o = str(t % 8) + res_o
            t //= 8

        res_h = ""
        t = n
        digits = "0123456789ABCDEF"
        while t > 0:
            res_h = digits[t % 16] + res_h
            t //= 16
        print(f"{res_b}, {res_o}, {res_h}")
    else:
        print("Неверный ввод")
