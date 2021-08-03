# URI Online Judge | 1184
# nome: Samantha Costa
O = input().upper() # soma ou media
soma, media, count = 0, 0, 0
matriz = list()
for i in range (12): #faz 12 listas de 12 dentro
    matriz.append(list(range(12)))

for linha in range(12):
    for coluna in range(12):
        matriz[linha][coluna] = float(input())
        
for linha in range(1,12): #linha um soma ate coluna 1, dois ate coluna 2,etc
    for coluna in range(linha):
        soma += matriz[linha][coluna]
        count +=1
if O == 'S':
    print(f'{soma:.1f}')
elif O == 'M':
    media = soma/count
    print(f'{media:.1f}')    