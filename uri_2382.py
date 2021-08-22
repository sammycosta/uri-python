# URI Online Judge | 2382
from math import sqrt
L, A, P, R = [int(x) for x in input().split()] # a largura, altura e profundidade da caixa, e o raio da esfera.
d = sqrt(L**2 + A**2 + P**2) # diagonal da caixa
if d <= (2*R):
    print('S')
else: 
    print('N')
