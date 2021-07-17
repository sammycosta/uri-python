# URI Online Judge | 1437
# nome: Samantha Costa 
N, result, direcoes, final = 1, 1, 0, 0
while N != 0:
    N = int(input())
    direcoes, result, final = 1, 1, 0
    if 1 <= N <= 1000:
        direcoes = input()
        for i in direcoes: #para cada caracter da string
            final = 'default'
            if i == 'D':
                result +=1
            if i == 'E':
                result += -1
            if result == 5:
                result = 1
            if result == 0:
                result = 4
        if result == 1:
            final = 'N'
        elif result == 2:
            final = 'L'
        elif result == 3:
            final = 'S'
        elif result == 4:
            final = 'O'
        print(final)            