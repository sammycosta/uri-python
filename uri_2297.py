# URI Online Judge | 2297
# nome: Samantha Costa
R = 1
n = 0
while R != 0:
    R = int(input())
    Aldo, Beto = 0, 0
    resultado = 'default'
    for i in range(R):
        A, B = [int(x) for x in input().split()]
        Aldo += A
        Beto += B
    n+= 1
    if Aldo > Beto:
        resultado = 'Aldo'
    elif Beto > Aldo:
        resultado = 'Beto'
    if R != 0:
        print(f'Teste {n}')
        print(resultado)
        print()