#  Desenvolva uma lógica que leia o peso e
#  a altura de uma pessoa, calcule seu Índice de
#  Massa Corporal (IMC) e mostre seu status, de
#  acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso(Kg): '))
alt = float(input('Digite sua altura(m): '))

imc = peso / (alt ** 2)  # ou alt * alt

print('O IMC ideal é entre 18,5 e 25.\nSeu IMC é {:.1f}: '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
