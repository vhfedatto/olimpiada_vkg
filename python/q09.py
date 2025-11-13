#Basics
matriz = []
soma = 0
ind = 0

#Valor inicial
tam = int(input("Qual o tamanho da matriz? "))

#Adição de valores da matriz
for i in range(tam):
    for j in range(tam):
        num = int(input(f"Digite o número {j+1} da coluna {i+1}: "))
        matriz.append(num)

#Soma da diagonal
for k in range(tam):
    soma += matriz[ind]
    ind += tam+1

print(soma)
