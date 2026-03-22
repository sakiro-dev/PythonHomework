s = input()
out = f"{int(s):b}, {int(s):o}, {int(s):X}" if s.isdigit() and int(s) > 0 else "Неверный ввод"
print(out)
