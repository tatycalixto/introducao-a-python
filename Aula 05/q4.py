nomes = []
#inserir os nomes em uma lista
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome.upper())

nomes.sort()
print("Nomes em Ordem Alfabética: ",nomes)