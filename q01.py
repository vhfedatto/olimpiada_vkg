while True:    
    hstr = input("Digite um horário: ")

    try:
        h = int(hstr)
        break
    except ValueError:
        print("Digite um número válido")

if h < 12:
    print("Dormindo")
elif h >= 12 and h <= 18:
    print("Brincando")
elif h > 18 and h <= 24:
    print("Pedindo comida")
else:
    print("Horário inválido")