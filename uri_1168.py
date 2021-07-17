# URI Online Judge | 1168
# nome: Samantha Costa
N = int(input())
leds = 0
for i in range(N):
    leds = 0 #zera a contagem
    V = input()
    for c in V:
        if c == '1':
            leds += 2
        elif c == '2' or c == '3' or c == '5':
            leds += 5
        elif c == '4':
            leds += 4
        elif c == '6' or c == '9' or c == '0':
            leds += 6
        elif c == '7':
            leds += 3
        elif c == '8':
            leds += 7
    print(f'{leds} leds')