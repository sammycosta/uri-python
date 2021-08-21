# URI Online Judge | 1953
# nome: Samantha Costa
while True:
    try:
        n = int(input())
        dicio = {}
        epr = ehd = intrusos = 0
        if 1 <= n <= 10**5:
            for i in range(n):
                matricula, sigla = input().split()
                if sigla == 'EPR':
                    epr += 1
                elif sigla == 'EHD':
                    ehd += 1
                else:
                    intrusos += 1
            print(f'EPR: {epr}')
            print(f'EHD: {ehd}')
            print(f'INTRUSOS: {intrusos}')
    except EOFError:
        break