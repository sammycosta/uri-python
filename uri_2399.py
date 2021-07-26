# URI Online Judge | 2399
# nome: Samantha Costa
N = int(input()) # numero de celulas
if 1 <= N <= 50:
    mina = list(range(N)) # faço a lista
    for i in range(N):
        mina[i] = 0 # zero tds componentes da lista
    for i in range(N):
        v = int(input()) # 0 ou 1
        if v == 1:
            mina[i] += 1
            if i == 0: # nao existe anterior
                mina[i+1] +=1
            elif i == (N-1): # nao existe proximo
                mina[i-1] +=1
            elif i != 0 and i != (N-1):
                mina[i+1] +=1
                mina[i-1] +=1
    for x in range(N):
        print(mina[x])