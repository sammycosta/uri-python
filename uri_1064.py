# URI Online Judge | 1064
# nome: Samantha Costa
soma, positivos = 0, 0
for i in range(6):
    n = float(input())
    if n > 0:
        soma += n
        positivos += 1

media = soma/positivos

print(f'{positivos} valores positivos')
print(f'{media:.1f}')