from random import randint
from time import sleep
print('-=-' *20)
print('Vamos jogar um jogo de advinhação')
print('-=-'*20)
print('Pensei em um número de 0 a 10!')
c = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    print('-=-' * 20)
    print('PROCESSANDO')
    print('-=-' * 20)
    sleep(1)
    palpites += 1
    if jogador == c:
        acertou = True
    else:
        if jogador < c:
            print('MAIS... tente novamente: ')
        elif jogador > c:
            print('MENOS... Tente novamente: ')
print('Você venceu em {} tentativas'.format(palpites))
