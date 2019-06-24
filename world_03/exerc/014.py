data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
  for c in range(0, 3):
    data[l][c] = int(input(f'Digite um valor para posição [{l}][{c}]: '))

print('-' * 20)

for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{data[l][c]:^5}]', end = '')
  print()
