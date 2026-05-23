usuario = "gustavo123"
senha = "123456789"

usuario1 = input('Digite o nome de usuário: ')
senha1 = input('Digite a senha: ')

tudo_correto = usuario == usuario1 and senha == senha1

if tudo_correto:
    print('Parabens! Você acertou o usuário e senha!')

elif usuario != usuario1 and senha == senha1:
    print('Usuário incorreto!')
elif usuario == usuario1 and senha != senha1: 
    print('Senha incorreta!')
else:
    print('tudo errado!!')