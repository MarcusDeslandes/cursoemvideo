time = []
ficha = {}
gols = []
while True:
    ficha.clear()
    ficha['Nome'] = str(input('Nome do Jogador: '))
    part = int(input(f'Quantas partidas {ficha['Nome']} jogou? '))
    gols.clear()
    for g in range(0,part):
        gols.append(int(input(f'Quantos gols na partida {g+1}: ')))
    ficha['Gols'] = gols[:]
    ficha['total'] = sum(gols)
    time.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in ficha.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f' {k+1:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador ? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}.')
    else:
        print(f' --  LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i} fez {g} gols.')
    print('-='*30)
print('<< VOLTE SEMPRE >>')
