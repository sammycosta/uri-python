# URI Online Judge | 2116
# nome: Samantha Costa
def eh_primoP1(num):
    qtd_divisores = 0
    primo = P1
    for d in range(1, num+1):  # fazer isso para todos os POSSÍVEIS divisores do número
            if num % d == 0:  # checando se d divide n
                qtd_divisores += 1
    if qtd_divisores > 2:
        primo += 0 #não é primo...não mudar a variável
    elif qtd_divisores == 2:  # é primo! divide por um e ele mesmo
        primo = num
    return primo
def eh_primoP2(num):
    qtd_divisores = 0
    primo = P2
    for d in range(1, num+1):  # fazer isso para todos os POSSÍVEIS divisores do número
            if num % d == 0:  # checando se d divide n
                qtd_divisores += 1
    if qtd_divisores > 2:
        primo += 0 #não é primo...não mudar a variável
    elif qtd_divisores == 2:  # é primo! divide por um e ele mesmo
        primo = num
    return primo
N, M = [int(x) for x in input().split()]
P1, P2 = 0,0
if 2 <= N and M <= 1000:
    for i in range (2, N+1):
        P1 = eh_primoP1(i)
    for c in range (2, M+1):
        P2 = eh_primoP2(c)   
    R = P1 * P2
    print(R)