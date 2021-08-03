# URI Online Judge | 1514
# nome: Samantha Costa
N, M = 1, 1 # N linhas, M colunas
matriz = list()
while (N and M) != 0:
    pontos, resolvidos, analise, analise2, analise3, analise4 = 0, 0, 0, 0, 0, 0
    N, M = [int(x) for x in input().split()] # numero de participantes, numero de problemas
    if N == M == 0:
        break
    for i in range(N):
        matriz.append([int(x) for x in input().split()]) # adiciona listas c as linhas
    # fazer a analise
    for j in range(M): # analisando cada problema, 2 e 3
        resolvidos = 0
        for i in range(N):
            resolvidos += matriz[i][j]
        if resolvidos != 0: #analisa se pelo menos uma pessoa respondeu
            analise2 += 1
        if resolvidos == N: #avalia se todo mundo acertou o problema
            analise3 = 1    
    for i in range(N): # analisando cada participante
        resolvidos = 0
        for j in range(M): # analiso cada coluna da linha
            resolvidos += matriz[i][j]
        if resolvidos == 0: #alguem n resolveu nd
            analise4 = 1
        if resolvidos == M: # alguem resolveu tudo
            analise = 1
    if analise != 1: #ngm resolveu tudo
        pontos += 1
    if analise2 >= M: #todos problemas foram resolvidos por alguem.
        pontos += 1
    if analise3 != 1:
        pontos += 1
    if analise4 != 1:
        pontos += 1
    print(pontos)
    matriz.clear()    
        