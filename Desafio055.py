maior = 0
menor = 0
for p in range (1,6):
    peso = float(input('Digite o peso da {}ª pessoa (Kg): '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg'.format(maior))
print('Já o menor peso foi {}Kg'.format(menor))

