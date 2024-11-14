peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O seu Índice de Massa Corporal (IMC) é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal')
elif imc <= 25:
    print('Você está no peso IDEAL')
elif imc <= 30:
    print('Você está com SOBREPESO')
elif imc <= 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')