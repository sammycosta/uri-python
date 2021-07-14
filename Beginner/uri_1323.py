# uri: https://www.urionlinejudge.com.br/judge/pt/problems/view/1323
# nome: Samantha Costa de Sousa
for i in range(1, 10000000000000):
    N = int(input()) # inputa qts vezes quiser
    x= 0 #reinicia o x
    for c in range(N, -1, -1): # do numero do input ate 1, 8,7,6,5,4,3,2,1,0
        x += (N - c)**2 #faz o cálculo do número de quadrados até o fim
    if 1 <= N <= 100:
        print(x)
    else:
        break #finaliza o cód quando envia 0