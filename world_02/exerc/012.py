import os
x = float(input('Primeiro valor: '))
y = float(input('Segundo valor: '))

while True:
  print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
  ''')
  choice = int(input('Qual sua escolha? '))

  if choice == 1:
    os.system('clear')
    print('A soma de {:.2f} + {:.2f} = {:.2f}'.format(x, y, x + y))
  elif choice == 2:
    os.system('clear')
    print('A multiplicação de {:.2f} * {:.2f} = {:.2f}'.format(x, y, x * y))
  elif choice == 3:
    os.system('clear')
    if x > y:
      print('O maior é {:.2f}'.format(x))
    elif x < y:
      print('O maior é {:.2f}'.format(y))
    else:
      print('Os números tem o mesmo valor')
  elif choice == 4:
    os.system('clear')
    x = float(input('Primeiro valor: '))
    y = float(input('Segundo valor: '))
  elif choice == 5:
    break
  else:
    print('Opção inválida')
