# URI Online Judge | 1043
A, B, C = [float(x) for x in input().split()]
if A >= (B + C) or B >= (A + C) or C >= (A + B): # não forma triangulo
    area = (A + B) * C / 2
    print(f'Area = {area:.1f}')
else:
    perimetro = A + B + C 
    print(f'Perimetro = {perimetro:.1f}')
    