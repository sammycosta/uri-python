linha1 = input().split()
linha2 = input().split()
a, b, c= linha1
x, y, z= linha2
qtdmax = (int(y)//int(b))*(int(x)//int(a))*(int(z)//int(c))

print(f'{qtdmax}')
