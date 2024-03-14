salario = float(input("Digite o valor do salário: "))
perc_aumento = float(input("Digite o valor do perc de aumento: "))
valor_aumento = (salario*perc_aumento)/100
salario_final = salario + valor_aumento
print(" O valor do aumento é R$ ",valor_aumento)
print("O valor do salário com aumento é de R$ ", salario_final)