# URI Online Judge | 1134
alcool = gasolina = diesel = 0
while True:
    N = int(input())
    while N != 1 and N != 2 and N != 3 and N != 4:
        N = int(input())
    if N == 1:
        alcool += 1
    elif N == 2:
        gasolina += 1
    elif N == 3:
        diesel +=1
    elif N == 4:
        break 
print(f'''MUITO OBRIGADO
Alcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}''')