valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
print('-='*25)
for i, v, in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os números digitados foram {valores}')
print(f'Os numeros pares são {pares}')
print(f'Os números impares são {impares}')