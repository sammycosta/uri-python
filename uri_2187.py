# URI Online Judge | 2187
c = 0
while True:
    V = int(input())
    if V == 0:
        break
    c +=1
    lista = [50, 10, 5, 1]
    dicio = {}
    for i in lista:
        R = V // i
        V -= R*i
        dicio[i] = R
    print(f'Teste {c}')
    print(f'{dicio[50]} {dicio[10]} {dicio[5]} {dicio[1]}\n')
    