frase=str(input('Escreva uma frase: ')).upper().strip()
print('A letra "a" aparece na frase quantas vezes?')
print(frase.count('A'))
print('Em que posição ela aparece pela primeira vez?')
print(frase.find('A')+1)
print('Em que posição ela aparece pela última vez?')
print(frase.rfind('A')+1)
