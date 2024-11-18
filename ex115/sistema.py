from ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opcão 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema ... Até logo!')
        sleep(1)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1)
