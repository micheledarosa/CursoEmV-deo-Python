# Faça um programa que leia nome e média de
# um aluno, guardando também a situação em um
# dicionário. No final, mostre o conteúdo da
# estrutura na tela.

alunos = dict()

alunos['nome'] = str(input('Nome: ')).strip()
alunos['média'] = float(input(f'Média de {alunos['nome']}: '))

if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif alunos['média'] >= 6:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'

print('-=' * 10)
print(f'Nome do aluno: {alunos['nome']}')
print(f'Sua média é {alunos['média']}')
print(f'Situação: {alunos['situação']}')

'''
for k, v in alunos.items():
    print(f'  - {k} é igual a {v}')'''
