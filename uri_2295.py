# URI Online Judge | 2295
# nome: Samantha Costa de Sousa
A, G, ra, rg = input().split()
A = float(A) #preço por litro de álcool
G = float(G) #preço por litro da gasolina
ra = float(ra) #rendimento (km/l) do carro utilizando álcool
rg = float(rg) #rendimento (km/l) do carro utilizando gasolina.
preco_alcool = A / ra
preco_gasosa = G / rg
if (0.01 <= A and G <= 10.00) and (0.01 <= ra and rg <= 20.00):
    if preco_alcool > preco_gasosa:
        print('G')
    elif preco_gasosa > preco_alcool:
        print('A')
    elif preco_gasosa == preco_alcool:
        print('G')
else:
    print('error')