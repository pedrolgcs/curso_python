people = []
data = []
bigger = smaller = 0

while True:
  data.append(str(input('Nome: ')))
  data.append(float(input('Peso: ')))

  if len(people) == 0:
    bigger = smaller = data[1]
  else:
    if data[1] > bigger:
      bigger = data[1]
    if data[1] < smaller:
      smaller = data[1]

  people.append(data[:])
  data.clear()
  while True:
    choice = str(input('Deseja continuar: [S/N] '))
    if choice in ('SsNn'):
      break
  if choice in 'Nn':
    break

print(f'Os dados foram {people}')
print(f'Ao todo você cadastrou {len(people)} pessoas!')

print(f'O maior peso foi de {bigger}Kg -> ', end = '')
for p in people:
  if p[1] == bigger:
    print(f'[{p[0]}],', end = ' ')

print(f'\nO menor peso foi de {smaller}Kg -> ', end = '')
for p in people:
  if p[1] == smaller:
    print(f'[{p[0]}],', end = ' ')

print(f'\n ---')