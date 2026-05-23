usuarios = {
    "gustavo": {"senha": "123"},
    "admin": {"senha": "999"}
}

def adicionar_usuario():
    usuario = input("Escreva o nome: ")
    senha = input("Escreva a senha: ")

    if usuario == "":
        return "Digite um nome!"

    if senha == "":
        return "Digite uma senha!"

    elif usuario in usuarios:
        return "Usuário já existente"
    else:
        usuarios[usuario] = {"senha": senha}
        return "Usuário criado com sucesso!"

def listar_usuarios():
    for usuario in usuarios:
        print(f"Usuário: {usuario} | senha: {usuarios[usuario]['senha']}")

def alterar_senha():
    usuario = input("Digite seu usuário: ")

    if usuario == "":
        return "Digite um usuário! Não tem nada aqui"

    elif usuario not in usuarios:
        return "Escreva um usuário certo!"

    else:
        nova_senha = input("Digite sua nova senha: ")
        if nova_senha == "":
            return "Digite uma senha! Não tem nada aqui!"
        else:
            usuarios[usuario]["senha"] = nova_senha

    return "Senha alterada com sucesso!!"

def remover_usuario():
    usuario = input("Digite um usuario válido: ")

    if usuario == "":
        return "Digite um usuário existente!"
    elif usuario not in usuarios:
        return "Digite um usuário válido!"
    else:
        del usuarios[usuario]

    return "Usuário deletado com sucesso!"

def main():

    while True:

        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Alterar senha")
        print("4 - Remover usuário")
        print("5 - Sair")

        escolha = input("Escolha uma opção para ser executada: ")

        if escolha == "1":
            print(adicionar_usuario())

        elif escolha == "2":
            listar_usuarios()

        elif escolha == "3":
            print(alterar_senha())

        elif escolha == "4":
            print(remover_usuario())

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Faça uma escolha da lista!")

main()