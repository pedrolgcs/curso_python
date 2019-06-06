foods = ['Pastel', 'pizza', 'coca-cola', 'Pudim', 'Hamburguer']

foods.append('Suco de laranja')
print(foods)

foods.insert(0, 'File')
print(foods)

foods.pop()
# foods.pop(index)
# foods.remove('Pudim')
print(foods)

for n in foods:
  if n in 'pizza':
    foods.remove('pizza')
print(foods)

numbers = [1, 3, 4, 2]
# numbers.sort(reverse = True)
numbers.sort()
print(numbers)

for i, v in enumerate(numbers):
  print(f'index: {i}, valor: {v}')
