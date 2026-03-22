def Palindrome(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    odd_c = 0
    for ch in freq:
        if freq[ch] % 2 == 1:
            odd_c += 1

    if odd_c > 1:
        print("Нельзя составить палиндром")
        return
    half = []
    center = ''
    for ch, cnt in freq.items():
        half.append(ch * (cnt // 2))
        if cnt % 2 == 1:
            center = ch
    left = ''.join(half)
    palindrome = left + center + left[::-1]
    print(palindrome)


s = input()
Palindrome(s)
