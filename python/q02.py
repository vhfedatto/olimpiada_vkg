print("1 - Café Preto - 3,00")
print("2 - Cappuccino - 4,50")
print("3 - Mocaccino - 5,00")
print("4 - Chocolete Quente - 4,00")

bebida = input("Código da bebida: ")
valorStr = input("Valor: ")

try: 
    bebida = int(bebida)
except ValueError:
    print("Código inválido! Digite um inteiro")

while True:
    try:
        valor = float(valorStr)
        break
    except ValueError:
        print("Valor inválido. Digite um valor float")


if bebida == 1:
    troco = valor - 3

    if troco < 0:
        print("Valor insuficiente!")
    else:
        print(f"\nBebida {bebida}")
        print(f"Troco: R$ {troco:.2f}\n")
elif bebida == 2:
    troco = valor - 4.50

    if troco < 0:
        print("Valor insuficiente!")
    else:
        print(f"\nBebida {bebida}")
        print(f"Troco: R$ {troco:.2f}\n")
elif bebida == 3:
    troco = valor - 5

    if troco < 0:
        print("Valor insuficiente!")
    else:
        print(f"\nBebida {bebida}")
        print(f"Troco: R$ {troco:.2f}\n")
elif bebida == 4:
    troco = valor - 4

    if troco < 0:
        print("Valor insuficiente!")
    else:
        print(f"\nBebida {bebida}")
        print(f"Troco: R$ {troco:.2f}\n")
else:
    print("Código inválido!")