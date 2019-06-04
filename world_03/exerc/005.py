items = (
  'Lapis', 1.75,
  'Borracha', 2.45,
  'Caderno', 15.90,
  'Mocilha', 120
)
print('-' * 40)
print(f'{"Lista de Preços":^40}')
print('-' * 40)

for item in (range(0, len(items))):
  if item % 2 == 0:
    print(f'{items[item]:.<30}', end='')
  else:
    print(f'R$ {items[item]:>5.2f}')

print('-' * 40)