numeros = []
num = []
rep = 0

qtde = int(input("Quantos números: "))

for i in range(qtde):
    n = int(input("Digite um número: "))

    if n in numeros:
        if n not in num:
            rep += 1 
        num.append(n)
    

    numeros.append(n)

print(rep)