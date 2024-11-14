casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Qual o salário do comprador? '))
ano = int(input('Em quantos anos será o pagamento? '))
prest = casa / (ano * 12)
print('Para o pagamento do valor do empréstimo de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa,ano,prest))
if prest <= (salario * 30) / 100:
    print('Parabéns! Seu empréstimo pode ser CONCEDIDO!')
else:
    print('Que pena! Seu empréstimo foi NEGADO!')
