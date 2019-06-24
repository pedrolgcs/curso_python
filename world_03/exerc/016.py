from random import randint
numbers = []
games = []
cont = 0

print('-' * 30)
print('      Joga na Mega Sena    ')
print('-' * 30)

choice = int(input('Quantos jogos deseja realizar: '))

for i in range(0, choice):
  while True:
    n = randint(1, 60)
    if n not in numbers:
      numbers.append(n)
      cont += 1
    if cont >= 6:
      cont = 0
      break
  numbers.sort()
  games.append(numbers[:])
  numbers.clear()

for i, l in enumerate(games):
  print(f'Jogo {i}: {l} ')
