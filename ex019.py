#  Um professor quer sortear um dos seus quatro
#  alunos para apagar o quadro. Faça um programa que ajude
#  ele, lendo o nome dos alunos e escrevendo na tela o nome
#  do escolhido.

from random import choice

aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
