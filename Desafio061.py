print('='*30)
print('10 PRIMEIROS TERMOS DA PA')
print('='*30)
pt = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo = termo + r
    cont = cont + 1
print('Acabou')