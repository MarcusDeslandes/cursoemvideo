n = int(input('Digite um numero inteiro: '))
print('''Escolha uma opção para escolher a base de conversão:'
[ 1 ] Para converter para BINÁRIO
[ 2 ] Para converter para OCTAL
[ 3 ] Para converter para HEXADECIMAL''')
opc = int(input('Digite sua opção: '))
if opc == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(n,bin(n)[2:]))
elif opc == 2:
    print('O número {} convertido para OCTAL é {}'.format(n,oct(n)[2:]))
elif opc == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')