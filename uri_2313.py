# URI Online Judge | 2313

A, B, C = [int(x) for x in input().split()]
if A >= (B + C) or B >= (A + C) or C >= (A + B): # não forma triangulo
    print('Invalido')
else:
    if A == B == C:
        tipo = 'Equilatero'
    elif A == B != C or A == C != B or B == C != A:
        tipo = 'Isoceles'
    elif A != B != C:
        tipo = 'Escaleno'
    if A**2 == (B**2 + C**2) or B**2 == (A**2 + C**2) or C**2 == (B**2 + A**2):
        retangulo = 'S'
    else: 
        retangulo = 'N'
    print(f'Valido-{tipo}')
    print(f'Retangulo: {retangulo}')