cont = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('-'*20)
    for c in range (1,11):
        print('{} x {:2} = {}'.format(n, c, n * c))
    print('-'*20)
print('Programa encerrado. Volte sempre!'.upper())