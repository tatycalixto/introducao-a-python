media = float(input("Digite uma média de 0-10:"))

if media >=7:
    print("Aprovado(a)!")
elif media >=3 or  media >7:
    print("Pode fazer a final!")
else:
    print("Reprovado(a)")