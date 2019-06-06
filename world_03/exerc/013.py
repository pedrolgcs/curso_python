numbers = [[], []]

for i in range(0, 7):
  number = int(input('number: '))
  if number % 2 == 0:
    numbers[0].append(number)
  else:
    numbers[1].append(number)

numbers[0].sort()
numbers[1].sort()

print(f'Pares: {numbers[0]}')
print(f'Impares: {numbers[1]}')
