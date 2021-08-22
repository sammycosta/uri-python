# URI Online Judge | 2375
N = int(input()) # diâmetro da bola de boliche
A, L, P = [int(x) for x in input().split()] # altura, largura, profundidade
if N <= A and N <= L and N <= P:
    print('S')
else:
    print('N')
