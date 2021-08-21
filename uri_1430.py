# URI Online Judge | 1430
# nome: Samantha Costa
dicio = {}
dicio['W'] = 1
dicio['H'] = 1/2
dicio['Q'] = 1/4
dicio['E'] = 1/8
dicio['S'] = 1/16
dicio['T'] = 1/32
dicio['X'] = 1/64
while True:
    caso = input()
    if caso == '*':
        break
    elif 3 <= len(caso) <= 200:
        compassos = []
        pos = 1
        corretos = 0
        compassos = caso[1:(len(caso)-1)].split('/')
        for i in compassos: #para cada compasso
            soma = 0
            for nota in i: #cada letra do compasso
                soma += dicio[nota]
            if soma == 1:
                corretos += 1
        print(corretos)        