c = 0
for i in range(500000, 600000):
    for d in range(18, (i//2 + 1)):
        if ((i % d) == 0) and ((d % 10) == 8):
            c += 1
            print(i, d)
            break
    if c == 5:
        break