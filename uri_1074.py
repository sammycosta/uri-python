N = int(input())
parouimpar, posiouneg = 0, 0
if N < 10000:
    for i in range(0, N):
        X = int(input())
        if -10**7 < X < 10**7:
            if X != 0:
                if X % 2 != 0:
                    parouimpar = 'ODD'
                if X % 2 == 0:
                    parouimpar = 'EVEN'
                if X > 0:
                    posiouneg = 'POSITIVE'
                if X < 0:
                    posiouneg = 'NEGATIVE'
                print(f'{parouimpar} {posiouneg}')
            else:
                print('NULL')
        else:
            print('Valor não aceito.')
else:
    print('Valor não aceito.')