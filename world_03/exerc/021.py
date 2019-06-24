person = {}
goal_rounds = []

person['name'] = str(input('Nome do jogador: '))
person['rounds'] = int(input(f'Quantas partidas {person["name"]} jogou: '))

for goal in range(0, person['rounds']):
  goal_rounds.append(int(input(f'Quantos gols fez no jogo {goal}: ')))
  person['goal'] = goal_rounds[:]

person['total_goal'] = sum(goal_rounds)

print('-' * 20)
print(person)

print('-' * 20)
for key, value in person.items():
  print(f'O campo {key} tem o valor {value}')

print('-' * 20)
for i, v in enumerate(person['goal']):
  print(f'  => Na partida {i}, fez {v} gols')

