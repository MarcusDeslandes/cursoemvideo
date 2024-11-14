def area(larg, comp):
    t = larg * comp
    print('-'*45)
    print(f'A área de um terreno {a} x {b} é de {t}m²')

#programa principal
print('Controle de Terrenos')
print('-'*25)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)