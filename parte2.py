usuario = (input("Usuario:"))
senha = (input('Senha:'))

while senha != "Senha123@":
    senha = (input('Senha incorreta, digite novamente:'))
    if(senha == "Senha123@"):
        print("Você esta logado")
    
