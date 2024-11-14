dados = {}
pessoas = []
soma = media = 0
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: '))
    while True:
        dados['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    pessoas.append(dados.copy())
    while True:
        resp = str(input('Quer continuar: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*40)
print(pessoas)
print(f'A)   Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B)   A média de idade é de {media:5.2f} anos.')
print(f'C)   As mulheres cadastradas foram ', end=' ')
for p in pessoas:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end=' ')
print()
print(f'D)   Lista de pessoas que estão acima da média ',end=' ')
for p in pessoas:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print()
print('<<< ENCERRADO >>>')