X = int(input())
if 1 <= X <= 1000:
    for i in range(1, X+1, 2):
        print(i)
else:
    print('Valor não aceito.')