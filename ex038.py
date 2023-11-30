#  Escreva um programa que leia dois números
#  inteiros e compare-os. mostrando na tela uma
#  mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

print('\033[35m-=-\033[m' * 6)
print('\033[1;35mComparando números\033[m')
print('\033[35m-=-\033[m' * 6)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O \033[4;36mPRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O \033[4;31mSEGUNDO\033[m valor é maior')
else:
    print('Não existe valor maior, os dois são \033[4;34mIGUAIS\033[m')
