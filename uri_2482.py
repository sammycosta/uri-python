# URI Online Judge | 2482
# nome: Samantha Costa

N = int(input()) # quantidade de traduções da palavra "Feliz Natal" existentes na entrada.
dicio = {}
if 1 <= N <= 100:
    for i in range(N):
        lingua = input().strip()
        traducao = input().strip()
        dicio[lingua] = traducao
    M = int(input()) # quantidade de crianças
    if 1 <= M <= 100:
        for c in range(M):
            nome = input()
            linguainput = input()
            print(nome)
            print(dicio[linguainput]+'\n')
