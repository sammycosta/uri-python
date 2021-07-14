# URI Online Judge | 2927
#A -> alunos \\ C -> computadores \\ X -> pc queimados por Caio \\ Y -> pc sem compilador
# nome: Samantha Costa
A, C, X, Y = [int(x) for x in input().split()]
pcs_disponiveis = C - (X+Y) - 1 #-1 é o pc que o prof vai usar.
resultado = 'default'
if 0 < A and Y and X <= C <= 1000:
    if pcs_disponiveis >= A:
        resultado = 'Igor feliz!'
    elif A > pcs_disponiveis:
        resultado = 'Igor bolado!'
        if X > (Y/2):
            resultado = 'Caio, a culpa eh sua!'
    print(resultado)