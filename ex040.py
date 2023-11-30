#  Crie um programa que leia duas notas
#  de um aluno e calcule sua média, mostrando
#  uma mensagem no final, de acordo com a média
#  atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a \033[4;30mPRIMEIRA\033[m nota: '))
n2 = float(input('Digite a \033[4;30mSEGUNDA\033[m nota: '))

media = (n1 + n2) / 2

print('Sua média com a nota \033[33m{}\033[m e \033[33m{}\033[m é \033[33m{}\033[m.'.format(n1, n2, media))
if 5 <= media <= 6.9:
    print('Você está em \033[1;33mRECUPERAÇÃO\033[m!')
elif media >= 7:
    print('Você foi \033[1;36mAPROVADO\033[m! Parabéns!')
else:
    print('Você foi \033[1;31mREPROVADO\033[m! Estude mais!')