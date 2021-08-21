# URI Online Judge | 1763
# nome: Samantha Costa
dicio = {}
dicio['brasil'] = dicio['portugal'] = 'Feliz Natal!'
dicio['alemanha'] = 'Frohliche Weihnachten!'
dicio['austria']  = 'Frohe Weihnacht!'
dicio['coreia']   = 'Chuk Sung Tan!'
dicio['grecia']   = 'Kala Christougena!'
dicio['estados-unidos']  = dicio['inglaterra']  = dicio['australia'] = dicio['antardida'] = dicio['canada'] = 'Merry Christmas!'
dicio['suecia'] = 'God Jul!'
dicio['turquia']= 'Mutlu Noeller'
dicio['argentina'] = dicio['chile']   = dicio['mexico']  = dicio['espanha']  = 'Feliz Navidad!'
dicio['irlanda']  = 'Nollaig Shona Dhuit!'
dicio['belgica'] = 'Zalig Kerstfeest!'
dicio['italia'] = dicio['libia']     ='Buon Natale!'
dicio['siria']     = dicio['marrocos']   =  'Milad Mubarak!'
dicio['japao']   = 'Merii Kurisumasu!'
while True:
    try:
        pais = input()
        print(dicio.get(pais, '--- NOT FOUND ---'))
    except EOFError:
        break