#  Faça um programa que leia um número Inteiro e
#  mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
soma = num + 1
sub = num - 1
print('Analisando o número {}, seu antecessor é {} e seu sucessor é {}'.format(num, sub, soma))

num = int(input('Digite um número inteiro: '))
print('Analisando o número {}, seu antecessor é {} e seu sucessor é {}'.format(num, (num - 1), (num + 1)))

#  usar a 2ª opção quando não precisar das variáveis depois
