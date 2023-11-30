#  Faça um programa que leia o sexo de
#  uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#  Caso esteja errado, peça a digitação novamente
#  até ter um valor correto.

'''while True:
    sexo = str(input('Digite seu sexo: [F/M] ')).strip().upper()[0]  # 0 para pegar apenas a primeira letra da palavra
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print('Dados inválidos.')'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))

