nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade <= 0:
    print('Idade inválida!')
elif idade < 18:
    print(f'{nome}, acesso negado.')
else:
    print(f'{nome}, acesso permitido.')