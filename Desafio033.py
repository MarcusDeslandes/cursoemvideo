a = int(input('Digite um número: '))
b: int = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi \033[30;41m{}\033[m'.format(menor))
print('O maior valor digitado foi \033[30;41m{}\033[m'.format(maior))
