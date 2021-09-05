# URI Online Judge | 1129
while True:
    N = int(input())
    if N == 0:
        break
    for i in range(N):
        A, B, C, D, E = [int(x) for x in input().split()]
        dicio = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}
        correta = []
        for c, v in dicio.items(): # c dá a key e v dá o valor
            if v <= 127:
                correta.append(c)
        if len(correta) > 1:
            print('*')
        elif len(correta) == 1:
            print(correta[0])
        else:
            print('*')