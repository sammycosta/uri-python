# URI Online Judge | 1173
# nome: Samantha Costa
V = int(input())
N = list(range(10))
if V <= 50:
    N[0] = V
    for i in range(1, 10):
        N[i] = (N[i-1])*2
    for x in range(10):
        print(f'N[{x}] = {N[x]}')