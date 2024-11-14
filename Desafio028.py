from random import randint
from time import sleep
print('-=-' * 20)
print('Vamos jogar um jogo de advinhação')
n=int(input('Tente advinhar em qual número eu pensei entre 0 e 5. Digite aqui: '))
c = randint(0,5) # faz o computador "pensar"
print('-=-'*20)
print('PROCESSANDO...')
sleep(2) # Coloca tempo para esperar o resultado
print('-=-'*20)
if n == c:
    print('Parabéns! Você venceu! Eu pensei no {} e você disse {}'.format(c,n))
else:
    print('Que pena! Você perdeu! Eu pensei no {} e você no {}'.format(c,n))
