valores = input().split()
c, q = valores
codigo = int(c)
quantidade = int(q)
preco = 4.00
if codigo == 2:
    preco = 4.50
if codigo ==3:
    preco = 5.00
if codigo ==4:
    preco = 2.00
if codigo ==5:
    preco = 1.50
print(f'Total: R$ {preco*quantidade:.2f}')