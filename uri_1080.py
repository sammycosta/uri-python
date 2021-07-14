posicao, X = 0,0
for i in range(100):
    A = int(input())
    if A > X: #se o input for maior que o X
        maior = A #o maior vira o input
        posicao = i+1 #a posição é escrita
        X = A #cria-se um novo X substituindo o anterior a cada maior que é colocado
print(X)
print(posicao)
