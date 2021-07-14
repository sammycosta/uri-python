# URI Online Judge | 2378
N, C = input().split()
N, C = int(N), int(C)
pessoas, resultado = 0, 0
if 1 <= N <= 1000 and 1 <= C <= 1000:
    for i in range(N):
        S, E = input().split()
        S, E = int(S), int(E)
        pessoas += -S + E
        if pessoas > C:
            resultado = 'S'

    if resultado != 'S':
        print('N')
    else:
        print(resultado)