geral = [[],[]]
num = 0
for n in range(1,8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        geral[0].append(num)
    else:
        geral[1].append(num)
geral[0].sort()
geral[1].sort()
print('-='*40)
print(f'Os valores pares digitados foram {geral[0]}')
print(f'Os valorese ímpares digitados foram {geral[1]}')
print(geral)