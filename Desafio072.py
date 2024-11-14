extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
cont = ' '
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Valor inválido! Tente novamente! ')
print(f'Você digitou o número {extenso[num]}')
while cont not in 'SN':
    cont = str(input('Quer continuar ? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('Programa encerrado! Volte sempre!')
