def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)

#programa principal
escreva('Gustavo Guanabara')
escreva(' Curso de Python no YouTube')
escreva('  CeV  ')
