ficha = {}
gols = []
ficha['Nome'] = str(input('Nome do Jogador: '))
part = int(input(f'Quantas partidas {ficha['Nome']} jogou? '))
for g in range(0,part):
    gols.append(int(input(f'Quantos gols na partida {g+1}: ')))
ficha['Gols'] = gols
ficha['total'] = sum(gols)
print('-='*30)
print(ficha)
print('-='*30)
for k, v in ficha.items():
    print(f'    O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {ficha['Nome']} jogou {part} partidas.')
for i, v in enumerate(gols):
    print(f'    => Na partida {i+1}, fez {v} gols')
print(f'Foi um total de {ficha['total']} gols!')
