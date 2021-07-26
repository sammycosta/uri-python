# URI Online Judge | 1547
# nome: Samantha Costa
N = int(input()) # casos de teste
for i in range(N):
    qt, s = [int(x) for x in input().split()] # quantidade de alunos, número secreto
    variavel = qt+1
    i = 0
    if 4 <= qt <= 10 and 1 <= s <= 100:
        tentativas = [int(x) for x in input().split()] # adivinhações
        if s in tentativas: #se alguém acertou o número exato
            while variavel == qt+1: #ele para quando consegue quem acertou primeiro.
                if s == tentativas[i]:
                    variavel = tentativas.index(tentativas[i]) + 1
                i +=1
            print(variavel)        
        else: #ngm acertou o numero exato. preciso encontrar quem acertou o mais próximo primeiro
            menordif = abs(s - tentativas[0]) # modulo da dif
            maisproximo = 0 
            for x in range(1, qt):
                if abs(s - tentativas[x]) < menordif: # ele ve o primeiro, se for igual n substitui
                    menordif = abs(s - tentativas[x]) # me da o modulo da diferença entre o numero
                    maisproximo = x
            print(maisproximo + 1)