# numbers = []
numbers = list()

while True:
  n = int(input('Digite um valor: '))
  if n in numbers:
    print('Erro ao adicionar valor, ele já existe na lista')
  else:
    numbers.append(n)
    print('Valor adicionado com sucesso!')
  while True:
    choice = str(input('Quer continuar? [S/N]: '))
    if choice in ('SsNn'):
      break
  if choice in 'Nn':
    break

numbers.sort()
print(numbers)
print('=-=' * 10)
