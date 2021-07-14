N = int(input()) #numero de bandejas
quebra = 0
for i in range(0, N):
    valores = input().split()
    L, C = valores
    L = int(L)
    C = int(C)
    if (L>C):
        quebra += C

print(quebra)