n = int(input("Digite um valor: "))
cont_par = 0 
soma_par = 0

for i in range(1,n+1):
    if i%2==0:
        cont_par +=1
        soma_par+=i

media = soma_par/cont_par
print("A média é: ",media)
