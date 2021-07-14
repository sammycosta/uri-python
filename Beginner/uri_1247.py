# URI Online Judge | 1247
# nome: Samantha Costa de Sousa
from math import sqrt

while True:
    try:
        D, VF, VG = input().split()
        D = int(D)  # distancia entre fugitivo e a guardaa
        VF = int(VF)  # velocidade do fugitivo
        VG = int(VG)  # velocidade da guarda
        tempo_fugitivo = 12 / VF
        DG = sqrt(12**2 + D**2)
        tempo_guarda = DG / VG
        if (1 <= D, VF, VG <= 100):
            if tempo_guarda <= tempo_fugitivo:
                print('S')
            else:
                print('N')
        else:
            break
    except EOFError:
        break