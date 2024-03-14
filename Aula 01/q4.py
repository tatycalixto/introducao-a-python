valor_mercadoria = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o valor do desconto: "))
valor_desconto = (valor_mercadoria*desconto)/100
valor_final = valor_mercadoria-valor_desconto
print("O Valor do desconto é R$ ",valor_desconto)
print("O Valor total a pagar é R$ ",valor_final)
