cadastro = list()
itens = list()
maip = menp = 0
while True:
    itens.append(str(input('Nome: ')))
    itens.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maip = menp = itens[1]
    else:
        if itens[1] > maip:
            maip = itens[1]
        if itens[1] < menp:
            menp = itens[1]
    resp = str(input('Quer Continuar? [S/N] '))
    cadastro.append(itens[:])
    itens.clear()
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso foi de {maip}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == maip:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menp}Kg. Peso de ', end='')
for p in cadastro:
    if p[1] == menp:
        print(f'{p[0]} ', end='')
        