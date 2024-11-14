print('-'*20)
print('CADASTRE UMA PESSOA')
tot18 = homem = m20 = 0
while True:
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >=18:
            tot18 += 1
        if sexo == 'M':
            homem += 1
        if sexo == 'F' and idade < 20:
            m20 += 1
    cont = ' '
    print('-'*20)
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {m20} mulheres com menos de 20 anos')