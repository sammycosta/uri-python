# URI Online Judge | 1261
# nome: Samantha Costa
M, N = [int(x) for x in input().split()] #numero de palavras, quantidade desc
if M <= 1000 and N <=100:
    haypoint = {}
    for i in range(M):
        palavra, dolar = input().split()
        if (len(palavra) <= 16) and (0 <= int(dolar) <= 10**6):
            haypoint[palavra.lower()] = int(dolar)
    for c in range(N):
        valor = 0
        while True:
            linha = input()
            if linha == '.':
                break    
            for i in haypoint.keys():
                valor += (linha.count(i)) * (haypoint[i])
        print(valor)     
