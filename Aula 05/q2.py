numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

#soma
soma = sum(numeros)

mult = 1
for i in range(5):
    mult*=numeros[i]

print("A soma: ",soma)
print("A multiplicação: ",mult)
print(numeros)
