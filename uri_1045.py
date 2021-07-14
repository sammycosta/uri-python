valores = input().split()
a, b, c = valores
n1 = float(a)
n2 = float(b)
n3 = float(c)
# ordenando A, B, C
A = n1
B = n1
C = n1
if n2 > n1 and n2 > n3:
    A = n2
if n3 > n1 and n3 > n2:
    A = n3
if n2 < n1 and n2 < n3:
    C = n2
if n3 < n2 and n3 < n1:
    C = n3
if n1 < n2 < n3 or n3 < n2 < n1:
    B = n2
if n1 < n3 < n2 or n2 < n3 < n1:
    B = n3

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == (B**2 + C**2):
        print('TRIANGULO RETANGULO')
    if A**2 > (B**2 + C**2):
        print('TRIANGULO OBTUSANGULO')
    if A**2 < (B**2 + C**2):
        print('TRIANGULO ACUTANGULO')
    if A == B == C:
        print('TRIANGULO EQUILATERO')
    if A == B != C or A == C != B or B == C != A:
        print('TRIANGULO ISOSCELES')
