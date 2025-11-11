soma = 0
while True:
    ns = input("número: ")

    try:
        n = int(ns)
        if n == 0 or n < 0:
            print(soma)
            break
        soma += n

    except ValueError:
        print("Número inválido")