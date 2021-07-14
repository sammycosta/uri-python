dias = int(input())
ano = dias // 365
mes = (dias - (ano*365)) // 30
diasr = dias - (ano*365) - (mes*30)

print (f'{ano} ano(s)')
print (f'{mes} mes(es)')
print (f'{diasr} dia(s)')