# URI Online Judge | 2376
# nome: Samantha Costa
M, N, winner1, winner2, winner3, winner4, winner5, winner6 = 0,0,0,0,0,0,0,0
winner7, winner8, winner9, winner10, winner11, winner12, winner13 = 0,0,0,0,0,0,0
winner14, winner15 = 0,0
for i in range(0,15):
    M, N = [int(x) for x in input().split()]
    if (0 <= M and N <=20) and M != N:
        if M > N:
            if i == 0:
                winner1 = 'A'
            if i == 1:   
                winner2 = 'C' 
            if i == 2:
                winner3 = 'E'    
            if i == 3:
                winner4 = 'G'    
            if i == 4:
                winner5 = 'I'    
            if i == 5:
                winner6 = 'K'    
            if i == 6:
                winner7 = 'M'        
            if i == 7:    
                winner8 = 'O'
            if i == 8:
                winner9 = winner1
            if i == 9:
                winner10 = winner3 
            if i == 10:
                winner11 = winner5
            if i == 11:
                winner12 = winner7
            if i == 12:
                winner13 = winner9
            if i == 13:
                winner14 = winner11
            if i == 14:
                winner15 = winner13
                
        elif N > M:
            if i == 0:
                winner1 = 'B'
            if i == 1:   
                winner2 = 'D' 
            if i == 2:
                winner3 = 'F'    
            if i == 3:
                winner4 = 'H'    
            if i == 4:
                winner5 = 'J'    
            if i == 5:
                winner6 = 'L'    
            if i == 6:
                winner7 = 'N'        
            if i == 7:    
                winner8 = 'P'
            if i == 8:
                winner9 = winner2
            if i == 9:
                winner10 = winner4
            if i == 10:
                winner11 = winner6
            if i == 11:
                winner12 = winner8
            if i == 12:
                winner13 = winner10
            if i == 13:
                winner14 = winner12
            if i == 14:
                winner15 = winner14

print(winner15)