from datetime import date
ficha = dict()
ficha['Nome'] = str(input('Nome: '))
ficha['Idade'] = int(input('Ano de Nascimento: '))
ficha['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['CTPS'] != 0:
    ficha['Ano de Contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário R$: '))
    ficha['Aposentadoria'] = ficha['Ano de Contratação'] - ficha['Idade'] + 35
ficha['Idade'] = date.today().year - ficha['Idade']
print('-='*30)
for k, v in ficha.items():
    print(f'     - {k} tem o valor {v}')
