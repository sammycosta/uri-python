valores = input().split()
c, p, f = valores
C = int(c)
P = int(p)
F = int(f)
if P/F < C:
    print('N')
else:
    print('S')