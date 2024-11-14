# Interactive Help (oferece documentação de ajuda sobre todosd os comandos)
#help(print)
#print(input.__doc__)

#docstrings (coloca descrição das funçoes que voce cria)
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('FIM')

help(contador)

#Parâmetros Opcionais (adicionar =0 no def para ser opcional colocar valor)
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(1,5,6)
somar(4,6)
somar()
somar(b=4, c=2)
print()

#Escopo de Variáveis
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')
print()

def teste(b):
    global a #Esse comando coloca a variavel que ta dentro pra fora
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
print()

#Retornando Valores (Coloca os resultados em variaveis de retorno com o comando "return"
def subtrair(a=0, b=0, c=0):
    s = a - b - c
    return s

r1 = subtrair(9, 2, 1)
r2 = subtrair(10, 5)
r3 = subtrair(9)

print(f'Os resultados foram {r1}, {r2}, {r3}')
print()

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}')
print()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número para saber se é par ou impar: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')