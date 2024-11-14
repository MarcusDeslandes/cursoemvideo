valor = float(input('Qual o valor das compras? R$:'))
print('''Escolha sua forma de pagamento ideal:
[ 1 ] À vista em DINHEIRO/CHEQUE
[ 2 ] À vista no CARTÃO
[ 3 ] Em até 2x no CARTÃO
[ 4 ] Em 3x ou mais no CARTÃO''')
opc = int(input('Escolha sua opção: '))
if opc == 1:
    print('Você recebeu um desconto de 10%. O valor da compra fica em R${:.2f}'.format(valor - (valor * 10 / 100)))
elif opc == 2:
    print('Você recebeu um desconto de 5%. O valor da compra fica em R${:.2f}'.format(valor - (valor * 5 / 100)))
elif opc == 3:
    print('Sua compra será parcelada em 2x de R${} SEM JUROS'.format(valor/2))
    print('Sua compra não teve desconto ou acrescimo de juros. O valor da compra fica em R${:.2f} no final'.format(valor))
elif opc == 4:
    total = valor + (valor * 20 / 100)
    parc = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc,total/parc))
    print('O valor da sua compra de R${} vai custar R${:.2f} no final'.format(valor,total))
else:
    print('OPÇÃO DE PAGAMENTO INVÁLIDA. Tente novamente!')
