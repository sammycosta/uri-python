# URI Online Judge | 2417
# v = vitórias, e = empates, s = saldo de gols
# nome: Samantha Costa
Cv, Ce, Cs, Fv, Fe, Fs = [int(x) for x in input().split()]
pontos_car, pontos_fla, resultado = 0, 0, 0
if (0 <= (Cv and Ce and Fv and Fe) <= 100) and (-1000 <= (Cs and Fs) <= 1000):
    pontos_car = (Cv*3) + Ce
    pontos_fla = (Fv*3) + Fe 
    if pontos_car > pontos_fla:
        resultado = 'C'
    elif pontos_fla > pontos_car:
        resultado = 'F'
    elif pontos_fla == pontos_car:
        if Cs > Fs:
            resultado = 'C'
        elif Fs > Cs:
            resultado = 'F'
        elif Fs == Cs:
            resultado = '='
    print(resultado)