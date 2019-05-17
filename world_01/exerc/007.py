import random

print('-' * 10)

a1 = str(input('a1: '))
a2 = str(input('a2: '))
a3 = str(input('a3: '))
a4 = str(input('a4: '))
lista = [a1, a2, a3, a4]
winner = random.choice(lista)
print('O ganhador foi: {}'.format(winner))

print('-' * 10)