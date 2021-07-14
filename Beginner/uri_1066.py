numeros = []

for i in range(5): #cria os 5 inputs
    n = int(input())
    numeros.append(n) # o append guarda os inputs
par = 0
impar = 0
positivo = 0
negativo = 0
for c in range(5): 
    if numeros[c]%2 == 0:
        par +=1 # o += soma mais um a variável
    if numeros[c]%2 !=0:
        impar +=1
    if numeros[c] > 0:
        positivo +=1
    if numeros[c] < 0:
        negativo += 1
print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')