from random import randint
print('-'*30)
print('Vamos jogar par ou ímpar'.upper())
print('-'*30)
v = 0
while True:
    jogador = int(input('Digite seu número: '))
    computador = randint(0,10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? {P/I} ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {soma}')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes!')
