usuario = {
    'gustavo': '123',
    'admin' : '999',
    'teste' : 'abc'
}

tentativas = 3

while tentativas > 0:

    login_teste = input('Coloque seu login: ')

    if login_teste == "":
        print("Coloque um Usuário!")
        continue

    elif login_teste not in usuario:
        print("Erro!! Usuário errado")
        tentativas -= 1

        if tentativas > 0:
            print(f'Restam {tentativas} tentativas')

        continue

    senha_teste = input('Coloque sua senha: ')
    senha_correta = usuario[login_teste]

    if senha_teste == senha_correta:
        print("Login completo!")
        break

    else:
        print("Senha incorreta :(")
        tentativas -= 1
        if tentativas > 0:
            print(f'Restam {tentativas} tentativas')

if tentativas == 0:
    print("Suas tentativas acabaram...")