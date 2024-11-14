print('CONVERSOR DE MOEDA')

r=float(input('Diga aqui quantos Reais (R$) você tem em sua carteira: R$'))
d=(r/5.58)
e=(r/6.10)

print('Hoje você possui {}, \nque se convertido para o dólar (US$), dada a sua cotação atual, você teria hoje: \nUS$: {:.2f}'.format(r,d))
print('Convertido para o Euro, você teria: \n€: {:.2f}'.format(e))