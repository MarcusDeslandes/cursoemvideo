f = str(input('Digite aqui a sua frase: ')).strip().upper() #eliminei os espaços e coloquei pra maiúsculo
palavras = f.split() #separei em uma lista
junto = ''.join(palavras) #juntei tudo em uma str só
inverso = ''
for letra in range (len(junto) -1, -1, -1,): #fui da ultima letra até a primeira voltando uma letra
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
