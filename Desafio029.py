vel =  float(input('Qual a velocidade do carro? '))
limite = float(80)
multa = (vel-80) * 7
if vel >80:
    print('Você ultrapassou o limite permitido de {:.0f}Km/h. Você será MULTADO!'.format(limite))
    print('Sua multa é no valor de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com responsabilidade!')