#Basics
matriz = []
soma = 0       #calcular a diagonal
media = 0      #calcular a média
maiores = 0    #números maiores que a média

#Valor inicial
tam = int(input("Qual o tamanho da matriz? "))

#Adição de valores da matriz
for i in range(tam):
    for j in range(tam):
        num = int(input(f"Digite o número {j+1} da coluna {i+1}: "))
        matriz.append(num)

#Soma da diagonal
ind = tam-1
for k in range(tam):
    soma += matriz[ind]
    ind += tam-1

#Calculo da média
media = sum(matriz) / len(matriz)

for l in matriz:
    if l > media:
        maiores +=1

print("Soma da diagonal secundária:", soma)
print("Valores maiores que a média:", maiores)

