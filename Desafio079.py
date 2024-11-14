valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar: [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}', end=' ')