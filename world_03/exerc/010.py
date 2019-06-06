numbers = list()

while True:
  numbers.append(int(input('Digite um valor: ')))
  while True:
    choice = str(input('Quer continuar? [S/N]: '))
    if choice in ('SsNn'):
      break
  if choice in 'Nn':
    break

print(f'Você digitou {len(numbers)} elementos')

numbers.sort(reverse = True)
print(f'Os valores em ordem decrescente são: {numbers}')

if 5 in numbers:
  print(f'O valor 5 foi inserido {numbers.count(5)} vezes')
