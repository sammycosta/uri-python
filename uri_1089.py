# URI Online Judge | 1089
while True:
    N = int(input())
    if N == 0:
        break
    H = [int(x) for x in input().split()] # sequência de magnitudes das amostras
    H.append(H[0])
    r =[]
    picos = 0
    # os picos acontecem quando algo começa a descrescer ou crescer. se não estava antes, então n é.
    for i in range(0,N):
        if H[i] > H[i+1]: #descresce
            r.append('d')
        elif H[i+1] > H[i]: #cresce
            r.append('c')
    for c in range(len(r)):
        if c == (len(r) -1):
            if r[c] != r[0]:
                picos +=1
        else:
            if r[c] != r[c+1]:
                picos +=1
    print(picos)