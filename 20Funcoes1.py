def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    print('-'*20)

#programa principal
soma(4, 5)
soma(b=4, a=5) #troquei os itens de lugar

def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')

#programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def alfabeto(*letra): # o * faz com que o def receba varios itens em tuplas
    tam = len(letra)
    print(f'Recebi as letras {letra} e são ao todo {tam} letras.')

#programa principal
alfabeto('a', 'b', 'c')
alfabeto('k', 'j')
alfabeto('i', 'm', 'p', 'l', 'r')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
#programa principal
valores = [6, 4, 3, 5, 8, 0]
dobra(valores)
print(valores)