linha1 = input().split()
linha2 = input().split()
x1, y1 = linha1
x2, y2 = linha2

formula = ((float(x2) - (float(x1)))**2 + (float(y2) - float(y1))**2 )**(1/2)
print(f'{formula:.4f}')
