x = 5**36 + 5**24 - 25
s = ""
while x != 0:
    s += str(x % 5)
    x = x // 5
s = s[::-1]
print(s.count("4"))