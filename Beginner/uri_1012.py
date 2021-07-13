valor = input().split()
A, B, C = valor
print(f'TRIANGULO: {float(A)*float(C)/2:.3f}')
print(f'CIRCULO: {(float(C)**2)*3.14159:.3f}')
print(f'TRAPEZIO: {(float(A)+float(B))*float(C)/2:.3f}')
print(f'QUADRADO: {float(B)*float(B):.3f}')
print(f'RETANGULO: {float(A)*float(B):.3f}')