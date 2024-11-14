sal=float(input('Digite aqui o salario do funcionário: R$'))
porc=float(input('Qual o valor da porcentagem do aumento?'))
novo = sal + (sal * porc / 100)
print('O seu aumento foi de {:.0f}% baseado no seu salário atual.'.format(porc))
print('O novo salário é de\nR${:.2f}'.format(novo))


