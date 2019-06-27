from time import sleep

def count(index, final, salt):
  print(f'Contagem de {index} até {final} de {salt} em {salt}')

  if salt < 0:
    salt *= -1
  if salt == 0:
    salt = 1

  if index < final:
    cont = index
    while cont <= final:
      print(cont, end = ' ')
      cont += salt
  else:
    cont = index
    while cont >= final:
      print(cont, end = ' ')
      cont -= salt
    print()

count(0, 10, 1)
print()
count(20, 14, 4)
print('Agora é sua vez de personalizar')
index = int(input('Início: '))
final = int(input('Final: '))
salt = (int(input('Pulo: ')))
count(index, final, salt)
print()