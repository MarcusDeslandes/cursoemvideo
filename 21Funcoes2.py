# Interactive Help (oferece documentação de ajuda sobre todosd os comandos)
#help(print)
#print(input.__doc__)

#docstrings
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