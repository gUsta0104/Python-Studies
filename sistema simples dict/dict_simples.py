usuarios = {
    "gustavo": {"senha": "123", "tentativas": 3},
    "admin": {"senha": "999", "tentativas": 3},
    "teste": {"senha": "abc", "tentativas": 3}
}

while True:

    usuario = input("Digite o usuário: ")

    if usuario == "":
        print("Digite um usuário!!")
        continue

    elif usuario not in usuarios:
        print("Usuário errado!")
        continue

    elif usuarios[usuario]["tentativas"] == 0:
        print("Suas tentativas acabaram")
        continue

    senhaT = input("Digite a senha: ")

    if senhaT == usuarios[usuario]["senha"]:
        print("Senha correta, parabéns!!")
        break

    else:
        usuarios[usuario]["tentativas"] -= 1

        if usuarios[usuario]["tentativas"] == 0:
            print("Suas tentativas acabaram!")

        else:
            print(f"ainda faltam {usuarios[usuario]['tentativas']}")