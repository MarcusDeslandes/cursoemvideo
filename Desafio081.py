valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'Os valores digitados foram {valores}')
print(f'A quantidade de números digitados foram {len(valores)}')
valores.sort(reverse=True)
print(f'A lista de valores ordenanda de forma DECRESCENTE é {valores}')
if 5 in valores:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 NÃO foi encontrado na lista')