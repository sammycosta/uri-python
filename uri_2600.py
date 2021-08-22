# URI Online Judge | 2600
N = int(input())
for i in range(N):
    a = int(input())
    b, c, d, e = [int(x) for x in input().split()]
    f = int(input())
    resultado = 'SIM'
    lista = [a, b, c, d, e, f]
    lista.sort()
    if lista != [1, 2, 3, 4, 5, 6]:
        resultado ='NAO'
    r = a + f
    r1 = b + d
    r2 = c + e
    if r != 7 or r1 != 7 or r2 != 7:
        resultado = 'NAO'
    print(resultado)