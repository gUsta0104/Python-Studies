numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite o próximo número: '))

operacao = str(input('Digite qual operação usar: '))

if operacao == '+':
    print(numero1 + numero2)
elif operacao == '-':
    print(numero1 - numero2)
elif operacao == '*':
    print(numero1 * numero2)
elif operacao == '/':
    if numero2 == 0:
        print('Conta inválida!')
    else:
        print(numero1 / numero2)

else:
    print("Operação Inválida!")