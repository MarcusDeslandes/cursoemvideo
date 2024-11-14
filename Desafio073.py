tabela = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Internacional', 'São paulo', 'Bahia', 'Cruzeiro',
          'Vasco', 'Atlético-MG', 'Grêmio', 'Vitória', 'Fluminense', 'Criciuma', 'Corinthians', 'Bragantino',
          'Athlético-PR', 'Juventude', 'Cuiabá', 'Atlético-GO')
print('='*80)
print(f'Lista de times do Brasileirão: {tabela}')
print(f'Os 5 primeiros da tabela são: {tabela[0:5]}')
print('='*80)
print(f'Os 4 últimos da tabela são {tabela[-4:]}')
print('='*80)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('='*80)
print(f'O Criciuma está na {tabela.index('Criciuma')+1}ª posição')