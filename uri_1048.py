# URI Online Judge | 1048

sal = float(input())

if 800 >= sal > 400:
    p = '12 %'
    reajuste = sal*0.12
    novosal = sal + reajuste
elif 400 >= sal >= 0:
    p = '15 %'
    reajuste = sal*(15/100)
    novosal = sal + reajuste
elif 1200 >= sal > 800:
    p = '10 %'
    reajuste = sal*0.10
    novosal = sal + reajuste
elif 2000 >= sal > 1200:
    p = '7 %'
    reajuste = sal*0.07
    novosal = sal + reajuste
elif sal > 2000:
    p = '4 %'
    reajuste = sal*0.04
    novosal = sal + reajuste
print(f'Novo salario: {novosal:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {p}')