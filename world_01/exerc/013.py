from random import randint
from time import sleep

number = randint(0, 5)
choice = int(input('Adivinhe o número: '))

print('Processando...')
sleep(2)

if choice == number:
  print('Parabéns você acertou, o número sortado foi: {}'.format(choice))
else:
  print('você errou, o número sorteado foi: {}'.format(number))
