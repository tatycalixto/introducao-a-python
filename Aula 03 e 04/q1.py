usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

while usuario == senha:
    print("Senha e usuário iguais! Digite novamente")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua e senha: ")

print("Seu usuário é: ",usuario)
print("Sua senha é: ",senha)