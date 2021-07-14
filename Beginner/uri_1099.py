# URI Online Judge | 1099
# nome: Samantha Costa
N = int(input())
for i in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    soma = 0
    if X > Y:
        X = X-1 # para ir até o número anterior a X.
        while X > Y:
            if (Y + 1)%2 != 0:
                soma += Y + 1
                Y = Y + 1
            else:
                Y = Y + 1
        print(soma)
    elif Y > X:
        Y = Y-1 # para ir até o número anterior a Y.
        while Y > X:
            if (X + 1)%2 != 0:
                soma += X + 1
                X = X + 1
            else:
                X = X + 1
        print(soma)
    elif Y == X:
        print(soma)
