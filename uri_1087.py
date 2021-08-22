# URI Online Judge | 1087
while True:
    X1, Y1, X2, Y2 = [int(x) for x in input().split()]
    X = [X1, X2]
    Y = [Y1, Y2]
    c = 0
    if X1 == Y1 == X2 == Y2 == 0: # tudo 0
        break
    elif (X1 == X2) and (Y1 == Y2): # tao no mesmo lugar
        print('0')
        c = 2
    elif (X1 == X2) or (Y1 == Y2): #mesma linha ou mesma coluna, é só ir reto
        print('1')
        c = 3
    # movimentos na diagonal
    while X1 > 0 and Y1 > 0 and X1 <= 8 and Y1 <= 8:
        X1 += 1
        Y1 += 1
        if X1 == X2 and Y1 == Y2:
            c = 1
            break
    X1 = X[0]
    Y1 = Y[0]
    while X1 > 0 and Y1 > 0 and X1 <= 8 and Y1 <= 8:
        X1 -= 1
        Y1 -= 1
        if X1 == X2 and Y1 == Y2:
            c = 1
            break  
    X1 = X[0]
    Y1 = Y[0]  
    while X1 > 0 and Y1 > 0 and X1 <= 8 and Y1 <= 8:
        X1 += 1
        Y1 -= 1
        if X1 == X2 and Y1 == Y2:
            c = 1
            break  
    X1 = X[0]
    Y1 = Y[0]
    while X1 > 0 and Y1 > 0 and X1 <= 8 and Y1 <= 8:
        X1 -= 1
        Y1 += 1
        if X1 == X2 and Y1 == Y2:
            c = 1
            break
    if c == 1:
        print('1')
    elif c == 0:
        print('2')