def read_number(text):
  while True:
    number = str(input(text))
    if number.isnumeric():
      number = int(number)
      return number
      break
    else:
      print('Error..')


number = read_number('Digite um número: ')
print(f'Você acabou de digitar o número {number}')
