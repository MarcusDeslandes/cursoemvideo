nome=str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
separa= nome.split()
print('Seu primeiro é {} e ele tem {} letras'.format(separa[0], len(separa[0])))