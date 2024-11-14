n=int(input('Digite um número que eu farei a tabuada ele para você: '))
for c in range(1,11):
    print('{} x {:2} = {}'.format(n, c, n * c))