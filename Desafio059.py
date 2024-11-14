from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
cont = 1
while opcao != 5:
    print('''o que você quer fazer?
          [1] SOMAR
          [2] MULTIPLICAR
          [3] MAIOR
          [4] NOVOS NUMEROS
          [5] SAIR DO PROGRAMA''')
    opcao = int(input('>>>>> Qual a sua opção ? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a {}'.format(n1,n2,soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é igual á {}'.format(n1,n2,multi))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é o {}'.format(n1))
        elif n1 == n2:
            print('Não existe valor maior. Os dois são iguais')
        else:
            print('O maior valor é o {}'.format(n2))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('-=-'*20)
sleep(1)
print('Fim do programa. Volte sempre!')
print('-=-'*20)