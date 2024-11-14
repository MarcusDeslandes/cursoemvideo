print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)
pt = int(input('Qual é o primeiro termo ? '))
r = int(input('Qual a razão ? '))
d = pt + (10-1) * r
for c in range(pt, d + r, r):
    print(c, end=' ')
print('ACABOU')
