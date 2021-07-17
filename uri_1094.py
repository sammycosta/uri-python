# URI Online Judge | 1094
# nome: Samantha Costa
N = int(input())
total, tcoelhos, tratos, tsapos, pcoelhos, pratos, psapos = 0, 0, 0, 0, 0, 0, 0
for i in range(N):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)
    Tipo = Tipo.upper()
    if 1 <=  Quantia <= 15:
        if Tipo == 'R': #ratos
            total += Quantia 
            tratos += Quantia
        elif Tipo == 'C': #coelhos
            total += Quantia
            tcoelhos += Quantia
        elif Tipo == 'S': #sapos
            total += Quantia
            tsapos += Quantia
pcoelhos = tcoelhos*100/total
pratos = tratos*100/total
psapos = tsapos*100/total
print(f'''Total: {total} cobaias
Total de coelhos: {tcoelhos}
Total de ratos: {tratos}
Total de sapos: {tsapos}
Percentual de coelhos: {pcoelhos:.2f} %
Percentual de ratos: {pratos:.2f} %
Percentual de sapos: {psapos:.2f} %''')
