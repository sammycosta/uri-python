# URI Online Judge | 2435
N, D, V = [int(x) for x in input().split()]
N1, D1, V1 = [int(x) for x in input().split()]
T = D/V
T1 = D1/V1
if T < T1: # a T é mais rápida
    print(N)
else:
    print(N1)