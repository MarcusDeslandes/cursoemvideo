lanche = ['hamburger', 'suco', 'pizza', 'pudim'] # Lista semrpe em []
print(lanche)
lanche[3] = 'picole' # Troca o item da lista
print(lanche)
lanche.append('cookie') # Comando que adiciona item ao final da lista
print(lanche)
lanche.insert(0,'cachorro quente') # Adiciona itens em posições especificas na lista
print(lanche)
del lanche[3] # Apaga o item na posição / pode ser feito com o comando lanche.pop(3) comumente usado para apagar o ultimo
lanche.remove('pizza') # Apaga o item da lista pelo nome do item

if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4,11)) # Cria uma lista com o range ja em ordem
valores.sort() # Organiza os itens
valores.sort(reverse=True) # Organiza ao contrário

len(valores) # Conta os elementos da lista

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei ou numero 5')
print(num)
print(f'Esta lista tem {len(num)} elementos')

valores = list()
for cont in range(0,5):
    valores.append(int(input('digite um valor: ')))
print(valores)
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a # isso liga as duas listas. Para copiar os itens é colocar b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')