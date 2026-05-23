usuario = "Gustavo123"
senha = "123456789"

tentativas = 3

while tentativas > 0:
    usuario_teste = input("Insira um usuário: ")
    senha_teste = input("insira uma senha: ")
    if usuario_teste == usuario and senha_teste == senha:
        print("Parabens, você acertou!")
        break
    else:
        tentativas -= 1
        print(f'Faltam {tentativas} tentativas.')

if tentativas == 0:
    print("Suas tentativas acabaram!")