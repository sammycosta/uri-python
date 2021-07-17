# URI Online Judge | 1049
osso = input().lower()
classe = input().lower()
alimento = input().lower()

if osso == 'vertebrado':
    if classe == 'ave':
        if alimento == 'carnivoro':
            print('aguia')
        elif alimento == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if alimento == 'onivoro':
            print('homem')
        elif alimento == 'herbivoro':
            print('vaca')
elif osso == 'invertebrado':
    if classe == 'inseto':
        if alimento == 'hematofago':
            print('pulga')
        elif alimento == 'herbivoro':
            print('lagarta')
    elif classe == 'anelideo':
        if alimento == 'hematofago':
            print('sanguessuga')
        elif alimento == 'onivoro':
            print('minhoca')