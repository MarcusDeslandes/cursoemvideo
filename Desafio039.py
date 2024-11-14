from datetime import date
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print('Você ja deveria ter se alistado há {} anos.\nSeu alistamento foi em {}.'.format(idade - 18, ano + 18))
else:
    print('Ainda faltam {} anos para o seu alistamento.\nSeu alistamento será em {}.'.format(18 - idade, ano + 18))
