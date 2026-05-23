usuarios = {
    "gustavo": {"senha": "123", "tentativas": 3},
    "admin": {"senha": "999", "tentativas": 3},
    "teste": {"senha": "abc", "tentativas": 3}
}

def pedir_usuario():
    usuario = input("Digite um usuário: ")
    return usuario


def verificar_usuario(usuario, usuarios):
    if usuario in usuarios:
        return True
    else:
        return False

def tem_tentativas(usuario, usuarios):
    if usuarios[usuario]["tentativas"] > 0:
        return True
    else:
        return False

def verificar_senha(usuario, senha_digitada, usuarios):
    if senha_digitada == usuarios[usuario]["senha"]:
        return True
    else:
        return False


def diminuir_tentativas(usuario, usuarios):
    usuarios[usuario]["tentativas"] -= 1
    return None

def login ():
    while True:
        usuario = pedir_usuario()

        if usuario == "":
            return usuario

        elif usuario not in usuarios:
            continue

        elif usuarios[usuario]["tentativas"] == 0:
            continue


        senha = input("Digite a senha: ")

        if usuarios[usuario]["senha"] == senha:
            print("Senha correta!!")
            break

        elif usuarios[usuario]["senha"] != senha:
            print("Senha incorreta!!")
            usuarios[usuario]["tentativas"] -= 1

        elif usuarios[usuario]["tentativas"] == 0:
            print("Suas tentativas acabaram!!")

