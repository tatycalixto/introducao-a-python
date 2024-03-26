numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

qtd_pares = 0

for i in range (5):
    if numeros[i]%2==0:
        qtd_pares +=1 #qtd_pares = qtd_pares + 1

print("A lista de números tem ",qtd_pares, " número pares!")