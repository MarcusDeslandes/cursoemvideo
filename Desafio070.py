print('-'*40)
nome = 'LOJA SUPER BARATÃO'
print(f'{nome:^38}')
print('-'*40)
barato = ''
nomeproduto = ''
total = mais1000 = menor = cont = 0
while True:
    nomeproduto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nomeproduto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compras foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
