# Nome: Samantha Costa de Sousa 
def escada_ligada(somadostempos, tempo_anterior, T):
    if (tempo_anterior + 10) > T: #ainda tem uma pessoa na escada quanto essa tá?
        somadostempos += T - tempo_anterior #tempo extra que essa nova pessoa precisa p terminar os 10
    else: # não tem niguém, ligada 10s pra levar
        somadostempos += 10  
    tempoligada = somadostempos
    return tempoligada
somadostempos, tempo_anterior, tempoligada = 0, -10,0 
N = int(input())
if 1 <= N <= 1000: #restrição de pessoas
    for i in range(N):
        T = int(input())
        tempoligada += escada_ligada(somadostempos, tempo_anterior, T)
        tempo_anterior = T      
    print(tempoligada)