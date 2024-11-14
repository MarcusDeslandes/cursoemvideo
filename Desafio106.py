def ajuda(com):
    help(com)

comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    tamanho = len(comando)
    if comando.upper() == 'FIM':
        print('~')
        print('  ATÉ LOGO!  ')
        print('~')
        break

    else:
        print('~' * tamanho)
        print(f'  Acessando o manual do comando {comando}  ')
        print('~' * tamanho)
        ajuda(comando)