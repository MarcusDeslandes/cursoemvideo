print('='*30)
print('10 PRIMEIROS TERMOS DA PA')
print('='*30)
pt = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))

