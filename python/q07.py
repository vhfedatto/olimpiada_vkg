n = int(input("Quantos valores: "))
notas = []
soma = 0

for i in range(n):
    nota = int(input())
    notas.append(nota)

    soma += nota

    m = soma / n

print(f"Média: {m:.2f}")
print(f"Maior: {max(notas)}")