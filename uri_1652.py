# URI Online Judge | 1652
L, N = [int(x) for x in input().split()] 
irregulares = {} #dicionário
consoantes = "bcdfghjklmnpqrstvwxyz"
for i in range(L): #descrição das palavras irregulares e sua forma plural
    singular, plural = input().split() #str
    irregulares[singular] = plural
for c in range(N): #input de uma palavra e recebe o plural seguindo as regras
    palavra = input().strip()
    if palavra in irregulares.keys(): #regra 1
        print(irregulares[palavra])
    else:
        ultima = len(palavra)-1 #posição da última letra
        if palavra[ultima:] == 'y' and palavra[ultima-1:ultima] in consoantes: #regra 2 
            palavra = palavra[:ultima]+'ies' # sem o y e com ies
            print(palavra)
        elif palavra[ultima:] in 'osx' or (palavra[ultima-1:] == 'ch') or (palavra[ultima-1:] == 'sh'): #regra 3
            palavra = palavra+'es'
            print(palavra)
        else: #regra 4
           palavra = palavra +'s'
           print(palavra)          