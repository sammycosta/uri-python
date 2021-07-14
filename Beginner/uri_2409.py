A, B, C = input().split()
H, L = input().split()
A = int(A)
B = int(B)
C = int(C)
H = int(H)
L = int(L)
if 1 <= (A and B and C) <= 300 and 1 <= (H and L) <= 250:
    if A <= H and B <= L:
        print('S')
    elif A <= H and C <= L:
        print('S')
    elif B <= H and A <= L:
        print('S')
    elif B <= H and C <= L:
        print('S')
    elif C <= H and A <= L:
        print('S')
    elif C <= H and B <= L:
        print('S')
    else:
        print('N')
else:
    print('error')