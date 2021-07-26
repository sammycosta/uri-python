# URI Online Judge | 1471
# nome: Samantha Costa
while True:
    try:
        N, R = [int(x) for x in input().split()] #mergulhou, e retornou
        mergulhadores = list(range(1, N+1))
        retornaram = [int(c) for c in input().split()]
        for i in range(R):
            mergulhadores.remove(retornaram[i])
        if mergulhadores == []:
            print('*')
        else:
            for i in range(len(mergulhadores)):
                print(mergulhadores[i], end = ' ')
            print('')
    except EOFError:
        break