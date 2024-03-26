notas = []

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

soma = sum(notas)
media = soma/4
print("A média é: ", media)