import random
prof=input('Qual o seu nome, Professor(a)? ')
print('Sorteio para ordem de apresentação de trabalho')
a1=input('Qual o nome do primeiro aluno? ')
a2=input('Qual o nome do segundo aluno? ')
a3=input('Qual o nome do terceiro aluno? ')
a4=input('Qual o nome do Quarto aluno? ')
lista =[a1,a2,a3,a4]
random.shuffle(lista)
print('Vamos sortear a ordem de apresentação')
print('A odrdem de apresentação será')
print(lista)