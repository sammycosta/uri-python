# URI Online Judge | 2139
# ano bissexto -- natal no dia 360
while True:
    try:
        dias31 = [1, 3, 5, 7, 8, 10, 12]
        dias30 = [4, 6, 9, 11]
        mes, dia = [int(x) for x in input().split()]
        if mes == 12 and dia == 24:
            print('E vespera de natal!')
        elif mes == 12 and dia == 25:
            print('E natal!')
        elif mes == 12 and dia >25:
            print('Ja passou!')
        else:
            dias = 0
            for i in range(1, mes):
                if i in dias31:
                    dias += 31
                elif i in dias30:
                    dias+= 30
                else:
                    dias+= 29
            dias+= dia 
            print(f'Faltam {360-dias} dias para o natal!')
    except EOFError:
        break