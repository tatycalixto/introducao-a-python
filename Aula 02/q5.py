numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("Número maior é ",numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Número maior é ",numero2)
else:
    print("Número maior é ",numero3)

if numero1 < numero2 and numero1 < numero3:
    print("Menor número ",numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("Menor número ",numero2)
else: 
    print("Menor número ", numero3)