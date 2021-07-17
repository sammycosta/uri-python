# URI Online Judge | 1044
A, B = [int(x) for x in input().split()]

if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')