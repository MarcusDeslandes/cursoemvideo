from time import sleep
print('='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Essas retas PODEM FORMAR um triângulo')
    print('Analisando o tipo do triangulo')
    print('=' * 30)
    sleep(2)
    if r1 == r2 == r3:
        print('Esse triângulo é um EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é um ESCALENO')
    else:
        print('Esse triângulo é um ISÓSCELES')
else:
    print('Essas retas NÃO PODEM FORMAR um triângulo')
# O sinal    !=    significa DIFERENTE
