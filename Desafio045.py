import sys
import pygame
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
print('Vamos jogar JOKENPÔ')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opc = int(input('Qual é a sua jogada? '))
if opc >=3:
    print('Jogada inválida. Tente novamente!')
    sys.exit()
pygame.init()
pygame.mixer.music.load('jankenpo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO!!!')
pygame.time.delay(1000)
c = randint(0,2)
print('-='*15)
print('Computador jogou {}'.format(itens[c]))
print('Jogador jogou {}'.format(itens[opc]))
print('-='*15)
if c == 0: #computador jogou pedra
    if opc == 0:
        print('\033[1;43mEMPATAMOS\033[m')
    elif opc == 1:
        print('\033[1;42mJOGADOR VENCEU\033[m')
    elif opc == 2:
        print('\033[1;41mCOMPUTADOR VENCEU\033[m')
elif c == 1: #computador jogou papel
    if opc == 0:
        print('\033[1;41mCOMPUTADOR VENCEU\033[m')
    elif opc == 1:
        print('\033[1;43mEMPATAMOS\033[m')
    elif opc == 2:
        print('\033[1;42mJOGADOR VENCEU\033[m')
elif c == 2: #computador jogou tesoura
    if opc == 0:
        print('\033[1;42mJOGADOR VENCEU\033[m')
    elif opc == 1:
        print('\033[1;41mCOMPUTADOR VENCEU\033[m')
    elif opc == 2:
        print('\033[1;43mEMPATAMOS\033[m')
