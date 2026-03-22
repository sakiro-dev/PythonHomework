s = input()
clean = "".join(ch for ch in s if ch.isdigit() or ch == "+")
print(clean)
