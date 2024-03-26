numero = int(input("Digite um número: "))
contador = 1
soma = 0

while contador <=numero:
    if contador%2==0:
        soma +=contador #soma = soma + contador
    contador +=1 #contador = contador + 1
print("A soma dos número pares é: ",soma)
