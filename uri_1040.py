# URI Online Judge | 1040
nota1, nota2, nota3, nota4 = [float(x) for x in input().split()]

media = (nota1*2 + nota2*3 + nota3*4 + nota4)/10
exame, result = 0, 0
if 6.9 >= media >= 5:
    print(f'''Media: {media:.1f}
Aluno em exame.''') 
    exame = float(input())
    media2 = (media + exame) / 2
    print(f'Nota do exame: {exame:.1f}')
    if media >= 5:
        result = 'aprovado'
    elif media <= 4.9:
        result = 'reprovado'
    print(f'Aluno {result}.')
    print(f'Media final: {media2:.1f}')
else:    
    if media >= 7:
        result = 'aprovado'
    elif media < 5:
        result = 'reprovado'
    print(f'Media: {media:.1f}')
    print(f'Aluno {result}.')
