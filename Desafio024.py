cidade=str(input('Digite o nome da cidade: ')).strip()
print('A cidade é {}'.format(cidade))
print('A cidade citada começa com a palavra "Santo"?')
print(cidade[:5].upper() == 'SANTO')