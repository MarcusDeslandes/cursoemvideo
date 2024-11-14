'''if True:
    if chao
        passo
    if buraco
        pula
    if moeda
        pega
    if trofeu
        pula
        break
pega'''

'''cont = 1
while True:
    print(cont, ' -> ', end = ' ')
    cont += 1
print('acabou')'''

n = s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha {salário:.2f}') #PYTHON 3.6+
print('o {} tem {} anos.'.format(nome,idade)) #PYTHON 3
print('o %s tem %d anos.' % (nome, idade)) #PYTHON 2
