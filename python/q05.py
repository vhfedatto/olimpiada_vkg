contador = 0

while True:
    n = int(input("Número: "))
    c = 0

    if n > 1:
        for i in range(1, n+1):
            x = n % i

            if x == 0:
                c += 1
            
        if c == 2:
            contador += 1
    elif n <= 0:
        break

print(contador)