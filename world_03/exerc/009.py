numbers = list()

for c in range(0, 5):
  n = int(input('Informe um valor: '))
  if c == 0 or n > numbers[-1]:
    numbers.append(n)
    print('Adicionado ao final da lista')
  else:
    index = 0
    while index < len(numbers):
      if n <= numbers[index]:
        numbers.insert(index, n)
        print(f'Adiciono na posição {index}')
        break
      index += 1

print('-' * 20)

print(f'Lista: {numbers}')
