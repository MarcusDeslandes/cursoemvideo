lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
# Tuplas são imutáveis
print(lanche[1])
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-'*40)
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche [cont]} na posição {cont}')
print('-'*40)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# print(sorted(lanche)) = Sorted põe em ordem
print('-'*40)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
# print(c.count()) = conta quantas vezes o item em () aparece na tupla

# print(c.index()) = mostra em qual posição está o item em () na tupla

# posso ter dados de tipos diferentes dentro das tuplas EX: ('Gustavo, 39, 'M', 99.88)

# del(tupla) = apaga a tupla