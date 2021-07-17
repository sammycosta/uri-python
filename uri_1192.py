# URI Online Judge | 1192
# nome: Samantha Costa
N = int(input())
for i in range (N):
    sequencia = input().strip()
    n1 = int(sequencia[0:1])
    n2 = int(sequencia[2:])
    letra = sequencia[1:2]
    if n1 == n2: 
        r = n1*n2
    elif letra.isupper(): #se for maiuscula
        r = n2 - n1
    elif letra.islower(): # minuscula
        r = n1 + n2
    print(r)