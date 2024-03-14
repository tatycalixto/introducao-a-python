km_rodados = float(input("Digite o valor em KM rodados: "))
qtd_dias = int(input("Digite a quantidade de dias: "))
valor_aluguel = qtd_dias * 60
valor_km = km_rodados * 0.15
valor_final = valor_aluguel + valor_km
print(valor_final)
