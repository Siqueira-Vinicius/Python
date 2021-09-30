def notas(* nots, sit=False):
    """ - Função notas, para analisar a situação das notas de uma turma com varios alunos;
        notas(* nots, sit=False)
        nots: inserir notas de varios alunos (aceita valores float)
        sit: avalia situação da turma, opcional (True,False)
        return: retorna um dicionario com a quantidade de notas, maior e menor nota, media da turma e situação
    """
    dic = {}
    dic['quantidade de notas'] = len(nots)
    dic['maior nota'] = max(nots)
    dic['menor nota'] = min(nots)
    dic['média da turma'] = sum(nots)/len(nots)
    if sit:
        if dic['média da turma'] > 7:
            dic['situação'] = 'boa'
        else:
            dic['situação'] = 'ruim'
    return dic


print(notas(5.5,2.5,9,8.5, sit=True))
help(notas)