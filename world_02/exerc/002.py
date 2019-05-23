number = int(input('x: '))

print(''' Escolha uma das bases para converter:
[ 1 ] Binários
[ 2 ] Octal
[ 3 ] Hexadecimal
''')
option = int(input('opção: '))

if option == 1:
  print('{} convertido para binário é: {}'.format(number, bin(number)[2:]))
elif option == 2:
  print('{} convertido para octal é: {}'.format(number, oct(number)[2:]))
elif option == 3:
  print('{} convertido para hexadecimal é: {}'.format(number, hex(number)[2:]))
else:
  print('Opção não existe')
