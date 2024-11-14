s = 0
cont = 0
for n in range (1,7):
    num = int(input('Digite aqui o {}º número? '.format(n)))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print('Você informou {} numeros pares e soma deles foi {}'.format(cont,s))
