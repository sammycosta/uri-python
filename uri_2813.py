# URI Online Judge | 2813
# SD: IDA / SN: VOLTA
# nome: Samantha Costa
N = int(input())
C, E = 0,0
casa, escritorio = 0,0
if 1 <= N <= 1000:
    for i in range(N):
        SD, SN = input().split()
        if SD == 'chuva':
            if casa == 0: #se nao tem guarda chuva na casa
                C += 1 #precisa comprar um pra casa
                escritorio +=1 #e dps da chuva ele fica no escritorio
            elif casa >= 1: #se tem um na casa
                casa += -1 #ele sai da casa
                escritorio += 1 #e vai pro escritorio
        if SN == 'chuva': 
            if escritorio == 0: #se n tem no escritorio
                E += 1 #uma pro escritorio
                casa += 1 #que vai pra casa               
            elif escritorio >= 1: # tem uma no escritorio
                escritorio += -1 # tira do escritorio
                casa +=1 #vai pra casa
    print(f'{C} {E}')            
    