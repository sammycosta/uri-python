# URI Online Judge | 2247
c = 0
while True:
    N = int(input())
    if N == 0:
        break
    c+=1
    print(f'Teste {c}')
    J = Z  = 0
    for i in range(N):
        a, b = [int(x) for x in input().split()]
        J += a 
        Z += b
        print(J-Z)
    (print())