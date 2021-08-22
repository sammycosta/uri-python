# URI Online Judge | 1221
from math import sqrt
N = int(input())
for i in range (N):
    num = int(input())
    if num > 1:
        resultado = 'Prime'
        for d in range(2, int(sqrt(num)+1)):
            if num % d == 0:
                resultado = 'Not Prime' # se tiver algum divisor entre 2 e a raiz quadrada, é composto
    print(resultado)