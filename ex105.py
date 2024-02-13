# Faça um programa que tenha uma função notas() que pode
# receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:

# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def media_das_notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    resp = {'total': len(notas), 'maior': max(notas), 'menor': min(notas), 'media': sum(notas) / len(notas)}
    if situacao:
        if resp['media'] >= 7:
            resp['situacao'] = 'BOA'
        elif resp['media'] >= 5:
            resp['situacao'] = 'RAZOÁVEL'
        else:
            resp['situacao'] = 'RUIM'
    return resp


resposta = media_das_notas(5.5, 2.5, 9, 8.5, situacao=True)
print(resposta)
help(media_das_notas)
