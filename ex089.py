# Crie um programa que leia nome e duas notas de
# vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de
# cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

from time import sleep

aluno_notas = list()
lista_completa = list()
media = list()
nota1 = nota2 = media_nota = 0

while True:
    aluno_notas.append(str(input('Nome do aluno: ')).strip())
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    aluno_notas.append(nota1)
    aluno_notas.append(nota2)
    media_nota = (nota1 + nota2) / 2
    media.append(media_nota)
    lista_completa.append(aluno_notas[:])
    aluno_notas.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Adicionar outro aluno? [S/N] ')).strip().upper()[0]
    if continua == 'N':
        break

print('-' * 30)
for i, aluno in enumerate(lista_completa):
    nome = aluno[0]
    media_nota = media[i]
    print(f'Média do aluno {nome}: {media_nota:.2f}')
print('-' * 30)

while True:
    consulta = ' '
    while consulta not in 'SN':
        consulta = str(input('Gostaria de consultar algum aluno? [S/N] ')).strip().upper()[0]
    if consulta == 'N':
        break
    nome_consulta = str(input('Digite o nome do aluno para consulta: ')).strip().upper()
    encontrado = False
    for aluno in lista_completa:
        if aluno[0].upper() == nome_consulta:
            encontrado = True
            print(f'Notas do aluno {nome_consulta}: {aluno[1]:.2f} e {aluno[2]:.2f}')
            break
    if not encontrado:
        print(f'Aluno {nome_consulta} não encontrado. Tente novamente.')

print('...')
sleep(1.5)
print('Programa finalizado.')
