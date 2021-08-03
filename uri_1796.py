# URI Online Judge | 1796 | [PJ]
# nome: Samantha Costa
Q = int(input())
V = [int(x) for x in input().split()]
sim, nao = 0,0
if (4 <= Q <= 233000):
    for i in range(len(V)):
        if V[i] == 1:
            nao +=1
        elif V[i] == 0:
            sim += 1

    if sim > nao:
        print('Y')
    else: 
        print('N')