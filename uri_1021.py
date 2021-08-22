# URI Online Judge | 1021
N = float(input())*100
lista = [10000,5000,2000,1000,500,200,100,50,25,10,5,1]
notas = {}
for i in (lista):
    R = N // i
    N -= R*i 
    notas[i] = R
print('NOTAS:')
for i in lista[0:6]:
    print(f'{int(notas[i])} nota(s) de R$ {(i/100):.2f}')
print('MOEDAS:')
for c in lista[6:12]:
    print(f'{int(notas[c])} moeda(s) de R$ {(c/100):.2f}')