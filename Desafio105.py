def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = {}
    dados['Total'] = len(n)
    dados['Maior'] = max(n)
    dados['Menor'] = min(n)
    dados['Média'] = sum(n) / len(n)
    if sit:
        if dados['Média'] >= 7:
            dados['Situação'] = 'BOA'
        elif dados['Média'] >= 5:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)