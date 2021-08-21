# URI Online Judge | 1281
# nome: Samantha Costa
N = int(input()) # quantidade de idas à feira de dona Parcinova
for i in range (N):
    valor = 0
    produtos = {}
    M = int(input()) # quantidade de produtos que estão disponíveis para venda na feira
    for c in range (M):
        lista = input().split()
        produtos[lista[0]] = float(lista[1])
    P = int(input())
    if 1 <= P <= M:
        for x in range (P):
            produto, quantidade = input().split() 
            valor += produtos[produto] * int(quantidade)
    print(f'R$ {valor:.2f}')