# URI Online Judge | 1467
while True:
    try:
        A, B, C = [int(x) for x in input().split()]
        if A == B == C:
            print('*')
        elif (A == B) and A!= C: 
            print('C')
        elif (A == C) and A!= B: 
            print('B')
        elif (B == C) and B != A: 
            print('A')            
    except EOFError:
        break
    