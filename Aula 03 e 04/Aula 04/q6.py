palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite uma palavra: ")

palavra1 = palavra1.lower()
palavra2 = palavra2.lower()

#exibindo o conteúdo da variável e o tamanho da string
print(palavra1,len(palavra1))
print(palavra2,len(palavra2))

if palavra1 == palavra2:
    print("As strings possuem o mesmo conteúdo!")
else:
    print("As astring não possuem o mesmo conteúdo")
if len(palavra1) == len(palavra2):
    print("As strings possuem o mesmo tamanho!")  
else:
    print("As strings não possuem o mesmo tamanho") 