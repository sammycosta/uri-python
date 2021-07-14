# URI Online Judge | 1150
# nome: Samantha Costa
X = int(input())
Z = int(input())
count = 2
Y = X
while Z <= X:
    Z = int(input())

while True:
    if X + (Y+1) < Z: 
        Y += Y + 1
        count += 1
    else:
        print(count)
        break