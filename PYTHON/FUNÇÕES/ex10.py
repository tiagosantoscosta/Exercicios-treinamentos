def notas(*n, sit=False):
    """-> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobra a atual turma."""
    print('='*40)
    r = dict()                  #RESOLVI 90%
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação']=('BOA')   
        elif r['media'] <= 5:
             r['situação']=('RUIM')
        elif r['media'] >5 and r['media'] < 7:
            r['situação']=('RAZOÁVEL')
    return r 


resp = notas(7)
print(resp)
help(notas)