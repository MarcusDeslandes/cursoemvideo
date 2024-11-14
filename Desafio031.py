d = float(input('Qual a distância da viagem em Km: '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))
if d <=200:
    preço = d * 0.50
else:
    preço = d * 0.45
print('O valor da sua passagem será de R${:.2f}'.format(preço))
print('Boa viagem!')