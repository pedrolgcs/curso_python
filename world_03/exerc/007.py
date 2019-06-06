numbers = []

for i in range(0, 5):
  numbers.append(int(input(f'Digite um valor para posição {i}: ')))

print('=-=' * 11)

print(f'O maior valor digitado foi: {max(numbers)} nas posições: ', end =' ')
for i, v in enumerate(numbers):
  if v == max(numbers):
    print(f'{i}', end = ' ')

print(f'\nO menor valor digitado foi: {min(numbers)} nas posições: ', end = ' ')
for i, v in enumerate(numbers):
  if v == min(numbers):
    print(f'{i}', end = ' ')

print(numbers)
