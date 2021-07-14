# URI Online Judge | 2434
# nome: Samantha Costa
N, S = [int(x) for x in input().split()]
menorsaldo = S
if (1 <= N <= 30) and (-10**3 <= S <= 10**3):
    for i in range (N):
        movim = int(input())
        S += movim 
        if S < menorsaldo:
                menorsaldo = S
    print(menorsaldo)            
    