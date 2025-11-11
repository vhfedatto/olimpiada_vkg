hora = int(input("Digite a hora: "))

if hora > 0 and hora <= 23:
    fluxo = input("Digite o fluxo [A, M, B]: ").upper()

    if hora >= 6 and hora <= 18:
        if fluxo == 'A':
            t = 60
        elif fluxo == 'M':
            t = 40  
        elif fluxo == 'B':
            t = 25
        else:
            print("Digite um fluxo válido.")
        
    elif hora >= 18 and hora <= 23 or hora >= 0 and hora <= 6:
            if fluxo == 'A':
                t = 40
            elif fluxo == 'M':
                t = 25  
            elif fluxo == 'B':
                t = 15
            else:
                print("Digite um fluxo válido.")

    print(f"Tempo de sinal verde: {t} segundos")

else:
    print("Hora inválida")