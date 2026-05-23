usuario = "Gustavo123"
senha =  "123456789"

tentativas = 3

while tentativas > 0:

    usuario_teste = input("Insira o usuário: ")
    senha_teste = input('Insira a senha: ')

    login_certo = usuario_teste == usuario and senha_teste == senha

    if usuario_teste == "" or senha_teste == "":
        print("Preencha este campo!")
        continue

    elif login_certo:
        print("Parabéns! Você acertou o login! Ihuuuuuuu")
        break

    elif usuario != usuario_teste:
        print("Usuário errado! -1 tentativa")

    elif senha != senha_teste:
        print("Senha errada! -1 tentativa")

    tentativas -= 1

    if tentativas > 0:
        print(f"Restam {tentativas} tentativas restantes")

if tentativas == 0:
    print("suas tentativas acabaram...")