# URI Online Judge | 1046
# nome: Samantha Costa
inicio, fim = [int(x) for x in input().split()]
duracao = 24 - inicio + fim 
if duracao > 24:
    duracao = duracao -24
if 24 >= duracao >= 1: 
    print(f'O JOGO DUROU {duracao} HORA(S)')