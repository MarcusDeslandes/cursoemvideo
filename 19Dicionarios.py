pessoas = {'nome': 'Marcus', 'Sexo': 'M', 'idade': 30}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys()) #printa os nomes dos itens que estão no dicionario
print(pessoas.values()) #printa só os itens do dicionario
print(pessoas.items()) #printa tudo do dicionário fazendo uma lista e colocando os itens em tuplas
for k in pessoas.keys(): #printa todos os nomes dos itens separadamente
    print(k)
for k in pessoas.values():#printa os itens do dicionário separadamente
    print(k)
for k, v in pessoas.items(): #faz a lista de tudo do jeito que quisermos com o print formatado
    print(f'{k} = {v}')
#del pessoas['sexo'] #deleta o item
#pessoas['nome'] = 'Leandro' #altera o item
#pessoas['peso'] = 98.5 #Adiciona chaves e itens
print('-='*30)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-='*30)
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()