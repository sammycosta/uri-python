# URI Online Judge | 2091
# nome: Samantha Costa
while True:
    N = int(input())
    if N == 0:
        break
    elif 1 <= N <= 10**5:
        numeros = [int(x) for x in input().split()]
        auxiliar = []
        for i in numeros:
            if i in auxiliar:
                auxiliar.remove(i) # caso ja tenha esse numero, remover ele de la. fecha o par
            else:
                auxiliar.append(i)
        print(auxiliar[0])