from random import randint
from time import sleep
from operator import itemgetter

ranking = []
numbers = {
  'player_1': randint(1, 6),
  'player_2': randint(1, 6),
  'player_3': randint(1, 6),
  'player_4': randint(1, 6)
}

for key, value in numbers.items():
  print(f'{key} -> {value}')
  sleep(0.5)

ranking = sorted(numbers.items(), key = itemgetter(1), reverse = True)

print('=-=' * 11)

print(ranking)
for index, value in enumerate(ranking):
  print(f'{index + 1}º lugar: {value[0]} com {value[1]} pontos')
