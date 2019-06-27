def player(name = '<desconhecido>', goal = 0):
  return print(f'O jogador {name}, fez {goal} gols no campeonato')

name = str(input('Nome do jogador: '))
goal = str(input('Quantidade de gols: '))

if goal.isnumeric():
  goal = int(goal)
else:
  goal = 0

if name.strip() == '':
  player(goal = goal)
else:
  player(name, goal)
