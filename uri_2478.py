# URI Online Judge | 2478
X = int(input())
presentes = {} # dicionário
for i in range(X):
    nome, a, b, c = input().lower().split()
    presentes[nome] = [a, b, c]
while True:
    try:
        N, P = input().lower().split() #nome da pessoa, presente
        if N in presentes.keys():
            if P in presentes[N]:
                print('Uhul! Seu amigo secreto vai adorar o/')
            else:
                print('Tente Novamente!')
        else:
            print('Tente Novamente!')
    except EOFError:
        break