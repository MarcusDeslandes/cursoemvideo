from datetime import date
print('='*40)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('='*40)
nasc = int(input('Qual o ano de nascimento? '))
idade = date.today().year - nasc
print('O atleta naseu no ano {} e tem {} anos.\nEle se encaixa na categoria:'.format(nasc, idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
