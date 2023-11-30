from math import sqrt
import random
import emoji

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual {:.2f}'.format(num, raiz))

num = random.randint(1, 100)
print(num)

print(emoji.emojize('Olá mundo :alien::vulcan_salute:'))
