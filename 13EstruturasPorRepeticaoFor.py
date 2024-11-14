# laço c no intervalo(1,10):
#   passo
# pega

'''for c in range(1,10):

for c in range(0,3):
    passo
    pula
passo
pega

for c in range (0,3):
    if moeda:
        pega
    passo
    pula
passo
pega'''
#repetição
for c in range(0,6):
    print('Oi')
print('FIM')
# contagem
for c in range (0,6):
    print(c)
print('FIM')
#contagem regressiva
for c in range (6, 0, -1):
    print(c)
print('FIM')
#pulando numeros
for c in range (0, 7, 2):
    print(c)
print('FIM')
#com interação
n = int(input('Digite um número: '))
for c in range (0, n+1):
    print(c)
print('FIM')
#programa passo
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
#repetição de input
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s +=n
print('O somatório de todos os valores foi {}'.format(s))
