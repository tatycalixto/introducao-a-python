p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ")
p4 = input("Devia para a vítima? ")
p5 = input("Já trabalhou com a vítima? ")

respostas = 0

if p1 == 's':
    respostas = respostas + 1 
if p2 == 's':
    respostas = respostas + 1
if p3 == 's':
    respostas = respostas + 1 
if p4 == 's':
    respostas = respostas + 1
if p5 == 's':
    respostas = respostas + 1

if respostas == 2:
    print("Pessoa Suspeita!")
elif respostas == 3 or respostas == 4:
    print("Pessoa Cúmplice!")
elif respostas == 5:
    print("Pessoa Assassina!")
else:
    print("Pessoa Inocente!")