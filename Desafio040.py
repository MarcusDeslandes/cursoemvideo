n1 = float(input('Digite sua primeira nota: '))
n2= float(input('Digite a sua segunda nota: '))
media = (n1 + n2) / 2
print('A média foi {:.1f}'.format(media))
if media <= 5.0:
    print('O aluno está REPROVADO')
elif media >= 7.0:
    print('O aluno está APROVADO')
else:
    print('O aluno ficou em RECUPERAÇÃO')