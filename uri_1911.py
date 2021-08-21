# URI Online Judge | 1911
# nome: Samantha Costa
while True:
    N = int(input())
    if N == 0:
        break
    dicio = {}
    falsas = 0
    if 1 <= N <= 50:
        for i in range(N):
            nome, assinatura = input().split()
            dicio[nome] = assinatura
        M = int(input())
        if 0 <= M <= N: 
            for i in range(M):
                nome, assinatura = input().split()
                c, erradas = 0, 0
                for letra in assinatura:
                    variavel = dicio[nome]
                    if variavel[c] != letra:
                        erradas += 1
                    c += 1
                if erradas > 1:
                    falsas +=1
            print(falsas)