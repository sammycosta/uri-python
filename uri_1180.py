# URI Online Judge | 1180
N = int(input())
X = [int(x) for x in input().split()]
c = sorted(X) #o sorted funciona, o .sort não
print(f'Menor valor: {c[0]}')
print(f'Posicao: {X.index(c[0])}')