# URI Online Judge | 2057
S, T, F = input().split()
S, T, F = int(S), int(T), int(F)
horario = S + T + F
if (0 <= S <= 23) and (1 <= T <= 12) and (-5 <= F <= 5):
    if horario >= 24:
        horario = horario -24
    if horario <0:
        horario = horario +24
    print(horario)