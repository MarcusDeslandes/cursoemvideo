from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} [e {moeda.dobro(p)}')
print(f'Aumentando em 10% temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo em 13% temos {moeda.diminuir(p, 13)}')
