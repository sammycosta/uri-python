duracao = int(input())
horas = duracao//(60*60)
minutos = (duracao - (horas*60*60))//60
segundos = duracao - (minutos*60) -(horas*60*60)

print(f'{horas}:{minutos}:{segundos}')