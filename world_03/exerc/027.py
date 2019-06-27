from random import randint
from time import sleep

numbers = []

def random_number(numbers):
  print(f'Sorteando os 5 valores da lista: ', end = '')
  for n in range(0, 5):
    numbers.append(randint(1, 10))
    print(f'{numbers[n]}', end = ' ', flush = True)
    sleep(0.3)
  print('Pronto')
  return numbers

def sum_par(numbers):
  par = 0
  for n in numbers:
    if n % 2 == 0:
      par += n
  print(f'Somando os valores pares de {numbers}, temo {par}')
  return par


random_number(numbers)
sum_par(numbers)
