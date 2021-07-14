# URI Online Judge | 1154
# nome: Samantha Costa
n, i, soma  = 2, 0, 0
while True:
    n = int(input())
    if n >= 0:
        i += 1
        soma += n
    else:
        print(f'{soma / i:.2f}')
        break