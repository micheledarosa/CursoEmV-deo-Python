#  Crie um algoritmo que leia um número e mostre o
#  seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('Analisando o número {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n, dobro, triplo, raiz))

n = int(input('Digite um número: '))
print('Analisando o número {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n, (n * 2), (n * 3),
                                                                                                    (n ** (1/2))))
