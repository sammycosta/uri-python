# URI Online Judge | 1318
while True:
    N, M = [int(x) for x in input().split()] #bilhetes originais, pessoas na festa
    if N == M == 0:
        break
    T = [int(x) for x in input().split()] # números dos bilhetes contidos no pacote que o diretor lhe deu
    c =[] #lista com os repetidos
    for i in T:
        count = T.count(i)
        if count > 1:
            c.append(i)
    c = list(dict.fromkeys(c)) #cria um dicionario, dicionario n repete keys, volta pra lista
    print(len(c))