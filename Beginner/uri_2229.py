# URI Online Judge | 2229
N = 0
teste = 0
pedacos = 0
while True:
    N = int(input())
    if N == -1:
        break
    else:
        if -1 <= N <= 15:
            teste += 1
            pedacos = (2**N + 1)**2
            print(f'Teste {teste}')
            print(pedacos)
            print('')